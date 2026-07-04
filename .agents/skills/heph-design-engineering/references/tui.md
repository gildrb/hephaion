# Heph CLI And TUI Design Engineering

Terminal and Textual rules adapted from Heph `cli-design.md`.

## Core Contract

- Default theme is dark; valid presets are dark and light.
- `interfaces.palette.Theme` is the canonical CLI color contract.
- Concrete colors stay centralized in `interfaces.palette`.
- TUI and terminal code should use semantic roles such as `text_primary`, `text_secondary`, and `action_primary_bg`.
- Do not add ad hoc hex values in render code.
- Labels are uppercase.
- UI-owned values are lowercase.
- Preserve literal user, model, file, path, provider, and evidence values when correctness requires it.
- Do not use color alone to communicate state.
- Dark theme root/background surfaces can be transparent so the terminal owns the base canvas.
- The CLI has no radius, shadows, or web line-height.

## Palette Roles

Use the existing role names and source values from Heph implementation:

- `bg_app`: root app and screen background
- `bg_surface`: primary shell, transcript, lists, status, footer, and side-panel surface
- `bg_raised`: raised user/composer panels and user transcript blocks
- `text_primary`: main transcript text and primary readable text
- `text_secondary`: labels, shortcuts, and metadata
- `text_muted`: values, footer body, disabled items, activity, notice, secondary detail
- `text_inverse`: inverse text on solid action fills
- `border_subtle`: reserved subtle border role
- `brand_primary`: Heph title and highest emphasis
- `action_primary_bg`: selection/action fill and accent/warning ANSI styles
- `action_primary_text`: text on action fill
- `status_success_text`: success messages
- `status_error_text`: errors and auth/config warnings

## Terminal ANSI Roles

Use existing terminal style tokens:

- `STYLE_PROMPT` for menu titles, section labels, current state badges
- `STYLE_BRAND` for brand emphasis
- `STYLE_ACCENT` and `STYLE_WARNING` for accent/warning emphasis
- `STYLE_SUCCESS` for success output
- `STYLE_ERROR` for `error:` prefixes and error messages
- `STYLE_CHROME_LABEL`, `STYLE_SHORTCUT`, and `STYLE_METADATA` for labels
- `STYLE_CHROME_DETAIL` and `STYLE_DIM` for secondary detail
- `STYLE_EMPHASIS`, `STYLE_ASSISTANT`, and `STYLE_EMBER` only where source patterns use them

Do not hand-code ANSI when a semantic token exists.

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
MODEL gpt-5.5
REASONING low
SCOPE 3/8
EVIDENCE none yet
STATE current
```

## Textual Layout Contract

Respect the existing full-height vertical screen:

- top content area with shell and optional side panel
- status line one terminal cell high
- transcript log as the flexible center
- thinking indicator visible only while active
- composer frame as raised user block
- completion stack for suggestions, position, and footer
- info panel with draggable width and narrow minimum

Use terminal cells and content width rules rather than web spacing units. Do not import web card, radius, or shadow patterns into TUI surfaces.

## Component Rules

### Status

- One-cell top status line.
- Brand title uses `brand_primary`.
- Labels use `text_secondary`.
- Values use `text_muted` unless preserving a high-emphasis state.
- Missing API or config state must include readable text.

### Transcript

- Assistant markdown uses inherited surface and primary text.
- Evidence citations and source footers are dimmed but readable.
- User transcript blocks use raised background and stable padding.
- Do not let activity or notice rows obscure current answer content.

### Composer

- Raised input block with primary text.
- Prompt cell is fixed-width and stable.
- Placeholder uses secondary text.
- Cursor and selection states must remain visible.
- Compact mode must not break text fit.

### Suggestions And Inline Menus

- Generic option lists may use solid action fill.
- Completion and inline menus use quieter selection when source patterns do.
- Selected prefix and label use brand emphasis.
- Descriptions are muted and aligned with stable gaps.
- Position indicators remain muted and compact.

### Info Panel

- Side panel surfaces remain quiet and dense.
- Labels are uppercase.
- Material entries render as `@name` where the app pattern uses material tokens.
- Hidden counts use compact forms such as `MORE +n`.
- Disabled material state uses muted text, not error color.

### Armory And Materials Browsers

- Inline browsers replace transcript while active.
- Headers start with compact scope/count state.
- Selected rows should not shift layout.
- Error rows are one-cell and use error text plus readable state.

## TUI Review Gates

Before shipping TUI or terminal design changes:

- compare token usage to `interfaces.palette.Theme`
- verify dark and light themes if the change touches theme roles
- verify narrow terminal behavior
- verify labels uppercase and value casing rules
- verify focus, selected, disabled, loading, empty, and error states
- verify no state depends on color alone
- verify docs drift with `cli-design.md`
