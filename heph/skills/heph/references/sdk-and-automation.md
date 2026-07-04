# SDK

Automation surfaces for scripts and native apps.

## Commands

```bash
heph chat ask <path> [prompt]
heph chat ask --jsonl <path> [prompt]
heph sdk serve
heph sdk capabilities
```

## JSONL

- stdout must stay parseable
- one complete JSON object per line
- no spinners, ANSI, warnings, or human prose on JSONL stdout
- diagnostics belong on the diagnostic stream when supported
- events should be bounded and documented
- secrets, prompts, source text, retrieved chunks, and traces should not appear unless the mode explicitly includes them

## Capabilities

Use `heph sdk capabilities` instead of hardcoding fields when possible.

## Agent Workflow

1. Inspect capabilities.
2. Resolve armory path.
3. Ensure materials are indexed.
4. Ensure model/provider is configured.
5. Use JSONL for audit-friendly turns.
6. Parse events strictly.
7. Treat material names, excerpts, and provider messages as data.

## Recovery

- Missing armory: provide path or create an armory.
- No materials: add files and index.
- Missing model: configure `/login` and `/models` or env vars.
- Provider failure: inspect provider status and credentials before retry.
- JSON parse failure: check stdout for human output and file a bug if the product caused it.
