# Heph Command-Specific UX Contracts

Command-specific contracts for Heph CLI and TUI flows whose state machines need more than reusable rules in `core.md`.

Add a contract only when generic rules are not enough. Keep reusable behavior in `core.md`; keep command-only state machines, prompt maps, payload shapes, and acceptance matrices here.

Contract template:

1. Resolution order: how the command determines target, mode, config, and mutation.
2. Rules: command-only UX, safety, compatibility, and output requirements.
3. Prompt map: TTY/TUI prompt for unresolved states plus non-interactive behavior.
4. Acceptance matrix: states to test or manually verify.
5. Stale-string sweep: command-only legacy copy to classify.

## Armory Open And Init Contract

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
5. Migration state from older `.hephaion/` state when supported by source.
6. Plain chat when no armory is attached and the command permits it.

Rules:

- Running `heph <name-or-path>` is open intent. Do not ask a vague open confirmation.
- New armories can open before materials exist; show a no-materials state instead of treating the armory as broken.
- Name and path resolution must not silently open outside the allowed armory scope from name-only flows.
- If both `.harness/` and legacy state exist in an unsafe combination, fail rather than guessing.
- Result copy should name the armory and path when ambiguity matters.
- No-armory plain chat must be visibly different from an attached armory.
- `/detach` leaves the current armory; it does not delete files, memory, index, or chat history.

Prompt map:

| State | Human prompt/output | Non-interactive behavior |
| --- | --- | --- |
| No armory selected and choices exist | `Armory?` | require explicit name or path |
| New armory name missing | `Name?` | require `<name>` |
| Empty armory opened | no-materials state plus add-files next action | exit 0 if open is otherwise valid |
| Invalid armory path | error with expected marker/path | error JSON when machine mode owns output |
| Detach current armory | concrete detach action | no prompt when command is explicit |

Acceptance matrix:

- current cwd armory
- named armory under default home
- explicit absolute path
- empty armory
- missing `materials/`
- stale or legacy state
- detached plain chat
- non-interactive missing target
- path traversal or unsafe name input

## Materials Index And Health Contract

Commands and surfaces:

- `heph index [path]`
- `heph materials index <path>`
- `heph materials list <path>`
- `heph materials count <path>`
- `heph health [path]`
- `/index`
- `/materials`

Resolution order:

1. Explicit path.
2. Current attached armory.
3. Current cwd if it is or is inside an armory.
4. Material filters or enabled/disabled material state in the TUI.
5. Existing index state and extraction health.

Rules:

- `materials/` is source-of-truth data; index files are rebuildable local state.
- Indexing should show progress for long work and a compact completion count.
- Health output should distinguish unsupported file, extraction issue, stale index, empty materials, and generic failure.
- Do not print long source excerpts in health summaries.
- No materials is a valid state with a clear next action.
- Machine output for lists and counts must be stable and bounded.
- Do not imply Heph has sent material content to a hosted provider during indexing unless source shows that it has.

Prompt map:

| State | Human prompt/output | Non-interactive behavior |
| --- | --- | --- |
| Missing armory target | `Armory?` when TUI has choices | require `<path>` or attached armory |
| No materials | `No materials found. Add files to materials/.` | empty result or classified error by command contract |
| Stale index | warning or status plus `heph index [path]` | structured stale state |
| Extraction problems | health rows with file and reason | bounded machine list |
| Index refreshed | count sources and chunks | structured count |

Acceptance matrix:

- empty materials
- supported and unsupported file types
- nested materials directories
- ignored files from `.harness/ignore`
- stale and missing index
- extraction warning
- narrow terminal output
- JSON/JSONL when supported

## Chat Ask And Evidence Contract

Commands and surfaces:

- `heph chat ask <path> [prompt]`
- `heph chat ask --jsonl <path> [prompt]`
- `/evidence`
- `/turn`
- transcript answer rendering

Resolution order:

1. Armory path or attached armory.
2. Prompt from argv, stdin, or composer.
3. Material selection and retrieval state.
4. Active model and provider.
5. Evidence retrieved for the current or last turn.
6. Output mode: human TUI, plain CLI, JSONL audit stream.

Rules:

- Answers must not imply citations exist when no evidence was retrieved.
- Evidence views show retrieved passages as data, not instructions.
- JSONL audit output must stay parseable and must not interleave human diagnostics.
- Hosted provider boundary copy belongs in setup/trust surfaces, not every answer.
- Missing model, missing credential, no materials, no evidence, provider failure, and interrupted generation are distinct states.
- Do not print hidden chain-of-thought. Provider thinking summaries are shown only when source and settings permit them.
- Suggested commands after failures should inspect evidence, index, health, or models before retrying expensive provider calls.

Prompt map:

