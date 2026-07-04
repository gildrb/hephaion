---
name: heph-cli-ux
description: Use for CLI/TUI changes that affect command UX, slash commands, prompts, help, output, progress, errors, JSON/JSONL, stdout/stderr, agent behavior, copy, terminal styling, Textual layout, or tests.
---

# CLI UX

Use this skill for CLI/TUI behavior that affects humans, scripts, or agents.

## Stance

Work as a CLI product engineer for a local-first document agent.

- Define user job, friction, outcome, success signal, and non-goals before choosing copy or layout.
- Inspect source and tests before judging a shipped string.
- Treat copy changes as symptoms. Check flow, state, side effects, privacy boundary, and tests.
- Keep human output readable and machine output stable.
- Treat agents as supported users and untrusted input sources.
- Preserve commands, env vars, config keys, file layout, JSON fields, parseable stdout, and exit behavior.
- Prefer existing terminal, palette, Textual, and command-family helpers.

## Authority

1. User goal and constraints.
2. Verified source and tests.
3. Product docs and design docs.
4. `AGENTS.md` and this skill.
5. Adjacent command patterns.
6. General CLI/TUI heuristics.

## Workflow

1. Outcome: user, job, current behavior, desired outcome, success signal, non-goals.
2. Surface: help, flags, slash commands, prompts, progress, warnings, success, errors, tables, panels, JSON, JSONL, non-interactive payloads.
3. State: armory, cwd/path, materials, index, evidence, model, provider, credentials, diagnostics, memory, caches.
4. Mode: TTY, non-TTY, TUI, plain CLI, JSON, JSONL, CI, agent/non-interactive.
5. Trust: prompts, retrieved chunks, API keys, traces, analytics, crash reports, local models, hosted providers.
6. Prompt audit: prove every prompt cannot be inferred and has a flag, slash path, payload, or non-interactive error.
7. Mutation audit: local writes, provider calls, downloads, model server starts, indexing, retries, idempotency, confirmations.
8. Transcript review: order, rhythm, duplicated concepts, privacy language, next action.
9. Regression lock: test changed paths; reject stale strings, stale terms, broken stdout contracts, design-doc drift.

## References

| Task | Load |
| --- | --- |
| CLI/TUI UX or output | `references/core.md` |
| Copy | `references/core.md` + `references/copy.md` |
| Prompts, slash commands, setup, armory flow | `copy.md` + `core.md` + `command-contracts.md` when named there |
| Layout, progress, status, transcript, styling | `core.md` |
| Errors, trust, credentials, privacy, diagnostics, provider failures | `copy.md` + `core.md` |
| JSON, JSONL, SDK, CI, non-interactive paths | `core.md` |
| Help, flags, env vars, config, completions | `copy.md` + `core.md` |
| Armory, materials, evidence, model, local model, settings, update flows | `command-contracts.md` |
| Tests, stale-copy sweeps, final review | `verification.md` |

## Done Questions

- What armory, materials, model, provider, or path was resolved?
- What will be read, written, sent, indexed, downloaded, or changed?
- What evidence or state is available now?
- What can the user or agent do next?

A CLI/TUI UX change is not done until prompts, output, machine contracts, privacy boundaries, and focused tests cover the touched surface.
