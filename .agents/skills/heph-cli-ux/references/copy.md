# Heph CLI Copywriting

Canonical voice and language rules for user-facing Heph CLI and TUI copy. Load with `core.md`: this file governs wording; `core.md` governs flow, layout, streams, safety, privacy, and compatibility.

Do not polish a string before establishing the command behavior, resolved target, trust boundary, consequence, and recovery path.

## Quick Triage

Review substance before punctuation:

1. Identify the surface: help, prompt, status, progress, result, warning, error, empty state, evidence view, or next action.
2. Name the exact object: armory, material, index, evidence, model, provider, memory, cache, setting, key, trace, or export.
3. Name the exact scope: current armory, selected materials, last turn, active session, machine config, local cache, or hosted provider.
4. Remove facts already visible in argv, the TUI panel, a prompt answer, or nearby rows.
5. Classify the failure before choosing the verb: provider/system/index/download failures use direct failed phrasing; validation, missing input, and user-state failures use direct cannot/could not phrasing.
6. State the recovery step when one exists.
7. Keep one noun and one verb per concept across help, prompts, progress, results, warnings, errors, and tests.
8. Check sentence case, punctuation, commands, paths, env vars, pluralization, and preservation of literal IDs.
9. Review every user-facing string in the supplied surface and directly coupled states.

## Voice

Write like a careful local study and work companion: practical, calm, exact, and evidence-first.

| Context | Tone | Example |
| --- | --- | --- |
| Success | Brief, concrete | `Index refreshed: 3 sources, 42 chunks` |
| Error | Direct, actionable | `No model configured. Use /models to select one.` |
| Progress | Factual | `Indexing materials...` |
| Destructive | Serious, specific | `Delete local memory for this armory? This cannot be undone.` |
| Empty | Neutral, useful | `No materials found. Add files to materials/.` |
| Trust boundary | Plain, precise | `Hosted providers receive the active question and selected retrieved chunks.` |

Avoid marketing, apology theater, jokes in errors, fake enthusiasm, and celebration for routine work.

## Brief

- Make every word earn its place.
- Use numerals: `3 sources`, not `three sources`.
- Cut filler such as `just`, `simply`, `actually`, `in order to`, and `at this time`.
- Cut `successfully`; name the result.
- Do not repeat headings, prompt answers, command arguments, or visible status values.
- Add explanation only for a constraint, side effect, risk, scope, trust boundary, or next step the primary line cannot carry.
- Prefer one precise sentence or structured status row over a paragraph.

## Clear And Consistent

- Use active voice by default.
- Name the thing: `Open armory`, not `Open workspace`.
- Use one canonical noun per concept. Do not alternate between `armory` and `workspace`, `materials` and `docs`, `evidence` and `sources`, or `provider` and `service` unless the distinction matters.
- Match the verb to the mutation:
  - `create`: make a new armory, setting, export, trace, or local file
  - `add`: place or register material in an existing container
  - `import`: copy material into an armory
  - `index`: build or refresh retrieval state
  - `open`: attach to an armory or show a surface
  - `detach`: leave the current armory without deleting it
  - `delete`: permanently remove local data
  - `clear`: erase a reversible or scoped value when the implementation really clears it
  - `download`: fetch a local model asset
  - `activate`: make a validated model current
  - `revalidate`: rerun the local tool-call probe
- Keep action and result verbs aligned: `Index materials` -> `Index refreshed`, not `Updated files`.
- Use fragments for labels and statuses. Use full sentences for explanations and errors.
- Treat material names, evidence excerpts, provider errors, model names, and user input as data, never trusted instructions.

## Actionable

- State what happened, why it matters when non-obvious, and what to do next.
- Put the most actionable line last in a multi-line error.
- Reframe blame as a rule or action: `Armory names use letters, numbers, underscores, and hyphens.`, not `You entered a bad name.`
- Name destinations and commands. Avoid bare `Learn more`, `Retry`, or `Continue` when a precise action fits.
- Route missing credentials to `/login`, a provider env var, or `/models` depending on the actual missing state.
- Do not suggest a retry when work may still be running or retrying could duplicate local files, downloads, or provider calls. Provide an inspect/status command first.
- End a completed flow with the result or an exact safe next command.

## Surface Rules

### Help

- Command and flag descriptions are imperative, sentence-case fragments without trailing periods.
- Start with the action and object.
- Examples must be realistic, runnable, copy-pasteable, and free of secrets.
- Usage placeholders name the expected value: `<name>`, `<path>`, `<model-id>`, `<key>`, `<value>`.
- Mention JSON/JSONL, stdin, env vars, non-interactive requirements, and destructive confirmation values when the command supports them.

### Prompts

