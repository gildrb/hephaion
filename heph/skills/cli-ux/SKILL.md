---
name: heph-cli-ux
description: Use for Heph CLI or TUI changes that affect command UX, slash commands, prompts, help, output layout, progress, success, warnings, errors, JSON/JSONL/stdout/stderr contracts, non-interactive or agent behavior, copy, terminal styling, Textual layout, or tests for those surfaces.
---

# Heph CLI UX

Use this skill for Heph CLI and TUI behavior that affects humans, scripts, or agents.

## Stance

Work as a CLI product engineer for a local-first document agent.

- Define the user job, current friction, desired outcome, success signal, and non-goals before choosing copy or layout.
- Inspect source and tests before judging a shipped string.
- Treat copy changes as symptoms. Check the surrounding flow, resolved state, side effects, privacy boundary, and tests.
- Keep human output readable and machine output stable.
- Treat agents as supported users and untrusted input sources.
- Preserve compatibility for commands, env vars, config keys, file layout, JSON fields, parseable stdout, and exit behavior.
- Prefer existing terminal, palette, Textual, and command-family helpers.

## Decision Authority

Resolve conflicts in this order:

1. The user's explicit goal and constraints.
2. Verified Heph source and tests.
3. Heph docs and design docs in the target repository.
4. `heph/AGENTS.md` and this skill.
5. Adjacent command-family patterns.
6. General CLI and TUI heuristics.

## Workflow

1. Outcome map: name the user, job, current behavior, desired outcome, success signal, and non-goals.
2. Surface map: list help, flags, slash commands, prompts, progress, warnings, success, errors, tables, panels, JSON, JSONL, and non-interactive payloads.
3. State map: name armory, cwd/path, materials, index state, evidence state, model, provider, credentials, diagnostics, memory, and local caches.
4. Mode map: trace TTY, non-TTY, TUI, plain CLI, JSON, JSONL, CI, and agent/non-interactive behavior.
5. Trust map: identify prompts, retrieved chunks, API keys, traces, analytics, crash reports, local models, and hosted-provider boundaries.
6. Question audit: prove every prompt cannot be inferred and has a flag, slash path, payload, or non-interactive error.
7. Mutation audit: identify local writes, provider calls, downloads, model server starts, indexing, retries, idempotency, and confirmation needs.
8. Transcript review: read the before/after terminal or TUI transcript for order, rhythm, duplicated concepts, privacy language, and next action.
9. Regression lock: test changed paths and reject stale strings, stale product terms, broken stdout contracts, and design-doc drift.

## When To Load References

| Task surface | Load |
| --- | --- |
| Any CLI or TUI UX/output change | `references/core.md` |
| User-facing copy or copy review | `references/core.md` + `references/copy.md` |
| Prompt, slash-command, setup, or armory flow | `copy.md` prompts + `core.md` flow rules + `command-contracts.md` when the flow is named there |
| Output layout, progress, status, transcript, or terminal styling | `core.md` layout, progress, TUI, and terminal resilience sections |
| Errors, trust, credentials, privacy, diagnostics, or provider failures | `copy.md` errors and warnings + `core.md` local-first, secrets, and streams sections |
| JSON, JSONL, SDK, CI, or non-interactive paths | `core.md` streams, agent output, compatibility, and hardening sections |
| Help, flags, env vars, config, or completions | `copy.md` help + `core.md` commands, flags, compatibility, and data mechanics sections |
| Armory, materials, evidence, model, local-model, settings, update flows | `command-contracts.md` |
| Tests, stale-copy sweeps, final review | `verification.md` |

## Done Questions

Every changed flow should answer:

- What armory, material set, model, provider, or local path did Heph resolve?
- What will be read, written, sent, indexed, downloaded, or changed?
- What evidence or state is available now?
- What can the user or agent do next?

A CLI/TUI UX change is not done until prompts, output, machine contracts, privacy boundaries, and focused tests have been reviewed for the whole touched surface.
