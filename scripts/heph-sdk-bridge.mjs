#!/usr/bin/env node
import { spawn } from "node:child_process";
import { randomUUID } from "node:crypto";
import http from "node:http";
import { createInterface } from "node:readline";

const DEFAULT_PORT = 8766;
const DEFAULT_ALLOWED_ORIGINS = ["https://hephaion.vercel.app"];

function parseArgs(argv) {
  const parsed = {
    allowedOrigins: (process.env.HEPH_BRIDGE_ALLOWED_ORIGINS || "")
      .split(",")
      .map((origin) => origin.trim())
      .filter(Boolean),
    armory: process.env.HEPH_ARMORY || "",
    executable: process.env.HEPH_EXECUTABLE || "heph",
    port: Number(process.env.PORT || DEFAULT_PORT),
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--armory") {
      parsed.armory = argv[index + 1] || "";
      index += 1;
    } else if (arg === "--heph") {
      parsed.executable = argv[index + 1] || parsed.executable;
      index += 1;
    } else if (arg === "--port") {
      parsed.port = Number(argv[index + 1] || DEFAULT_PORT);
      index += 1;
    } else if (arg === "--allow-origin") {
      const origin = argv[index + 1] || "";
      if (origin) {
        parsed.allowedOrigins.push(origin);
      }
      index += 1;
    }
  }

  if (parsed.allowedOrigins.length === 0) {
    parsed.allowedOrigins = DEFAULT_ALLOWED_ORIGINS;
  }

  return parsed;
}

function requestOrigin(request) {
  return request.headers.origin || "";
}

function originAllowed(request) {
  const origin = requestOrigin(request);
  return !origin || options.allowedOrigins.includes(origin);
}

function setCorsHeaders(request, response) {
  const origin = requestOrigin(request);
  if (origin) {
    response.setHeader("Access-Control-Allow-Origin", origin);
    response.setHeader("Vary", "Origin");
  }
  response.setHeader("Access-Control-Allow-Headers", "Content-Type");
  response.setHeader("Access-Control-Allow-Methods", "GET,POST,OPTIONS");
  if (request.headers["access-control-request-private-network"] === "true") {
    response.setHeader("Access-Control-Allow-Private-Network", "true");
  }
}

function jsonResponse(request, response, status, payload) {
  setCorsHeaders(request, response);
  response.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
  });
  response.end(`${JSON.stringify(payload)}\n`);
}

function ndjsonHeaders(request, response) {
  setCorsHeaders(request, response);
  response.writeHead(200, {
    "Content-Type": "application/x-ndjson; charset=utf-8",
    "Cache-Control": "no-store",
  });
}

function readBody(request) {
  return new Promise((resolve, reject) => {
    let body = "";

    request.setEncoding("utf8");
    request.on("data", (chunk) => {
      body += chunk;
      if (body.length > 1_000_000) {
        reject(new Error("request body too large"));
        request.destroy();
      }
    });
    request.on("end", () => resolve(body));
    request.on("error", reject);
  });
}

const options = parseArgs(process.argv.slice(2));
const childArgs = ["sdk", "serve"];
if (options.armory) {
  childArgs.push("--armory", options.armory);
}

const child = spawn(options.executable, childArgs, {
  env: process.env,
  stdio: ["pipe", "pipe", "pipe"],
});

const pendingCalls = new Map();
const streams = new Map();
const stderrTail = [];
let readyPayload = null;
let latestState = null;
let sdkClosed = false;
let childFailure = "";

function rememberStderr(chunk) {
  stderrTail.push(String(chunk));
  while (stderrTail.join("").length > 4000) {
    stderrTail.shift();
  }
}

function markSdkUnavailable(error) {
  const message = error instanceof Error ? error.message : String(error);
  sdkClosed = true;
  childFailure = message;
  readyPayload = null;
  latestState = null;
  rememberStderr(`${message}\n`);

  for (const pending of pendingCalls.values()) {
    pending.reject(new Error(message));
  }
  pendingCalls.clear();

  for (const stream of streams.values()) {
    stream.response.write(
      `${JSON.stringify({
        type: "error",
        error: { code: "sdk_unavailable", message },
      })}\n`,
    );
    stream.response.end();
  }
  streams.clear();
}

function sdkUnavailableMessage() {
  return childFailure || "heph sdk is not ready";
}

function canWriteToChild() {
  return !sdkClosed && !child.stdin.destroyed && !child.stdin.writableEnded;
}

function writeRequest(method, params, id = randomUUID()) {
  if (!canWriteToChild()) {
    throw new Error(sdkUnavailableMessage());
  }

  try {
    child.stdin.write(`${JSON.stringify({ id, method, params })}\n`, (error) => {
      if (error) {
        markSdkUnavailable(error);
      }
    });
  } catch (error) {
    markSdkUnavailable(error);
    throw error;
  }
  return id;
}

function call(method, params) {
  return new Promise((resolve, reject) => {
    let id;
    try {
      id = writeRequest(method, params);
    } catch (error) {
      reject(error);
      return;
    }
    pendingCalls.set(id, { resolve, reject });
  });
}

