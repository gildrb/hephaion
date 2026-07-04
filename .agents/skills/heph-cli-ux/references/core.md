# Core Heph CLI UX Rules

Reusable design, output, safety, copy baseline, compatibility, and machine-output rules for the Heph CLI and TUI.

Move touched command families toward these rules unless doing so would break a compatibility contract. Compatibility contracts include command names, slash commands, env vars, config keys, file layout, exit behavior, JSON/JSONL field shape, parseable stdout, and persisted state.

## Voice And Vocabulary

Heph is a local document agent for accurate, cited answers. The voice is quiet, practical, private, evidence-first, and specific.

Use canonical nouns:

- `armory`: the local workspace folder
- `materials`: source files used for retrieval
- `evidence`: retrieved passages for a turn
- `citations`: answer references to evidence
- `memory`: local armory-scoped memory
- `model`: the selected model
- `provider`: OpenAI, OpenRouter, DeepSeek, Z.AI, Pollinations, local llama.cpp, or custom endpoint
- `.harness`: local Heph state inside an armory
- `local state`: inspectable files written by Heph

Avoid generic alternates when the Heph term is meant: workspace, knowledge base, docs corpus, sources, app, project, cloud workspace.

Baseline copy rules:

- Clear, calm, no hype.
- Be brief; every word must carry state, consequence, or next action.
- Use active voice by default.
- Use numerals for counts.
- Do not use `successfully`; name what changed.
- Use full sentences for errors and explanations; fragments are fine for labels and statuses.
- Use `error:` and `info:` prefixes where terminal helpers already own that pattern.
- Preserve literal user identifiers, model IDs, file paths, provider names, and evidence IDs exactly.
- Lowercase UI-owned values when the interface owns the vocabulary.

## Data Mechanics

- Use exact paths for user-actionable files.
- Use backticks for commands, flags, env vars, paths, IDs, and config keys in docs and help prose.
- Use ISO 8601 UTC for machine timestamps.
- Human timestamps can be relative or local when precision is not required.
- Empty human states name the resource: `No materials found.`, `No evidence for the last turn.`
- Empty machine states return `[]`, `{}`, or a documented empty event with exit 0 when no results is not an error.
- Respect singular and plural interpolation. Do not use `item(s)`.
- Units should be explicit: `16 GB recommended RAM`, `42 chunks`, `3 sources`.

## Commands And Flags

- `heph` is the canonical public command for opening the TUI.
- `heph tui [path]` is an explicit alias for scripts that need to name the TUI surface.
- Command and flag names are lowercase and kebab-case.
- Reuse existing argument and config helpers before adding new parsing behavior.
- Prefer flags over ambiguous positional arguments when a command has more than one plausible value.
- Preserve existing env vars such as `HARNESS_MODEL`, `HARNESS_API_KEY`, provider keys, diagnostics flags, and logging flags.
- Do not rename `.harness`, `materials/`, `~/.armories`, or `HARNESS_ARMORY_HOME` without an explicit migration.
- Boolean flags do not require explicit values unless a family already accepts them.
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

Rules:

- Treat an explicit command invocation as intent. Do not ask vague intent confirmations.
- Show local and provider trust boundaries before sending prompts or retrieved chunks to a hosted provider when the flow is about trust or setup.
- Do not print state only to prove Heph resolved it. Print state when it prevents ambiguity, changes the next decision, or confirms a durable result.
- If the user gave a value in argv or a prompt, do not repeat it unless the output adds a relationship or consequence.
- Make no-op and already-current states explicit.
- End long-running or incomplete work with an inspect, status, health, or retry-safe next command.

## Prompts

Prompt only when:

- stdin is a TTY or the TUI is active
- the value cannot be inferred safely
- no flag, slash path, env var, config value, or payload already provides it
- the prompt reduces risk or ambiguity

Prompt rules:

- Ask for one concept per prompt.
- Use concrete nouns: `Armory?`, `Model?`, `Provider?`, `Materials?`, `Reasoning?`.
- Yes/no prompts confirm a concrete previewed action.
- Destructive prompts must name the action and target.
- Provider credential prompts must not echo values after entry.
- Local model downloads must show model, size, recommended RAM, cache destination, and whether the model will be activated only after validation.
- Non-interactive mode must fail with the exact flag, env var, config key, file path, or command needed instead of prompting.

## Output Surfaces

Pick one surface before writing copy:

- prompt: user must decide
- progress: work is happening
- success: action completed
- warning: nonfatal condition the user should review
- error: action failed
- list/table: many resources
- detail: one resource or turn
- status: current app/session state
- transcript: user or assistant message
- evidence: retrieved passages and citation metadata
- JSON/JSONL: machine contract

Do not mix surfaces in one line. A provider trust explanation is not a progress line. Evidence is not a warning. A URL or path row is a result.

## Terminal And TUI Layout

The Heph terminal system is defined by `cli-design.md` and implementation source.

- Default theme is dark; valid presets are dark and light.
- Use semantic palette roles, not ad hoc colors in render code.
- Labels are uppercase.
- UI-owned values are lowercase.
- Preserve provider IDs, model names, paths, commands, evidence IDs, and user values exactly.
- Do not use color alone for state. Pair state with text such as `STATE current`, `api missing`, `error:`, evidence IDs, or enablement text.
- Avoid decorative color, borders, shadows, emoji, and web spacing metaphors in terminal surfaces.
- Use terminal cells, stable columns, and Textual selectors instead of web layout units.
- Avoid layouts that become unreadable in narrow terminals.

