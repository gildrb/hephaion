# Heph CLI And TUI Design Engineering

Terminal and Textual rules for Heph.

## Core Contract

- Default theme and valid presets come from Heph source and design docs.
- Concrete colors stay centralized in the palette implementation.
- TUI and terminal code should use semantic roles.
- Do not add ad hoc hex values in render code.
- Labels are uppercase.
- UI-owned values are lowercase.
- Preserve literal user, model, file, path, provider, and evidence values when correctness requires it.
- Do not use color alone to communicate state.
- The CLI has no radius, shadows, or web line-height.

## Label And Value Grammar

The CLI uses:

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

## Textual Layout Contract

Respect the existing full-height vertical screen and source selectors. Use terminal cells and content width rules rather than web spacing units. Do not import web card, radius, or shadow patterns into TUI surfaces.

## Component Rules

- Status labels use quiet label styling; values preserve exactness when needed.
- Evidence citations and source footers are dimmed but readable.
- Composer cursor and selection states must remain visible.
- Selected rows should not shift layout.
- Disabled material state uses muted text, not error color.
- Error rows use error text plus readable state.

## TUI Review Gates

Before shipping TUI or terminal design changes, verify semantic palette use, dark/light behavior when relevant, narrow terminal behavior, focus/selection states, uppercase labels, value preservation, and design-doc drift.
