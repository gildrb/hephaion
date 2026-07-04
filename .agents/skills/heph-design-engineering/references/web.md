# Heph Web Design Engineering

Browser and brand rules adapted from Heph `design.md`.

## Stack Contract

Default stack:

- HTML
- CSS
- vanilla JavaScript or tiny TypeScript
- no framework by default
- no component library by default
- no router by default
- no bundler by default
- static files by default

Do not introduce a framework, component library, router, CSS framework, preprocessor, or build system unless the product direction explicitly requires it.

## Theme And Tokens

Default theme is dark. Implement foundational values as CSS custom properties.

Required dark token meanings:

- `--color-background`: opaque root background
- `--color-foreground`: highest-emphasis foreground
- `--color-surface`: raised panels, cards, and user-message-like surfaces
- `--color-surface-foreground`: main text on surfaces
- `--color-primary`: brand and highest-emphasis text
- `--color-secondary`: labels and quiet icons
- `--color-tertiary`: muted values and helper copy
- `--color-accent`: primary action, warning accent, focused command action
- `--color-accent-foreground`: text on accent
- `--color-error`: error text and destructive warnings
- `--color-success`: success text and badges
- `--color-border`: subtle borders and separators
- `--color-focus`: visible focus indication

Use the exact values from `design.md` or the implementation source when working in the Heph repo. Do not invent adjacent shades in component code.

## Typography

- Use Geist Sans for interface, headings, and prose.
- Use Geist Mono for commands, code, paths, IDs, metrics, evidence IDs, and timestamps.
- Letter spacing is 0.
- Do not use font weights below 400.
- Do not animate or change font weight on hover, focus, active, or selected states.
- Use tabular numbers for counters, timers, metrics, and totals.
- Keep touch input font sizes at 16px or larger where mobile browsers would zoom.

## Layout And Spacing

- Use a 4px spacing base.
- Use 8px inside compact groups.
- Use 16px between related groups.
- Use 32-40px between major product sections.
- Public pages can breathe more, but should not drift into oversized decorative composition.
- Use responsive constraints, not viewport-scaled font sizes.
- Do not create card-in-card layouts.
- Page sections should be full-width bands or unframed constrained layouts; cards are for repeated items, settings groups, detail panels, and tools.

## Radius And Elevation

- Cards stay at 8px radius or less.
- Buttons and inputs use restrained radius.
- Large 12px radius is reserved for modal-scale surfaces.
- Shadows are only for floating surfaces such as popovers, menus, tooltips, dialogs, and sheets.
- Prefer surfaces and borders over shadow for hierarchy.

## Components

### Buttons

- Use native `<button>` elements for actions.
- Disable buttons during async submission when duplicate action is harmful.
- Icon-only buttons need `aria-label`.
- Icons should use `currentColor`.
- Primary action uses accent background and accent foreground.
- Secondary action uses surface background, primary text, and border.
- Destructive action uses error text and border unless the design explicitly needs a filled destructive action.

### Inputs And Textareas

- Use native form elements and correct input types.
- Labels must focus inputs when clicked.
- Related inputs belong in a `<form>` when Enter should submit.
- Use native validation attributes when they match real requirements.
- Show validation feedback close to the field.
- Do not put placeholder-only labels in production forms.

### Cards

- Use cards for repeated items, settings groups, detail panels, and tool surfaces.
- Do not put cards inside cards.
- Keep card contents scannable: heading, state, metadata, action.
- Do not turn page sections into floating cards.

### Command Palette And Menus

- Use real buttons or links for selectable rows.
- Support keyboard navigation where the component behaves like a menu or palette.
- Use uppercase labels and lowercase UI-owned values.
- Do not delay open behavior behind fragile click-only interactions when pointer down is the expected pattern.

### Data Tables

- Use `<table>` for truly tabular data.
- Header labels are uppercase.
- Values preserve identifiers where needed.
- Prefer fewer columns over wrapped unreadable rows.
- Long paths, evidence IDs, and commands need an exact copyable path.

### Evidence Panel

Evidence panels should show:

- evidence ID in mono
- source path or material name in mono when exactness matters
- uppercase labels
- excerpt text only where inspection is intended
- missing or unverified state with error text plus readable text

### Material Item

Material items should expose:

- `@name` style when representing a material token
- active/disabled state with text and contrast, not color alone
- metadata such as file type, chunk count, or path when useful
- selected state without changing layout size

## Media

- Use real `<img>` elements for inspectable images.
- Provide useful alt text for meaningful images.
- Mark decorative images with empty alt text.
- Lazy-load non-critical images.
- Preload only truly critical first-viewport assets.
- Avoid dark, blurred, cropped, or stock-like media when users need to inspect the real product.

## Motion

- Frequent interactions should avoid extraneous animation.
- Theme switching should not trigger broad transitions.
- Hover styles belong inside hover-capable media queries.
- Touch press states should not leave controls looking hovered.
- Pause or remove looping animation when off-screen.
- Use GPU hints only for measured rendering problems.

## Web Review Gates

Before shipping web UI:

- verify desktop and mobile widths
- verify keyboard-only operation
- verify focus visibility
- verify text fits in buttons, labels, cards, tables, dialogs, and nav
- verify no layout shift on hover or selected state
- verify contrast with dark and light tokens where both are supported
- verify no framework or build-step drift
