import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { probeHephBridge, streamPromptThroughBridge } from "./hephSdkBridge.js";

const INSTALL_SCRIPT = "uv tool install heph@latest\nheph\nheph --version";
const SECONDARY_INSTALL = "pip install heph";
const DEFAULT_SITE_ORIGIN = "https://hephaion.vercel.app";

const NAV_LINKS = [
  { href: "#install", label: "Install" },
  { href: "#cli", label: "Terminal" },
  { href: "#workflow", label: "Workflow" },
  { href: "#sdk", label: "Bridge" },
  { href: "#privacy", label: "Privacy" },
];

const DEFAULT_MATERIALS = [
  { path: "materials/course-outline.pdf", enabled: true },
  { path: "materials/week-04-retrieval.md", enabled: true },
  { path: "materials/problem-set.docx", enabled: false },
  { path: "materials/notes/calculus.txt", enabled: true },
];

const MODEL_CHOICES = [
  "gpt-5.5",
  "openai/gpt-5.5",
  "openrouter/qwen3",
  "local/llama.cpp",
];

const REASONING_LEVELS = ["low", "medium", "high", "xhigh"];

const INITIAL_TRANSCRIPT = [
  {
    id: "start",
    role: "notice",
    lines: [
      "OPEN ctrl+a",
      "OPEN exact armory name",
      "SCOPE ~/.armories",
      "MATERIALS materials/",
    ],
  },
];

const WORKFLOW_STEPS = [
  {
    title: "Create an armory",
    text: "Each project gets a normal folder under ~/.armories with source files, local memory, saved chats, traces, and rebuildable retrieval state.",
  },
  {
    title: "Ask with evidence",
    text: "Heph retrieves from enabled materials before the model answers, then keeps citations and the last turn evidence inspectable.",
  },
  {
    title: "Keep model access swappable",
    text: "Use /login and /models for OpenAI, OpenRouter, Pollinations, local llama.cpp, or a custom OpenAI-compatible endpoint.",
  },
];

const PROVIDERS = [
  ["Pollinations AI", "No account required", "Testing and casual use"],
  ["OpenRouter", "API key", "Many hosted models"],
  ["OpenAI", "API key or subscription login", "Production document work"],
  ["Local llama.cpp", "Local tool-capable model", "Private prompts on your machine"],
  ["Custom endpoint", "OpenAI-compatible API", "Self-hosted or enterprise routes"],
];

