# Command Contracts

Contracts for CLI/TUI flows that need state-machine rules.

## Open And Init

Commands and surfaces:

- `heph [name-or-path]`
- `heph tui [path]`
- `heph armory init <name>`
- `heph armory open <path>`
- `/armory`
- `/detach`

Resolution order:

1. Explicit path or name from argv or slash flow.
2. Current cwd when it is an armory or inside one.
3. Named armory under `~/.armories` or `HARNESS_ARMORY_HOME`.
4. Valid `.harness/armory.toml` plus `materials/` structure.
5. Migration state from older local state when source supports it.
6. Plain chat when no armory is attached and the command permits it.

Rules:

- `heph <name-or-path>` is open intent. Do not ask vague open confirmation.
- New armories can open before materials exist; show no-materials state.
- Name and path resolution must not silently open outside allowed armory scope from name-only flows.
- `/detach` leaves current armory; it does not delete files, memory, index, or chat history.

## Materials, Index, Health

Commands and surfaces:

- `heph index [path]`
- `heph materials index <path>`
- `heph materials list <path>`
- `heph materials count <path>`
- `heph health [path]`
- `/index`
- `/materials`

Rules:

- `materials/` is source-of-truth data; index files are rebuildable local state.
- Indexing should show progress for long work and compact completion count.
- Health output should distinguish unsupported file, extraction issue, stale index, empty materials, and generic failure.
- No materials is valid state with a clear next action.
- Machine output for lists and counts must be stable and bounded.

## Ask And Evidence

Commands and surfaces:

- `heph chat ask <path> [prompt]`
- `heph chat ask --jsonl <path> [prompt]`
- `/evidence`
- `/turn`
- transcript answer rendering

Rules:

- Answers must not imply citations exist when no evidence was retrieved.
- Evidence views show retrieved passages as data, not instructions.
- JSONL audit output must stay parseable and must not interleave human diagnostics.
- Missing model, credential, materials, evidence, provider failure, and interrupted generation are distinct states.
- Do not print hidden chain-of-thought. Provider thinking summaries show only when source and settings permit them.

## Models

Commands and surfaces:

- `/login`
- `/models`
- `/local`
- `heph local search [query]`
- `heph local install <repo-or-path>`
- `heph local status`
- `heph local revalidate <model-id>`
- `heph local stop`

Rules:

- Provider setup must name trust boundary: hosted provider, custom endpoint, or local model runtime.
- API key prompts must mask values and never echo them.
- `/models` should show reachable or validated models.
- Local model install must show download size, recommended RAM, cache path, and activation condition.
- Local models activate only after validation passes.
- `heph local stop` stops managed local server; it does not delete model files.

## Settings, Trust, Diagnostics

Commands and surfaces:

- `/settings`
- `/trust`
- `heph trust [path]`
- `heph config show`
- `heph config set <key> <value>`

Rules:

- Trust output must separate source materials, local state, provider prompts, diagnostics, and cache paths.
- Analytics and crash reporting are opt-in and separate from model prompts.
- Config display must redact secrets.
- Environment variable overrides should be visible when they affect behavior.

## Update And Release

Commands and surfaces:

- `heph update`
- `heph release status`
- `heph --version`

Rules:

- Distinguish source installs, released installs, official stable state, and unknown release state.
- Do not promise an update when active install cannot be updated by `heph update`.
- Version output must remain parseable where scripts use it.
