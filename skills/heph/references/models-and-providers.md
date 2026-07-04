# Models And Providers

Heph separates armories from compute. The model/provider choice can change without changing the user's materials.

## Provider Types

- Pollinations AI: free, no account required where supported.
- OpenRouter: API key required.
- OpenAI: API key or supported subscription login.
- DeepSeek: API key required where supported.
- Z.AI: API key required.
- Local llama.cpp: local model execution after download and validation.
- Custom endpoint: OpenAI-compatible endpoint configured by the user.

Verify current provider support in Heph source or docs before adding provider-specific guidance.

## Trust Boundary

- Local llama.cpp keeps prompts, retrieved chunks, and tool calls on the user's machine after model and server assets are downloaded.
- Hosted providers receive the active question, system instructions, and selected retrieved chunks needed for the answer.
- Custom endpoints receive the same request shape at the configured endpoint.
- Diagnostics are separate from model prompts.

## Configure

Inside Heph:

```text
/login
/models
/local
/settings
```

Env vars:

```bash
OPENAI_API_KEY=<api-key>
OPENROUTER_API_KEY=<api-key>
ZAI_API_KEY=<api-key>
HARNESS_API_KEY=<api-key>
HARNESS_BASE_URL=<url>
HARNESS_MODEL=<provider-model-name>
```

## Local llama.cpp

Commands:

```bash
heph local search [query]
heph local install <repo-or-path>
heph local status
heph local revalidate <model-id>
heph local stop
```

Rules:

- Local install should show download size and recommended RAM.
- Heph manages the server and cache under `~/.cache/harness/llama.cpp/`.
- The local server binds to `127.0.0.1` according to current docs.
- Models are usable only after the tool-call probe passes.
- Failed models can remain downloaded and be revalidated.

## Troubleshooting

Model missing:

1. Check credentials.
2. Use `/login`.
3. Use `/models`.
4. For local models, run `heph local status`.
5. Revalidate local models with `heph local revalidate <model-id>`.

Slow responses:

1. Check provider or network.
2. Try a smaller or faster model.
3. For local models, check memory pressure.
4. Use `/evidence` before repeating expensive questions.