function App() {
  const [menuOpen, setMenuOpen] = useState(false);

  const closeMenu = useCallback(() => {
    setMenuOpen(false);
  }, []);

  const toggleMenu = useCallback(() => {
    setMenuOpen((current) => !current);
  }, []);

  useEffect(() => {
    function handleEscape(event) {
      if (event.key === "Escape") {
        setMenuOpen(false);
      }
    }

    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, []);

  return (
    <>
      <a className="skip-link" href="#main">
        Skip to main content
      </a>
      <Header menuOpen={menuOpen} onCloseMenu={closeMenu} onToggleMenu={toggleMenu} />
      <main id="main">
        <Hero />
        <InstallSection />
        <WorkflowSection />
        <SdkSection />
        <PrivacySection />
        <FinalCta />
      </main>
      <Footer />
    </>
  );
}

function Header({ menuOpen, onCloseMenu, onToggleMenu }) {
  return (
    <header className="site-header">
      <nav className="nav" aria-label="Primary navigation">
        <a className="brand" href="#top" aria-label="Hephaion home" onClick={onCloseMenu}>
          <img
            className="brand-logo"
            src="/assets/logo-auto.v0.0.49.svg"
            alt=""
            aria-hidden="true"
          />
        </a>
        <button
          className="nav-toggle"
          type="button"
          aria-expanded={menuOpen}
          aria-controls="primary-menu"
          onClick={onToggleMenu}
        >
          Menu
        </button>
        <div className="nav-links" id="primary-menu" data-open={menuOpen}>
          {NAV_LINKS.map((link) => (
            <a href={link.href} key={link.href} onClick={onCloseMenu}>
              {link.label}
            </a>
          ))}
        </div>
        <a className="nav-cta" href="#install">
          Download
        </a>
      </nav>
    </header>
  );
}

function Hero() {
  return (
    <section className="hero" id="top" aria-labelledby="hero-title">
      <div className="hero-copy">
        <h1 id="hero-title">Hephaion</h1>
        <p>
          A local document harness for accurate, cited answers. Build an armory
          from your files, ask questions, and inspect the evidence path.
        </p>
        <div className="hero-actions" aria-label="Primary actions">
          <a className="button primary" href="#install">
            Install Heph locally
          </a>
          <a className="button secondary" href="#cli">
            Try the terminal
          </a>
        </div>
      </div>
      <HephTerminalDemo />
    </section>
  );
}

function HephTerminalDemo() {
  const [activePanel, setActivePanel] = useState("home");
  const [bridgeState, setBridgeState] = useState("checking");
  const [input, setInput] = useState("");
  const [materials, setMaterials] = useState(DEFAULT_MATERIALS);
  const [messages, setMessages] = useState(INITIAL_TRANSCRIPT);
  const [model, setModel] = useState(MODEL_CHOICES[0]);
  const [reasoning, setReasoning] = useState(REASONING_LEVELS[0]);
  const [evidence, setEvidence] = useState([]);
  const [busy, setBusy] = useState(false);
  const promptAbortRef = useRef(null);
  const demoTimeoutRef = useRef(null);

  const enabledMaterials = useMemo(
    () => materials.filter((material) => material.enabled),
    [materials],
  );

  const statusText = useMemo(
    () =>
      `Heph  ARMORY exams  MODEL ${model}  REASONING ${reasoning}`,
    [model, reasoning],
  );

  const bridgeLabel = useMemo(() => {
    if (bridgeState === "online") {
      return "BRIDGE sdk";
    }

    if (bridgeState === "checking") {
      return "BRIDGE checking";
    }

    return "BRIDGE demo";
  }, [bridgeState]);

  useEffect(() => {
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 900);

    probeHephBridge({ signal: controller.signal })
      .then(() => setBridgeState("online"))
      .catch(() => setBridgeState("demo"))
      .finally(() => window.clearTimeout(timeout));

    return () => {
      window.clearTimeout(timeout);
      controller.abort();
    };
  }, []);

  useEffect(
    () => () => {
      promptAbortRef.current?.abort();
      if (demoTimeoutRef.current) {
        window.clearTimeout(demoTimeoutRef.current);
      }
    },
    [],
  );

  const appendAssistantDelta = useCallback((delta) => {
    setMessages((current) =>
      current.map((message, index) => {
        if (index !== current.length - 1 || message.role !== "assistant") {
          return message;
        }

        return {
          ...message,
          text: `${message.text}${delta}`,
        };
      }),
    );
  }, []);

  const finishAssistantMessage = useCallback((text) => {
    setMessages((current) =>
      current.map((message, index) => {
        if (index !== current.length - 1 || message.role !== "assistant") {
          return message;
        }

        return {
          ...message,
          text,
          streaming: false,
        };
      }),
    );
  }, []);

  const runDemoPrompt = useCallback(
    (text) => {
      const sourceList = enabledMaterials
        .slice(0, 2)
        .map((material, index) => `E${index + 1} ${material.path}#chunk=${index}`)
        .join("  ");
      const answer =
        sourceList.length > 0
          ? `Heph would retrieve from the enabled materials before answering "${text}". The answer stays tied to ${sourceList}.`
          : "No searchable materials are enabled. Open materials and choose what retrieval can see.";

      const nextEvidence = enabledMaterials.slice(0, 2).map((material, index) => ({
        id: `E${index + 1}`,
        path: `${material.path}#chunk=${index}`,
      }));
      const citation = nextEvidence.length > 0 ? " [E1]" : "";

      setEvidence(nextEvidence);
      finishAssistantMessage(`${answer}${citation}`);
    },
    [enabledMaterials, finishAssistantMessage],
  );

  const handleBridgeMessage = useCallback(
    (message) => {
      if (message.type === "stream_event" && message.event?.type === "assistant_delta") {
        appendAssistantDelta(message.event.delta || "");
      }

      if (message.type === "stream_event" && message.event?.type === "notice") {
        appendAssistantDelta(`\n${message.event.message || ""}`);
      }

      if (message.type === "stream_end" && message.ok === false) {
        appendAssistantDelta("\nThe SDK stream ended with an error. Check provider setup.");
      }

      if (message.type === "stream_end" && message.ok !== false) {
        setEvidence([{ id: "E1", path: "last-turn evidence from the active SDK session" }]);
      }
    },
    [appendAssistantDelta],
  );

  const submitPrompt = useCallback(
    async (event) => {
      event.preventDefault();
      const text = input.trim();

      if (!text || busy) {
        return;
      }

      setInput("");
      setBusy(true);
      setActivePanel("home");
      setEvidence([]);
      setMessages((current) => [
        ...current,
        { id: crypto.randomUUID(), role: "user", text },
        { id: crypto.randomUUID(), role: "assistant", text: "", streaming: true },
      ]);

      const controller = new AbortController();
      promptAbortRef.current = controller;

      if (bridgeState === "online") {
        try {
          await streamPromptThroughBridge(text, {
            onMessage: handleBridgeMessage,
            signal: controller.signal,
          });
        } catch (error) {
          if (controller.signal.aborted || error?.name === "AbortError") {
            finishAssistantMessage("Stopped before Heph answered.");
          } else {
            setBridgeState("demo");
            runDemoPrompt(text);
          }
        } finally {
          promptAbortRef.current = null;
          setBusy(false);
        }
        return;
      }

      demoTimeoutRef.current = window.setTimeout(() => {
        if (controller.signal.aborted) {
          return;
        }

        runDemoPrompt(text);
        promptAbortRef.current = null;
        demoTimeoutRef.current = null;
        setBusy(false);
      }, 180);
    },
    [bridgeState, busy, finishAssistantMessage, handleBridgeMessage, input, runDemoPrompt],
  );

  const stopPrompt = useCallback(() => {
    promptAbortRef.current?.abort();
    promptAbortRef.current = null;
    if (demoTimeoutRef.current) {
      window.clearTimeout(demoTimeoutRef.current);
      demoTimeoutRef.current = null;
    }
    setBusy(false);
    finishAssistantMessage("Stopped before Heph answered.");
  }, [finishAssistantMessage]);

  const toggleMaterial = useCallback((path) => {
    setMaterials((current) =>
      current.map((material) =>
        material.path === path ? { ...material, enabled: !material.enabled } : material,
      ),
    );
  }, []);

  const cycleReasoning = useCallback(() => {
    setReasoning((current) => {
      const index = REASONING_LEVELS.indexOf(current);
      return REASONING_LEVELS[(index + 1) % REASONING_LEVELS.length];
    });
    setMessages((current) => [
      ...current.filter((message) => message.id !== "reasoning-notice"),
      {
        id: "reasoning-notice",
        role: "notice",
        lines: [`Reasoning ${REASONING_LEVELS[(REASONING_LEVELS.indexOf(reasoning) + 1) % REASONING_LEVELS.length]}.`],
      },
    ]);
  }, [reasoning]);

  return (
    <section className="heph-cli" id="cli" aria-label="Interactive Heph terminal">
      <div className="cli-status" aria-label="Heph session status">
        <span>{statusText}</span>
        <span>{bridgeLabel}</span>
      </div>
      <div className="cli-body">
        <div className="cli-main">
          <CliTranscript
            activePanel={activePanel}
            evidence={evidence}
            materials={materials}
            messages={messages}
            model={model}
            onChooseModel={setModel}
            onSetPanel={setActivePanel}
            onToggleMaterial={toggleMaterial}
          />
          <form className="cli-composer" onSubmit={submitPrompt}>
            <span aria-hidden="true">-&gt;</span>
            <label className="sr-only" htmlFor="heph-prompt">
              Ask Heph
            </label>
            <input
              id="heph-prompt"
              value={input}
              onChange={(event) => setInput(event.target.value)}
              placeholder="Ask a cited question about your materials..."
              disabled={busy}
            />
            {busy ? (
              <button type="button" onClick={stopPrompt}>
                stop
              </button>
            ) : (
              <button type="submit">send</button>
            )}
          </form>
          <div className="cli-footer" aria-label="Heph shortcuts">
            <CliFooterButton label="ARMORY" keys="ctrl+a" onClick={() => setActivePanel("armory")} />
            <CliFooterButton
              label="MATERIALS"
              keys="ctrl+o"
              onClick={() => setActivePanel("materials")}
            />
            <CliFooterButton
              label="COMMANDS"
              keys="ctrl+p"
              onClick={() => setActivePanel("commands")}
            />
            <CliFooterButton label="REASONING" keys="shift+tab" onClick={cycleReasoning} />
          </div>
        </div>
        <CliInfoPanel
          bridgeLabel={bridgeLabel}
          enabledMaterials={enabledMaterials}
          evidence={evidence}
          materials={materials}
          model={model}
        />
      </div>
    </section>
  );
}