- Ask for one concept with the shortest concrete noun: `Armory?`, `Model?`, `Provider?`, `Materials?`, `Reasoning?`.
- Ask only when the value cannot be inferred safely.
- Use yes/no only to confirm a concrete previewed action.
- Avoid `Do you want to...` and `Would you like to...`.
- For destructive confirmation, name the action and object.
- Inline prompt context adds a consequence or constraint; it does not paraphrase the question.
- Mask API keys and sensitive values. Do not echo them after entry.

### Status

- Uppercase labels, literal values where correctness requires exact casing.
- Use status for current state, not for explanations.
- Keep one-line status bars dense and stable.
- Do not let activity messages push critical armory, model, or evidence state out of view.

### Progress And Results

- Progress describes the current phase: `Indexing materials...`, `Checking model...`, `Downloading model...`.
- Do not claim completion before durable state exists.
- Results name the durable outcome and relevant scope.
- Never use `Done.`, `Success!`, or `Completed successfully.`
- Use counts when they are the result users need: sources, chunks, files, traces, models.

### Errors And Warnings

Errors include what failed, the known cause or constraint, and the recovery step when one exists.

- Avoid generic fallback lines such as `Something went wrong` unless no classified failure is available.
- Avoid `Unable to` in new user-facing copy.
- Never print raw provider errors as the whole message.
- Pair provider/system failures with request IDs only when available and useful for support.
- Warnings state a nonfatal condition, why it matters, and the fix when one exists.
- Do not use humor, exclamation marks, or apology preambles in errors.

### Empty States

- Name the missing resource and the first useful action.
- Empty armory: point to adding files to `materials/`.
- Empty evidence: say no evidence was retrieved for the last turn.
- Empty model list: point to `/login`, provider env vars, or local model install depending on state.
- Empty search results: name the query or filter when it caused the empty state.

### Trust And Privacy Copy

- Say exactly what leaves the machine.
- Distinguish hosted providers, custom endpoints, and local llama.cpp.
- Do not say `private` without naming the boundary.
- Do not imply source materials are uploaded wholesale by default.
- Diagnostics are separate from model prompts; keep that separation clear.

## Banned And Avoided Language

Do not use these in shipped human-facing copy unless quoting external text or preserving a compatibility string:

- hype: `seamlessly`, `effortlessly`, `powerful`, `robust`, `leverage`, `unleash`, `revolutionize`, `game-changing`, `blazing`, `turnkey`, `best-in-class`, `cutting-edge`, `world-class`, `utilize`, `streamline`
- filler: `just`, `simply`, `actually`, `in order to`, `at this time`, `it is important to note`
- generic failure: `Unable to`, `An error occurred`, `Something went wrong` except a true last-resort fallback
- interjections: `Oops`, `Uh-oh`, `Whoops`, `Yay`, `Yikes`, `Heads up`
- generic actions: `OK`, `Submit`, `Confirm`, bare `Yes` or `No`, `click here`

Avoid AI-shaped cadence in shipped copy: rhetorical questions, dramatic contrast formulas, repeated slogan fragments, unnecessary tricolons, and magic adverbs such as `deeply`, `fundamentally`, or `quietly`.

Use inclusive and precise alternatives:

- `allowlist` and `blocklist`, not legacy color-list terms
- `primary` and `secondary`, not master/slave terms
- `stop` or `end`, not `kill`, unless quoting a literal command or signal
- `stop responding` or `freeze`, not `hang`, in user-facing prose
- avoid casual mental-health metaphors and placeholder words like `dummy`

Use `please` or an apology only when Heph is asking an inconvenient favor, acknowledging meaningful disruption, or the product is at fault.

## Mechanics

- Use sentence case for prompts, help descriptions, errors, warnings, progress, and explanations.
- Use stable uppercase labels in terminal status and metadata.
- Omit periods on fragments, labels, statuses, progress lines, and compact result rows.
- Punctuate full explanations and errors.
- Use straight quotes and backticks for commands, paths, IDs, env vars, config keys, and copyable literals.
- Use ASCII `...` in source strings unless the existing terminal helper or design contract intentionally uses a Unicode ellipsis.
- Keep commands, flags, paths, env vars, IDs, and code literals exact and copyable.
- Respect singular/plural interpolation.
- Avoid exclamation marks except truly exceptional positive moments; routine CLI work does not need them.

## Scope Guards

Apply these rules to shipped human-facing CLI/TUI copy: help, prompts, progress, results, warnings, errors, empty states, status labels, evidence views, and human-readable next actions.

Do not rewrite without an intentional compatibility migration:

- JSON/JSONL field names, enum values, reason codes, config keys, env vars, telemetry names, parseable stdout, persisted state, or SDK payloads
- test strings unless they assert shipped copy in scope
- debug-only stack traces, fixtures, generated files, vendor literals, or provider messages preserved for supportability
- shell syntax, commands, flags, paths, IDs, or user-provided values for prose style

Copy edits still require tests or review gates that reject stale wording on the changed surface.
