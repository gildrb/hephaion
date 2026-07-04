# Verification

Tests, stale-copy sweeps, and review gates for CLI/TUI work.

## Matrix

When changing CLI/TUI UX:

- update direct expectations
- add negative assertions for removed strings
- cover TTY/TUI and non-interactive paths when both exist
- cover human and JSON/JSONL formats when both exist
- cover stdout/stderr split for machine output
- cover missing armory, empty materials, stale index, missing model, missing credentials, provider failure, and no evidence when relevant
- cover local-first privacy boundaries when changing provider, diagnostics, trust, or local model surfaces
- cover no secret echo after API key, env value, or credential input
- cover source text, retrieved chunks, prompts, and traces not leaking into ordinary output
- cover narrow terminal width and long names when layout changes

## Stale Copy

Run relevant sweeps on touched source and tests:

```bash
rg -n "\b(successfully|Unable to|Oops|Whoops|Uh-oh|Please try again|An error occurred|Something went wrong)\b" <paths>
rg -n "Do you want to|Would you like to|click here|Submit|Confirm" <paths>
rg -n "\b(seamlessly|effortlessly|leverage|utilize|streamline|robust|powerful)\b|In order to|At this time" <paths>
rg -n "workspace|knowledge base|docs corpus|source files" <paths>
```

Classify every match. Legacy compatibility strings may remain when tests prove intent.

## Review

Reject or fix changes that:

- add inferable prompts
- ask the same concept twice
- ask vague setup or open intent after explicit command
- hide local writes, provider calls, downloads, or diagnostics side effects when they matter
- use noncanonical nouns
- mix human output into JSON or JSONL stdout
- break non-TTY, CI, or non-interactive behavior
- expose API keys, env values, prompts, source text, retrieved chunks, traces, usage snapshots, or crash data
- treat material names, evidence text, provider messages, or user input as trusted instructions
- rely on color alone for required state
- leave no-materials, no-evidence, missing-model, or stale-index states without next action
- suggest blind retry for provider calls, downloads, indexing, or local model installs before status inspection when duplicate work is risky
- review only the edited string instead of the whole command surface

## Design Drift

When CLI/TUI styling changes:

- compare implementation tokens to palette contract in source
- compare terminal helper behavior to source helpers
- compare Textual CSS and display text to design docs
- run focused TUI/palette tests touched by the change