async function refreshState() {
  try {
    const state = await call("state");
    latestState = state;
  } catch {
    // The health endpoint can still return the initial ready state.
  }
}

async function ensureSession() {
  try {
    await call("new_session");
    await refreshState();
  } catch {
    await refreshState();
  }
}

function routeMessage(message) {
  if (message.type === "ready") {
    readyPayload = message;
    latestState = message.state;
    ensureSession();
    return;
  }

  if (message.type === "response") {
    const pending = pendingCalls.get(message.id);
    if (!pending) {
      return;
    }
    pendingCalls.delete(message.id);
    if (message.ok) {
      pending.resolve(message.result);
    } else {
      pending.reject(new Error(message.error?.message || "SDK response failed"));
    }
    return;
  }

  if (message.type === "error") {
    const pending = pendingCalls.get(message.id);
    const stream = streams.get(message.id);
    if (pending) {
      pendingCalls.delete(message.id);
      pending.reject(new Error(message.error?.message || message.message || "SDK error"));
    }
    if (stream) {
      stream.response.write(`${JSON.stringify(message)}\n`);
      stream.response.end();
      streams.delete(message.id);
    }
    return;
  }

  if (message.type === "stream_start" || message.type === "stream_event") {
    const stream = streams.get(message.id);
    if (stream) {
      stream.response.write(`${JSON.stringify(message)}\n`);
    }
    return;
  }

  if (message.type === "stream_end") {
    const stream = streams.get(message.id);
    if (stream) {
      stream.response.write(`${JSON.stringify(message)}\n`);
      stream.response.end();
      streams.delete(message.id);
      refreshState();
    }
  }
}

createInterface({ input: child.stdout }).on("line", (line) => {
  if (!line.trim()) {
    return;
  }

  try {
    routeMessage(JSON.parse(line));
  } catch (error) {
    rememberStderr(`invalid sdk json: ${error.message}\n${line}\n`);
  }
});

child.stderr.on("data", rememberStderr);
child.on("error", (error) => {
  markSdkUnavailable(error);
});
child.on("exit", (code, signal) => {
  markSdkUnavailable(new Error(`heph sdk exited with ${code ?? signal}`));
});

const server = http.createServer(async (request, response) => {
  if (!originAllowed(request)) {
    response.writeHead(403, {
      "Content-Type": "application/json; charset=utf-8",
    });
    response.end(
      `${JSON.stringify({
        error: "origin is not allowed",
        allowedOrigins: options.allowedOrigins,
      })}\n`,
    );
    return;
  }

  if (request.method === "OPTIONS") {
    jsonResponse(request, response, 204, {});
    return;
  }

  if (request.method === "GET" && request.url === "/health") {
    if (!readyPayload) {
      jsonResponse(request, response, 503, {
        ready: false,
        error: sdkUnavailableMessage(),
        stderr: stderrTail.join("").slice(-1200),
      });
      return;
    }

    jsonResponse(request, response, 200, {
      ready: true,
      protocol: readyPayload.protocol,
      version: readyPayload.version,
      state: latestState || readyPayload.state,
    });
    return;
  }

  if (request.method === "POST" && request.url === "/prompt") {
    if (!readyPayload) {
      jsonResponse(request, response, 503, { error: "heph sdk is not ready" });
      return;
    }

    let payload;
    try {
      payload = JSON.parse(await readBody(request));
    } catch {
      jsonResponse(request, response, 400, { error: "request must be JSON" });
      return;
    }

    if (!payload.text || typeof payload.text !== "string") {
      jsonResponse(request, response, 400, { error: "text is required" });
      return;
    }

    if (!canWriteToChild()) {
      jsonResponse(request, response, 503, { error: sdkUnavailableMessage() });
      return;
    }

    ndjsonHeaders(request, response);
    const id = randomUUID();
    streams.set(id, { response });
    try {
      writeRequest("prompt", { text: payload.text }, id);
    } catch (error) {
      streams.delete(id);
      response.write(
        `${JSON.stringify({
          type: "error",
          error: { code: "sdk_unavailable", message: error.message },
        })}\n`,
      );
      response.end();
    }
    response.on("close", () => {
      if (!response.writableEnded) {
        try {
          writeRequest("abort");
        } catch {
          // The SDK is already unavailable; there is nothing left to abort.
        }
        streams.delete(id);
      }
    });
    return;
  }

  jsonResponse(request, response, 404, { error: "not found" });
});

server.listen(options.port, "127.0.0.1", () => {
  console.log(`Heph SDK bridge listening on http://127.0.0.1:${options.port}`);
});

function shutdown() {
  server.close();
  if (!child.stdin.destroyed && !child.stdin.writableEnded) {
    child.stdin.end();
  }
  const timer = setTimeout(() => child.kill(), 500);
  timer.unref();
}

process.on("SIGINT", shutdown);
process.on("SIGTERM", shutdown);