function CliTranscript({
  activePanel,
  evidence,
  materials,
  messages,
  model,
  onChooseModel,
  onSetPanel,
  onToggleMaterial,
}) {
  if (activePanel === "materials") {
    return <MaterialsPanel materials={materials} onToggleMaterial={onToggleMaterial} />;
  }

  if (activePanel === "armory") {
    return <ArmoryPanel onSetPanel={onSetPanel} />;
  }

  if (activePanel === "commands") {
    return <CommandsPanel onSetPanel={onSetPanel} />;
  }

  if (activePanel === "evidence") {
    return <EvidencePanel evidence={evidence} />;
  }

  if (activePanel === "models") {
    return <ModelsPanel model={model} onChooseModel={onChooseModel} />;
  }

  return (
    <div className="cli-transcript" aria-live="polite">
      {messages.map((message) => (
        <CliMessage key={message.id} message={message} />
      ))}
    </div>
  );
}

function CliMessage({ message }) {
  if (message.role === "notice") {
    return (
      <div className="cli-notice">
        {message.lines.map((line) => (
          <div key={line}>{line}</div>
        ))}
      </div>
    );
  }

  return (
    <div className={`cli-message ${message.role}`}>
      <span>{message.text || (message.streaming ? "thinking..." : "")}</span>
    </div>
  );
}

