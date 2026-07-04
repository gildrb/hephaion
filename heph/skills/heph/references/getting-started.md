# Getting Started With Heph

## Install

Heph requires Python 3.13+.

Recommended install:

```bash
uv tool install heph@latest
heph --version
```

Source install for development:

```bash
uv sync --frozen --group dev
uv run heph
```

Run source commands from the Heph repository root.

## Create An Armory

```bash
heph armory init <name>
cp <file> ~/.armories/<name>/materials/
heph <name>
```

A new armory can open before documents are added. Heph should show a no-materials state until files are present in `materials/`.

## Configure A Model

Inside Heph, use:

```text
/login
/models
```

Provider setup can use `/login`, saved settings, a custom endpoint, local model setup, or supported environment variables. Check current Heph docs and CLI help for provider-specific keys.

## Ask Questions

Ask questions about the materials in the active armory. Heph retrieves relevant passages, generates an answer, shows citations, and saves armory-scoped memory.

Use `/evidence` to inspect what was retrieved for the last answer.

## First Checks When Setup Fails

1. Confirm the armory path and `materials/` folder.
2. Run `heph index <path>`.
3. Run `heph health <path>`.
4. Use `/login` or configured provider credentials.
5. Use `/models` to pick a reachable model.
6. Use `/trust` or `heph trust <path>` to inspect ownership and data flow.
