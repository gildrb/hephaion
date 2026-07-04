# Getting Started

## Install

Requires Python 3.13+.

```bash
uv tool install heph@latest
heph --version
```

Development install:

```bash
uv sync --frozen --group dev
uv run heph
```

Run source commands from the repository root.

## Create Armory

```bash
heph armory init <name>
cp <file> ~/.armories/<name>/materials/
heph <name>
```

A new armory can open before documents are added. Show a no-materials state until files exist in `materials/`.

## Configure Model

Inside the app:

```text
/login
/models
```

Provider setup can use `/login`, saved settings, a custom endpoint, local model setup, or supported env vars. Check current docs and CLI help for provider-specific keys.

## Ask

Ask questions about active armory materials. The app retrieves passages, answers, shows citations, and saves armory-scoped memory.

Use `/evidence` to inspect last-answer retrieval.

## Setup Fails

1. Confirm armory path and `materials/`.
2. Run `heph index <path>`.
3. Run `heph health <path>`.
4. Use `/login` or configured credentials.
5. Use `/models` to pick a reachable model.
6. Use `/trust` or `heph trust <path>` to inspect ownership and data flow.
