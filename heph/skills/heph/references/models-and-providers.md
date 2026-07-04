# Models

Armories are separate from compute. Model and provider can change without changing materials.

## Provider Types

Supported providers may include hosted providers, custom endpoints, and local models. Verify current support in source, docs, or command help before adding provider-specific guidance.

## Trust Boundary

- Local models keep prompts, retrieved chunks, and tool calls on the user's machine after required assets are available.
- Hosted providers receive active question, system instructions, and selected retrieved chunks.
- Custom endpoints receive the same request shape at the configured endpoint.
- Diagnostics are separate from model prompts.

## Configure

```text
/login
/models
/local
/settings
```

Generic env vars:

```bash
HARNESS_API_KEY=<api-key>
HARNESS_BASE_URL=<url>
HARNESS_MODEL=<provider-model-name>
```

Provider-specific keys may exist. Check current docs before naming them.

## Local Models

```bash
heph local search [query]
heph local install <repo-or-path>
heph local status
heph local revalidate <model-id>
heph local stop
```

Rules:

- Install should show download size and recommended RAM.
- Cache path must be documented.
- Models are usable only after validation passes.
- Failed models can remain downloaded and be revalidated.

## Troubleshoot

Missing model:

1. Check credentials.
2. Use `/login`.
3. Use `/models`.
4. For local models, run `heph local status`.
5. Revalidate with `heph local revalidate <model-id>`.

Slow responses:

1. Check provider or network state.
2. Try a smaller or faster model.
3. For local models, check memory pressure.
4. Use `/evidence` before repeating expensive questions.
