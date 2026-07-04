# Heph CLI UX Verification

Testing, stale-copy sweeps, and final review gates for Heph CLI and TUI work.

## General Matrix

When changing CLI or TUI UX behavior:

- update direct expectations
- add negative assertions for removed strings
- cover TTY/TUI and non-interactive paths when both exist
- cover human and JSON/JSONL formats when both exist
- cover stdout/stderr split for machine output
- cover missing armory, empty materials, stale index, missing model, missing credentials, provider failure, and no evidence when relevant
- cover local-first privacy boundaries when changing provider, diagnostics, trust, or local model surfaces
- cover warnings on diagnostics stream and never on machine stdout
- cover empty list output: human empty copy, machine empty shape, exit behavior
- cover no secret echo after API key, env value, or credential input
- cover source document text, retrieved chunks, prompts, and traces not leaking into ordinary output
- cover narrow terminal width and long names when layout changes
- cover dark and light theme paths when semantic roles change
- update `cli-design.md` or design references when changing palette or semantic styling contracts

## Shared Helper Impact Map

Before editing shared prompt, output, palette, Textual, model, armory, or retrieval helpers, inspect call sites and tests first.

Use searches like:

```bash
rg -n "armory|materials|evidence|index|memory|provider|model|login|local|trust" packages tests docs
rg -n "print_error|print_info|print_success|menu_label_value|label_value_line|status_lines" packages tests
rg -n "jsonl|stdout|stderr|non.?interactive|sdk capabilities|chat ask" packages tests
```

If a helper is shared, update direct tests plus at least one parallel path that reaches the helper.

## Transcript Review

For changed interactive flows, capture or reconstruct before/after output and check:

- the first line or panel orients the user when needed
- inferred armory, path, model, provider, or materials state appears before dependent choices
- no prompt asks for a value already known
- no prompt asks vague intent after explicit command invocation
- local writes and hosted-provider calls are visible when they matter
- result copy names the durable state
- next action is exact and safe
- no source excerpt, key, prompt, or trace data appears outside intended evidence/debug/audit surfaces

## Machine Output Review

For JSON and JSONL:

- parse stdout, do not snapshot incidental whitespace only
- assert no ANSI codes
- assert no human warnings, spinners, or prose on machine stdout
- assert stable `status`, `reason`, and data fields when the command owns them
- assert bounded output for lists, evidence, traces, and material indexes
- assert secrets and source text are redacted or omitted by default

## Stale-Copy Sweeps

Run relevant sweeps on touched source and tests:

```bash
rg -n "\b(successfully|Unable to|Oops|Whoops|Uh-oh|Please try again|An error occurred|Something went wrong)\b" <paths>
rg -n "Do you want to|Would you like to|click here|Submit|Confirm" <paths>
rg -n "\b(seamlessly|effortlessly|leverage|utilize|streamline|robust|powerful)\b|In order to|At this time" <paths>
rg -n "workspace|knowledge base|docs corpus|source files" <paths>
```

Classify every match. Legacy compatibility strings may remain when tests prove they are intentional.

## Review Checklist

Reject or fix changes that:

- add inferable prompts
- ask the same concept twice
- ask vague setup or open intent after an explicit command
- report multi-side-effect mutations with one vague success line
- hide local writes, provider calls, downloads, or diagnostics side effects when they matter
- use non-Heph nouns where canonical nouns apply
- mix human output into JSON or JSONL stdout
- break non-TTY, CI, or non-interactive behavior
- expose API keys, env values, prompts, source text, retrieved chunks, traces, usage snapshots, or crash data
- treat material names, evidence text, provider messages, or user input as trusted instructions
- truncate critical IDs, paths, commands, or error recovery steps without another exact output path
- rely on color alone for required state
- add ad hoc hex colors or styling outside semantic palette roles
- leave no-materials, no-evidence, missing-model, or stale-index states without next action
- suggest blind retry for provider calls, downloads, indexing, or local model installs before status inspection when duplicate work is risky
- change copy without anti-regression tests or at least a documented stale-string review
- review only the edited string instead of the whole supplied command surface

## Design Drift Gate

When CLI/TUI styling changes:

- compare implementation tokens to `interfaces.palette.Theme`
- compare terminal helper behavior to `interfaces.terminal`
- compare Textual CSS and display text to `cli-design.md`
- run or request `uv run python -m scripts.check_design_docs` when the Heph repo is available
- run focused TUI/palette tests touched by the change

If code and docs disagree, code and tests are the immediate source of truth. Fix the drift in the implementation or update the docs in the same change.