function MaterialsPanel({ materials, onToggleMaterial }) {
  return (
    <div className="cli-panel">
      <p>SCOPE materials</p>
      {materials.map((material) => (
        <button
          className="cli-row"
          type="button"
          key={material.path}
          onClick={() => onToggleMaterial(material.path)}
        >
          <span>{material.enabled ? "@" : "-"}</span>
          <span>{material.path}</span>
          <span>{material.enabled ? "enabled" : "off"}</span>
        </button>
      ))}
    </div>
  );
}

function ArmoryPanel({ onSetPanel }) {
  return (
    <div className="cli-panel">
      <p>ITEMS 3</p>
      <button className="cli-row selected" type="button" onClick={() => onSetPanel("home")}>
        <span>-&gt;</span>
        <span>exams</span>
        <span>state current</span>
      </button>
      <button className="cli-row" type="button" onClick={() => onSetPanel("home")}>
        <span> </span>
        <span>research</span>
        <span>files 9</span>
      </button>
      <button className="cli-row" type="button" onClick={() => onSetPanel("home")}>
        <span> </span>
        <span>contracts</span>
        <span>files 12</span>
      </button>
    </div>
  );
}

function CommandsPanel({ onSetPanel }) {
  return (
    <div className="cli-panel two-column">
      <button type="button" onClick={() => onSetPanel("materials")}>
        <code>/materials</code>
        <span>choose what retrieval can see</span>
      </button>
      <button type="button" onClick={() => onSetPanel("evidence")}>
        <code>/evidence</code>
        <span>inspect the last turn sources</span>
      </button>
      <button type="button" onClick={() => onSetPanel("models")}>
        <code>/models</code>
        <span>switch reachable model choices</span>
      </button>
      <button type="button" onClick={() => onSetPanel("home")}>
        <code>/turn</code>
        <span>review the answer path</span>
      </button>
    </div>
  );
}

