# Web System

Browser and brand rules.

## Stack

Current default stack:

- HTML
- CSS
- vanilla JavaScript or tiny TypeScript
- static files by default

Keep the current static stack unless product direction requires a broader one.

## Tokens

Use exact values from design docs or source.

Required token meanings:

- background: root and page canvas
- foreground: highest-emphasis readable text
- surface: raised panels and cards
- primary: brand and highest-emphasis text
- secondary: labels and quiet icons
- tertiary: muted values and helper copy
- accent: primary action, warning accent, focused command action
- error: error text and destructive warnings
- success: success text and badges
- border: subtle borders and separators
- focus: visible focus indication

## Typography

- Use product font stack from design docs.
- Use mono for commands, code, paths, IDs, metrics, evidence IDs, and timestamps.
- Letter spacing is 0.
- Keep font weight stable on hover, focus, active, and selected states.
- Use tabular numbers for counters, timers, metrics, and totals.

## Layout

- Use responsive constraints, not viewport-scaled font sizes.
- Cards are for repeated items, settings groups, detail panels, and tools.
- Use native `<button>` elements for actions.
- Icon-only buttons need `aria-label`.
- Inputs need labels and correct types.
- Use `<table>` for tabular data.
- Evidence panels must show source identity and missing/unverified state with text.

## Media

- Use real images for inspectable images.
- Provide useful alt text for meaningful images.
- Mark decorative images with empty alt text.
- Frequent interactions use minimal motion.
- Respect reduced motion.

## Review

Before shipping web UI, verify desktop and mobile widths, keyboard operation, focus visibility, text fit, no layout shift, contrast, and no framework/build-step drift.