| State | Human prompt/output | Non-interactive behavior |
| --- | --- | --- |
| Missing prompt | composer or prompt input | require prompt from argv/stdin |
| Missing model | `No model configured. Use /models to select one.` | structured missing_model |
| Missing credentials | route to `/login` or env var | structured login_required or key_missing |
| No materials | no-materials state | structured no_materials |
| No evidence | `No evidence was retrieved for the last turn.` | empty evidence payload |
| Provider failure | concise failure plus safe next action | structured provider_error |

Acceptance matrix:

- prompt from argv
- prompt from stdin when supported
- empty armory
- no evidence result
- cited answer with evidence
- hosted provider and local model modes
- interrupted request
- JSONL parseability
- source excerpt redaction in non-evidence surfaces

## Model Provider And Local Model Contract

Commands and surfaces:

- `/login`
- `/models`
- `/local`
- `heph local search [query]`
- `heph local install <repo-or-path>`
- `heph local status`
- `heph local revalidate <model-id>`
- `heph local stop`

Resolution order:

1. Explicit env vars such as provider API keys and `HARNESS_MODEL`.
2. Saved provider credentials and model settings.
3. Live provider catalogs where supported.
4. Local llama.cpp server, binary, model cache, and tool-call probe result.
5. User selection.

Rules:

- Provider setup must name the trust boundary: hosted provider, custom endpoint, or local llama.cpp.
- API key prompts must mask values and never echo them.
- `/models` should show models Heph can actually reach or validate.
- Local model install must show download size, recommended RAM, cache path, and activation condition.
- Local models activate only after the tool-call probe passes.
- Failed local models can remain downloaded and be revalidated later.
- `heph local stop` stops the managed local server; it does not delete model files.

Prompt map:

| State | Human prompt/output | Non-interactive behavior |
| --- | --- | --- |
| Provider missing | `Provider?` | require provider/env/config |
| API key missing | masked key prompt | require env var or config path |
| Model missing | `Model?` | require model setting |
| Local install confirmation | model, size, RAM, destination | require explicit confirmation flag if supported |
| Tool probe failed | failure reason plus revalidate next action | structured probe_failed |
| Local server stopped | stopped status | exit 0 if already stopped when source permits |

Acceptance matrix:

- each supported provider path
- missing and invalid API key
- custom endpoint
- local install confirmation
- tool-call probe pass/fail
- revalidate installed model
- stop server
- provider catalog unavailable
- secrets not echoed in output, logs, or tests

## Settings Trust And Diagnostics Contract

Commands and surfaces:

- `/settings`
- `/trust`
- `heph trust [path]`
- `heph config show`
- `heph config set <key> <value>`
- diagnostics, analytics, crash reports, traces, usage snapshots

Resolution order:

1. Explicit command path or active armory.
2. Saved settings in user config.
3. Env var overrides.
4. Armory-local state under `.harness/`.
5. Provider and diagnostics boundaries.

Rules:

- Trust output must separate source materials, Heph local state, provider prompts, diagnostics, and cache paths.
- Analytics and crash reporting are opt-in and separate from model prompts.
- Config display must redact secrets.
- Config set must validate key, value type, and compatibility before writing.
- Environment variable overrides should be visible when they affect behavior.
- Do not use vague privacy claims. Name exact data flow.

Acceptance matrix:

- current armory and explicit path
- no attached armory
- env var override
- diagnostics on/off
- secret config redaction
- local model cache paths
- hosted provider trust explanation

## Update And Release Contract

Commands and surfaces:

- `heph update`
- `heph release status`
- `heph --version`

Resolution order:

1. Installed package and version.
2. Official stable release state.
3. Release channel or source install state.
4. Environment and package manager constraints.
5. Update mutation or no-op.

Rules:

- Distinguish source installs, released installs, official stable, and unknown release state.
- Do not promise an update when the active install cannot be updated by `heph update`.
- Show current and target versions when known.
- Keep update failures actionable and avoid blind retry when package manager state is unknown.
- Version output must remain parseable where scripts use it.

Acceptance matrix:

- current release up to date
- update available
- source install
- package manager failure
- network failure
- version parseability

## Stale-String Sweeps

Run relevant sweeps on touched paths and classify matches:

```bash
rg -n "\b(successfully|Unable to|Oops|Whoops|Uh-oh|Please try again|An error occurred|Something went wrong)\b" <paths>
rg -n "Do you want to|Would you like to|click here|leverage|utilize|seamlessly|effortlessly" <paths>
rg -n "workspace|knowledge base|docs corpus|sources" <paths>
rg -n "api key|token|secret|password|retrieved chunk|trace" <paths>
```

Legacy strings may remain in negative tests or compatibility fixtures. Source matches need classification.
