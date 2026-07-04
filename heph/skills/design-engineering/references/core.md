# Core

Reusable rules for web, brand, CLI, and TUI surfaces.

## Traits

Surfaces should be:

- private
- precise
- quiet
- local-first
- evidence-forward
- fast
- easy to scan

Avoid decorative color, gradient hero shortcuts, glass effects, oversized marketing cards, stock-feeling visuals, and ornamental animation. Show materials, evidence, armory, and trust boundary.

## Sources

Use the right contract:

- CLI design docs: terminal cells, Textual CSS, ANSI styles, one-line status bars, fixed-width side panels, TUI copy density.
- Web design docs: browser layout, responsive spacing, radius, media, native forms, focus states, static web stack, brand expression.
- Source and tests: immediate truth when docs drift.

Do not copy terminal cell dimensions into responsive web layout. Do not copy web radius, cards, or shadows into terminal surfaces.

## Implementation

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

## Evidence, Trust

Evidence and trust need visible UI state.

Evidence surfaces should show evidence ID or citation marker, source path or material name, relevant excerpt when inspection is intended, and missing/unverified state with text.

Trust surfaces should show what stays local, what is sent to hosted providers, where local state and cache files live, whether diagnostics are enabled, and how to change or inspect the setting.
