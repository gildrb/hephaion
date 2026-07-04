# Web System

Browser and brand rules.

## Stack

Default stack:

- HTML
- CSS
- vanilla JavaScript or tiny TypeScript
- no framework by default
- no component library by default
- no router by default
- no bundler by default
- static files by default

Do not introduce a framework, component library, router, CSS framework, preprocessor, or build system unless product direction requires it.

## Theme And Tokens

Use exact values from design docs or source. Do not invent adjacent shades in component code.

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
- Do not animate or change font weight on hover, focus, active, or selected states.
- Use tabular numbers for counters, timers, metrics, and totals.

## Layout And Components

- Use responsive constraints, not viewport-scaled font sizes.
- Do not create card-in-card layouts.
- Cards are for repeated items, settings groups, detail panels, and tools.
- Use native `<button>` elements for actions.
- Icon-only buttons need `aria-label`.
- Inputs need labels and correct types.
- Use `<table>` for tabular data.
- Evidence panels must show source identity and missing/unverified state with text.

## Media And Motion

- Use real images for inspectable images.
- Provide useful alt text for meaningful images.
- Mark decorative images with empty alt text.
- Frequent interactions should avoid extra animation.
- Respect reduced motion.

## Review Gates

Before shipping web UI, verify desktop and mobile widths, keyboard operation, focus visibility, text fit, no layout shift, contrast, and no framework/build-step drift.
