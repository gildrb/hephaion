# Core Heph Design Engineering Rules

Reusable design-engineering rules for Heph web, brand, CLI, and TUI surfaces.

## Product Feeling

Heph should feel like a focused reading and thinking instrument:

- private
- precise
- quiet
- local-first
- evidence-forward
- fast
- easy to scan

Avoid decorative color, gradient hero shortcuts, glass effects, oversized marketing cards, stock-feeling visuals, and ornamental animation. The interface should make the user's materials, evidence, armory, and trust boundary legible.

## Source Boundaries

Use the right contract for the surface:

- `cli-design.md`: terminal cells, Textual CSS, ANSI styles, one-line status bars, fixed-width side panels, TUI copy density.
- `design.md`: browser layout, responsive spacing, radius, media, native forms, focus states, static web stack, brand expression.
- Heph source and tests: immediate truth when docs drift.

Do not copy terminal cell dimensions into responsive web layout. Do not copy web radius, cards, and shadows into terminal surfaces.

## Implementation Principles

- Read existing implementation before adding UI.
- Use semantic tokens before raw values.
- Use native HTML controls before custom controls.
- Use Textual and terminal helpers before hand-rolled ANSI or cursor behavior.
- Keep interaction predictable and reversible where possible.
- Avoid layout shift on hover, focus, or selected states.
- Do not animate font weight.
- Respect reduced motion.
- Make disabled and loading states explicit.
- Keep critical IDs, paths, commands, and evidence references exact and copyable.

## Visual Hierarchy

Hierarchy should come from:

1. content structure
2. typography role
3. spacing and grouping
4. neutral foreground contrast
5. border or surface when needed
6. accent color only for action, warning, focus, or selected affordance

Do not make a one-note palette by filling large regions with variations of a single accent. Heph's accent is a tool, not a background mood.

## Content Rules

- Use canonical nouns: armory, materials, evidence, citations, model, provider, memory, local state.
- Labels are uppercase; UI-owned values are lowercase.
- Preserve identifiers, file paths, commands, model IDs, provider names, and evidence IDs exactly.
- Empty states should point to the first meaningful action.
- Error states should say what happened and what to do next.
- Trust states should name exact data flow.

## Accessibility

- Use semantic HTML and native controls on web surfaces.
- Every icon-only control needs an accessible name.
- Every form control needs an associated label.
- Focus states must be visible and not rely on color alone.
- Keep touch targets usable on mobile.
- Ensure keyboard navigation works for menus, tabs, dialogs, and command palettes.
- Use real table markup for truly tabular content.
- Provide useful alt text for meaningful images and empty alt text for decorative images.
- Do not hide essential content behind hover-only interactions.

## State Design

For each component or surface, define:

- default
- hover or highlighted when supported
- focus
- active or selected
- loading
- empty
- disabled
- error
- success or completed when applicable
- narrow width or small terminal

Do not ship only the happy path for evidence panels, materials lists, provider setup, or destructive settings.

## Evidence And Trust Components

Evidence and trust are first-class product objects.

Evidence surfaces should show:

- evidence ID or citation marker
- source path or material name
- relevant excerpt when the surface is meant for inspection
- missing/unverified state with text, not color alone

Trust surfaces should show:

- what stays local
- what is sent to hosted providers
- where local state and cache files live
- whether diagnostics are enabled
- how to change the setting or inspect state

## Motion And Feedback

- Most interactions should feel instant.
- Use motion only when it clarifies state change.
- Avoid looping or decorative animation.
- Honor `prefers-reduced-motion` on web surfaces.
- Terminal/TUI progress should be bounded and readable in logs.
- Feedback should appear near the action that caused it.

## Public API And Compatibility

Design work can still break contracts. Preserve:

- CSS custom property names when public
- documented design tokens
- screenshot-tested selectors when intentional
- TUI selector IDs and classes used by tests
- command output and machine-readable formats
- keyboard shortcuts unless intentionally migrating

When changing a public token or selector, update docs and tests in the same change.
