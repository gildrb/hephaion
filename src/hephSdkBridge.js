const DEFAULT_BRIDGE_ORIGIN = "http://127.0.0.1:8766";

function bridgeOrigin() {
  return window.localStorage.getItem("heph.bridgeOrigin") || DEFAULT_BRIDGE_ORIGIN;
}

async function readNdjson(response, onMessage) {
  if (!response.body) {
    return;
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) {
      break;
    }

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() || "";

    for (const line of lines) {
      const trimmed = line.trim();
      if (trimmed) {
        onMessage(JSON.parse(trimmed));
      }
    }
  }

  const tail = buffer.trim();
  if (tail) {
    onMessage(JSON.parse(tail));
  }
}

export async function probeHephBridge({ signal } = {}) {
  const response = await fetch(`${bridgeOrigin()}/health`, {
    method: "GET",
    signal,
  });

  if (!response.ok) {
    throw new Error(`Bridge returned ${response.status}`);
  }

  const payload = await response.json();

  if (payload.protocol !== "heph-sdk-jsonl" || payload.ready !== true) {
    throw new Error("Not a Heph SDK bridge");
  }

  return payload;
}

export async function streamPromptThroughBridge(text, { onMessage, signal } = {}) {
  const response = await fetch(`${bridgeOrigin()}/prompt`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
    signal,
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || `Bridge returned ${response.status}`);
  }

  await readNdjson(response, onMessage);
}
