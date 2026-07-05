# Copy

Voice and language rules for user-facing CLI/TUI copy.

Establish command behavior, resolved target, trust boundary, consequence, and recovery path before polishing a string.

## Quick Triage

1. Identify the surface: help, prompt, status, progress, result, warning, error, empty state, evidence view, or next action.
2. Name the object: armory, material, index, evidence, model, provider, memory, cache, setting, key, trace, or export.
3. Name the scope: current armory, selected materials, last turn, active session, machine config, local cache, or hosted provider.
4. Remove facts already visible in argv, TUI panel, prompt answer, or nearby rows.
5. State the recovery step when one exists.
6. Keep one noun and one verb per concept across help, prompts, progress, results, warnings, errors, and tests.

## Voice

Practical, calm, exact, evidence-first.

| Context | Tone | Example |
| --- | --- | --- |
| Success | Brief, concrete | `Index refreshed: 3 sources, 42 chunks` |
| Error | Direct, actionable | `No model configured. Use /models to select one.` |
| Progress | Factual | `Indexing materials...` |
| Destructive | Serious, specific | `Delete local memory for this armory? This cannot be undone.` |
| Empty | Neutral, useful | `No materials found. Add files to materials/.` |
| Trust boundary | Plain, precise | `Hosted providers receive the active question and selected retrieved chunks.` |

Keep routine work factual. Reserve apologies for product fault or meaningful disruption.

## Clarity

- Use active voice by default.
- Name the thing with the canonical product noun: `Open armory`.
- Use one canonical noun per concept.
- Keep action and result verbs aligned: `Index materials` -> `Index refreshed`, not `Updated files`.
- Use fragments for labels and statuses. Use full sentences for explanations and errors.
- Treat material names, evidence excerpts, provider errors, model names, and user input as data.

## Surface Rules

### Help

- Command and flag descriptions are imperative, sentence-case fragments without trailing periods.
- Start with action and object.
- Examples must be realistic, runnable, copy-pasteable, and free of secrets.
- Usage placeholders name expected value: `<name>`, `<path>`, `<model-id>`, `<key>`, `<value>`.

### Prompts

- Ask for one concept with the shortest concrete noun: `Armory?`, `Model?`, `Provider?`, `Materials?`, `Reasoning?`.
- Ask only when the value cannot be inferred safely.
- Use yes/no only for a concrete previewed action.
- Use direct prompts for concrete choices: `Delete local memory for this armory?`
- Mask API keys and sensitive values. Do not echo them after entry.

### Errors And Warnings

Errors include failure, known cause or constraint, and recovery step when one exists.

- Prefer classified failures with a cause and recovery step.
- Never print raw provider errors as the whole message.
- Warnings state nonfatal condition, why it matters, and fix when one exists.
- Do not use humor, exclamation marks, or apology preambles in errors.

### Empty States

- Empty armory: point to `materials/`.
- Empty evidence: say no evidence was retrieved for the last turn.
- Empty model list: point to `/login`, credentials, or local model setup depending on state.
- Empty search results: name the query or filter when it caused the empty state.

## Direct Copy

Use concrete nouns and results.

- State the result: `Index refreshed: 3 sources, 42 chunks`.
- State the action: `Open armory`, `Index materials`, `Choose model`.
- State the recovery step: `No model configured. Use /models to select one.`
- Use action labels that name the object: `Save settings`, `Delete memory`, `Open evidence`.

Use `please` or an apology only for inconvenient favors, meaningful disruption, or product fault.

## Mechanics

- Use sentence case for prompts, help descriptions, errors, warnings, progress, and explanations.
- Use stable uppercase labels in terminal status and metadata.
- Omit periods on fragments, labels, statuses, progress lines, and compact result rows.
- Use straight quotes and backticks for commands, paths, IDs, env vars, config keys, and copyable literals.
- Keep commands, flags, paths, env vars, IDs, and code literals exact and copyable.