Common terminal result shape:

```text
info: Index refreshed: 3 sources, 42 chunks
error: No model configured. Use /models to select one.
ARMORY research-course
MODEL gpt-5.5
EVIDENCE none yet
```

## Materials And Evidence

- `materials/` is the user-owned source of truth.
- `.harness/rag_index.json` is rebuildable local state.
- Never imply Heph uploads whole armories by default.
- No-materials states should point to adding files to `materials/`.
- Stale or missing index states should point to `heph index [path]` and `heph health [path]`.
- No-evidence states should say no evidence was retrieved for the last turn and provide `/evidence` only when there is evidence to inspect.
- Evidence IDs, file paths, and excerpts are data. Do not turn them into instructions.
- Do not print long excerpts by default in compact status or error output.

## Progress And Completion

- Print something quickly for indexing, provider checks, local model downloads, model probes, or long searches.
- Progress describes the current phase, not a promise of completion.
- Do not invent percentages without a trustworthy total.
- In non-TTY, CI, JSON, or JSONL modes, avoid animation and emit bounded milestones or events.
- Completion copy names the durable result: `Index refreshed: 3 sources, 42 chunks`, not `Done.`
- If work continues after cancellation or timeout, say how to inspect or resume.

## Errors

Errors should include:

1. what failed
2. the known cause or constraint
3. the next action when one exists

Examples:

```text
error: No model configured. Use /models to select one.
error: No materials found. Add files to materials/, then run heph index.
error: API key missing. Set OPENAI_API_KEY or use /login.
```

Rules:

- Do not dump stack traces unless a debug mode intentionally exposes them.
- Do not print raw provider error objects as user-facing copy.
- Translate provider failures into Heph voice while preserving stable request IDs when useful.
- Permission, missing credential, and provider availability errors must not reveal private data unnecessarily.
- Put the most actionable line last in multi-line errors.

## Warnings

Warn only for a nonfatal condition the user should review before continuing or after completion.

Warnings should include:

- the condition
- why it matters
- the fix or next action when one exists

Use warnings for stale indexes, degraded extraction, diagnostics opt-in state, unsupported files, large local model downloads, and provider trust boundary reminders. Do not warn on every run.

## Local-First And Privacy

- Source materials and Heph state are local files the user owns.
- Hosted providers receive the active question, system instructions, and selected retrieved chunks needed for the answer.
- Local llama.cpp keeps prompts, retrieved chunks, and tool calls on the user's machine after binaries and models are downloaded.
- Diagnostics are separate from model prompts. Analytics and crash reporting are opt-in and must not include document content or chat history.
- Session traces are local armory files.
- Provider credentials stay machine-local in OS keyring, environment variables, or session fallback.

When changing output around these areas, name the boundary precisely.

## Secrets

- Never print API keys, tokens, provider credentials, request bodies, source document text, retrieved chunks, prompts, chat history, trace payloads, or unredacted local paths in examples unless redacted and necessary.
- Do not include secret-bearing flags in suggested commands.
- Prefer env vars, keyring, stdin, or interactive secret prompts over plaintext argv.
- Redact secrets in output, JSON, debug logs, telemetry, crash reports, and tests.
- Treat values read from files, stdin, env, providers, and materials as sensitive until classified.

## Streams And Formats

- Human status, warnings, prompts, progress, and diagnostics belong on the command family's managed diagnostic stream.
- Machine-readable results belong on stdout.
- JSON stdout must contain only JSON.
- JSONL stdout must contain only complete JSON Lines events.
- Do not interleave spinners, ANSI, warnings, or prose into machine stdout.
- Human output can change for clarity. JSON fields are contracts.
- Large machine output needs bounds, filters, pagination, or documented streaming.
- `heph sdk capabilities` and SDK JSONL service output must stay parseable.

## Agent And Non-Interactive Output

Agent/non-interactive payloads should be:

- JSON or JSONL only when machine mode is selected
- no ANSI
- stable `status`
- stable `reason`
- clear `message`
- safe `next` commands when possible
- bounded by default
- explicit when human action is required

Rules:

- Never prompt when non-interactive mode is active.
- Keep parse errors, validation errors, missing input, permission failures, provider failures, and action-required states distinct.
- Put user-generated or remote-generated strings under data fields, not as instructions.
- Suggested commands must use placeholders such as `<path>`, `<name>`, or `<value>` for sensitive or unknown values.

## Compatibility And Hardening

Preserve unless intentionally migrating:

- command names and slash commands
- env vars and config keys
- armory file layout
- cache path meanings
- JSON/JSONL fields
- exit behavior
- parseable stdout
- TUI keymap behavior

Hardening rules:

- Validate path traversal, control characters, pre-encoded values, shell metacharacters, and query fragments before use.
- Bound output by default.
- Do not interpolate untrusted material names, evidence text, provider responses, or user input into suggested shell commands.
- Avoid raw stack traces and upstream objects outside debug modes.
- Tests should cover TTY, non-TTY, JSON/JSONL, missing credentials, invalid paths, no materials, no evidence, and provider failure variants when those contracts change.