function EvidencePanel({ evidence }) {
  if (evidence.length === 0) {
    return (
      <div className="cli-panel">
        <p>EVIDENCE none yet</p>
        <p>Ask a question after enabling materials.</p>
      </div>
    );
  }

  return (
    <div className="cli-panel">
      <p>EVIDENCE {evidence.map((item) => item.id).join(" ")}</p>
      {evidence.map((item) => (
        <div className="cli-evidence-line" key={item.id}>
          <span>{item.id}</span>
          <span>{item.path}</span>
        </div>
      ))}
      <p>OPEN /evidence or /turn</p>
    </div>
  );
}

function ModelsPanel({ model, onChooseModel }) {
  return (
    <div className="cli-panel">
      <p>MODEL choices</p>
      {MODEL_CHOICES.map((choice) => (
        <button
          className={`cli-row ${choice === model ? "selected" : ""}`}
          type="button"
          key={choice}
          onClick={() => onChooseModel(choice)}
        >
          <span>{choice === model ? "-&gt;" : " "}</span>
          <span>{choice}</span>
          <span>{choice === model ? "current" : "available"}</span>
        </button>
      ))}
    </div>
  );
}

function CliFooterButton({ label, keys, onClick }) {
  return (
    <button type="button" onClick={onClick}>
      <span>{label}</span>
      <span>{keys}</span>
    </button>
  );
}

function CliInfoPanel({ bridgeLabel, enabledMaterials, evidence, materials, model }) {
  return (
    <aside className="cli-info" aria-label="Heph session details">
      <p>
        <span>SCOPE</span>
        <span>
          {enabledMaterials.length}/{materials.length}
        </span>
      </p>
      <p>
        <span>STATE</span>
        <span>{enabledMaterials.length > 0 ? "current" : "no materials"}</span>
      </p>
      <p>
        <span>EVIDENCE</span>
        <span>{evidence.length > 0 ? evidence.map((item) => item.id).join(" ") : "none yet"}</span>
      </p>
      <p>
        <span>MODEL</span>
        <span>{model}</span>
      </p>
      <p>
        <span>{bridgeLabel.split(" ")[0]}</span>
        <span>{bridgeLabel.split(" ")[1]}</span>
      </p>
      {enabledMaterials.slice(0, 3).map((material) => (
        <p className="cli-material-token" key={material.path}>
          <span>@</span>
          <span>{material.path}</span>
        </p>
      ))}
    </aside>
  );
}

function InstallSection() {
  return (
    <section className="section install-section" id="install" aria-labelledby="install-title">
      <div className="section-copy">
        <h2 id="install-title">Install Heph locally.</h2>
        <p>
          Use <code>uv tool</code> for the public command, then open Heph and
          check the installed version.
        </p>
      </div>
      <CommandBlock command={INSTALL_SCRIPT} feedbackId="install-copy-feedback" />
      <p className="secondary-install">
        Prefer pip for this Python environment? <code>{SECONDARY_INSTALL}</code>
      </p>
    </section>
  );
}

function CommandBlock({ command, feedbackId }) {
  const [feedback, setFeedback] = useState("ready to copy");

  const copyCommand = useCallback(async () => {
    if (!navigator.clipboard?.writeText) {
      setFeedback("copy unavailable");
      return;
    }

    try {
      await navigator.clipboard.writeText(command);
      setFeedback("copied");
    } catch {
      setFeedback("copy failed");
    }
  }, [command]);

  return (
    <div className="command-block">
      <pre aria-label="Install script">
        <code>{command}</code>
      </pre>
      <div className="command-actions">
        <button className="button secondary" type="button" onClick={copyCommand}>
          Copy script
        </button>
        <span id={feedbackId} aria-live="polite">
          {feedback}
        </span>
      </div>
    </div>
  );
}

