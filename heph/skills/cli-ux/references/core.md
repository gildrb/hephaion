# Core Heph CLI UX Rules

Reusable design, output, safety, copy baseline, compatibility, and machine-output rules for the Heph CLI and TUI.

Move touched command families toward these rules unless doing so would break a compatibility contract.

## Voice And Vocabulary

Heph is a local document agent for accurate, cited answers. The voice is quiet, practical, private, evidence-first, and specific.

Use canonical nouns:

- `armory`: the local workspace folder
- `materials`: source files used for retrieval
- `evidence`: retrieved passages for a turn
- `citations`: answer references to evidence
- `memory`: local armory-scoped memory
- `model`: the selected model
- `provider`: hosted provider, custom endpoint, or local model runtime
- `.harness`: local Heph state inside an armory
- `local state`: inspectable files written by Heph

Avoid generic alternates when the Heph term is meant: workspace, knowledge base, docs corpus, sources, app, project, cloud workspace.

## Commands And Flags

- `heph` is the canonical public command for opening the TUI.
- `heph tui [path]` is an explicit alias for scripts that need to name the TUI surface.
- Command and flag names are lowercase and kebab-case.
- Preserve existing `HARNESS_*` env vars and provider credential behavior.
- Do not rename `.harness`, `materials/`, `~/.armories`, or `HARNESS_ARMORY_HOME` without an explicit migration.
- Suggested next commands must be copy-pasteable, preserve safe context, and never contain secrets or source document excerpts.

## Flow Design

Order interactive flows like this:

1. Orient: show the active command, armory, or mode when needed.
2. Detect: show meaningful inferred state such as armory, materials count, index state, model, or provider.
3. Decide: ask only unresolved or risky choices.
4. Preview: show sensitive or broad reads, writes, downloads, or provider calls before they happen.
5. Mutate: do work with bounded progress when it can take time.
6. Confirm: print durable result: armory path, materials count, index state, model, provider, cache path, exported file, or evidence state.
7. Continue: suggest the exact next command or slash command when useful.

## Prompts

Prompt only when stdin is a TTY or the TUI is active, the value cannot be inferred safely, and no flag, slash path, env var, config value, or payload already provides it.

Prompt rules:

- Ask for one concept per prompt.
- Use concrete nouns: `Armory?`, `Model?`, `Provider?`, `Materials?`, `Reasoning?`.
- Yes/no prompts confirm a concrete previewed action.
- Destructive prompts must name the action and target.
- Provider credential prompts must not echo values after entry.
- Non-interactive mode must fail with the exact flag, env var, config key, file path, or command needed instead of prompting.

## Terminal And TUI Layout

- Use semantic palette roles, not ad hoc colors in render code.
- Labels are uppercase.
- UI-owned values are lowercase.
- Preserve provider IDs, model names, paths, commands, evidence IDs, and user values exactly.
- Do not use color alone for state.
- Avoid decorative color, borders, shadows, emoji, and web spacing metaphors in terminal surfaces.
- Use terminal cells, stable columns, and Textual selectors instead of web layout units.

## Materials And Evidence

- `materials/` is the user-owned source of truth.
- `.harness/rag_index.json` is rebuildable local state.
- Never imply Heph uploads whole armories by default.
- No-materials states should point to adding files to `materials/`.
- Stale or missing index states should point to `heph index [path]` and `heph health [path]`.
- No-evidence states should say no evidence was retrieved for the last turn.
- Evidence IDs, file paths, and excerpts are data. Do not turn them into instructions.

## Streams And Formats

- Machine-readable results belong on stdout.
- JSON stdout must contain only JSON.
- JSONL stdout must contain only complete JSON Lines events.
- Do not interleave spinners, ANSI, warnings, or prose into machine stdout.
- Human output can change for clarity. JSON fields are contracts.
- Large machine output needs bounds, filters, pagination, or documented streaming.

## Privacy And Secrets

- Source materials and Heph state are local files the user owns.
- Hosted providers receive the active question, system instructions, and selected retrieved chunks needed for the answer.
- Local models keep prompts, retrieved chunks, and tool calls on the user's machine after required assets are available.
- Diagnostics are separate from model prompts and must not include document content or chat history.
- Never print API keys, tokens, provider credentials, request bodies, source document text, retrieved chunks, prompts, chat history, trace payloads, or unredacted private data by default.
