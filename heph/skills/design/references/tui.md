# CLI/TUI System

Terminal and Textual rules.

## Contract

- Default theme and valid presets come from source and design docs.
- Concrete colors stay centralized in palette implementation.
- TUI and terminal code should use semantic roles.
- Labels are uppercase.
- UI-owned values are lowercase.
- Preserve literal user, model, file, path, provider, and evidence values when correctness requires it.
- Pair color with text state.
- CLI has no radius, shadows, or web line-height.

## Label Grammar

```text
LABEL value
```

Rules:

- Label is always uppercase.
- Menu metadata values are lowercased when UI-owned.
- Plain label/value lines preserve value text because paths, model IDs, commands, and evidence IDs can be case-sensitive.

Examples:

```text
ARMORY research-course
MODEL local-model
REASONING low
SCOPE 3/8
EVIDENCE none yet
STATE current
```

## Layout

Respect existing full-height vertical screen and source selectors. Use terminal cells and content width rules.

## Components

- Status labels use quiet label styling; values preserve exactness when needed.
- Evidence citations and source footers are dimmed but readable.
- Composer cursor and selection states must remain visible.
- Selected rows should not shift layout.
- Disabled material state uses muted text, not error color.
- Error rows use error text plus readable state.

## Review

Before shipping terminal changes, verify semantic palette use, dark/light behavior when relevant, narrow terminal behavior, focus/selection states, uppercase labels, value preservation, and design-doc drift.