function WorkflowSection() {
  return (
    <section className="section workflow-section" id="workflow" aria-labelledby="workflow-title">
      <div className="section-copy">
        <h2 id="workflow-title">A harness around your documents, not a hosted workspace.</h2>
        <p>
          Hephaion provides the guardrails around Heph: retrieval, citation
          checks, scoped memory, and model boundaries.
        </p>
      </div>
      <div className="workflow-grid">
        {WORKFLOW_STEPS.map((step) => (
          <article className="feature-card" key={step.title}>
            <h3>{step.title}</h3>
            <p>{step.text}</p>
          </article>
        ))}
      </div>
    </section>
  );
}

function SdkSection() {
  const [allowedOrigin, setAllowedOrigin] = useState(DEFAULT_SITE_ORIGIN);

  useEffect(() => {
    if (window.location.protocol === "http:" || window.location.protocol === "https:") {
      setAllowedOrigin(window.location.origin);
    }
  }, []);

  const bridgeCommand = useMemo(
    () =>
      `npm run heph:sdk-bridge -- --armory ~/.armories/exams --allow-origin ${allowedOrigin}\n# then refresh this page and ask in the terminal`,
    [allowedOrigin],
  );

  return (
    <section className="section sdk-section" id="sdk" aria-labelledby="sdk-title">
      <div className="section-copy">
        <h2 id="sdk-title">Use the SDK when the interface is yours.</h2>
        <p>
          Heph exposes a JSONL service for native apps, GUI shells, automation,
          and local web experiments. The terminal above looks for a local bridge
          at <code>127.0.0.1:8766</code> and falls back to the in-browser demo
          when the bridge is not running.
        </p>
      </div>
      <div className="sdk-grid">
        <CommandBlock
          command={bridgeCommand}
          feedbackId="bridge-copy-feedback"
        />
        <div className="sdk-notes">
          <p>
            The bridge starts <code>heph sdk serve</code>, forwards prompts, and
            streams JSONL events into the browser surface.
          </p>
          <p>
            Deployed Vercel pages remain static. Your local armory stays on your
            machine.
          </p>
        </div>
      </div>
    </section>
  );
}

function PrivacySection() {
  return (
    <section className="section privacy-section" id="privacy" aria-labelledby="privacy-title">
      <div className="section-copy">
        <h2 id="privacy-title">Private by default, explicit when it talks to a model.</h2>
        <p>
          Documents, chat history, retrieval indexes, traces, and local memory
          live in the armory. When you use a hosted model, Heph sends the
          question, relevant chunks, and prompt context to the configured
          provider.
        </p>
      </div>
      <div className="provider-table" role="table" aria-label="Supported model access">
        <div role="row" className="provider-row provider-head">
          <span role="columnheader">Provider</span>
          <span role="columnheader">Access</span>
          <span role="columnheader">Use</span>
        </div>
        {PROVIDERS.map(([provider, access, use]) => (
          <div role="row" className="provider-row" key={provider}>
            <span role="cell">{provider}</span>
            <span role="cell">{access}</span>
            <span role="cell">{use}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

function FinalCta() {
  return (
    <section className="section final-cta" aria-labelledby="final-title">
      <div>
        <h2 id="final-title">Start with one armory.</h2>
        <p>
          Install Heph, add files to <code>materials/</code>, and ask for an
          answer you can trace.
        </p>
      </div>
      <a className="button primary" href="#install">
        Get the install script
      </a>
    </section>
  );
}

function Footer() {
  return (
    <footer className="site-footer">
      <p>Heph is the public command for the Hephaion local document harness.</p>
      <a href="#top">Back to top</a>
    </footer>
  );
}

export default App;
