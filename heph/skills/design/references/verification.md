# Verification

Review gates for visual, web, brand, CLI, and TUI design work.

## Matrix

For design-facing changes, verify:

- default, hover/highlighted, focus, selected, loading, empty, disabled, error, and success states where relevant
- keyboard-only operation
- narrow width and small viewport behavior
- text fit in buttons, nav, cards, panels, tables, status lines, and prompts
- no layout shift on hover, focus, active, or selected states
- color is not the only carrier of meaning
- semantics are real: buttons for actions, links for navigation, tables for tabular data, labels for inputs
- product objects are visible: armory, materials, evidence, model, provider, path, state
- trust boundaries are explicit where data leaves the machine

## Web

Inspect mobile, tablet, and desktop widths; test keyboard navigation; verify focus rings; verify form semantics; check motion preferences; verify CSS uses product tokens.

## CLI/TUI

Inspect terminal output or TUI screenshots when feasible; verify semantic palette roles, labels, narrow layout, stable selected rows, and no web radius/shadow metaphors.

## Docs Drift

When design contracts change, update design docs in the same change or name the drift with evidence. Run focused tests for palette, terminal helpers, Textual display text, or web components touched by the change.

## Reject Or Fix

- hidden product object
- ad hoc styling
- state conveyed only by color
- font weight changes on hover
- viewport-scaled font size
- negative letter spacing
- card-in-card layouts
- missing narrow behavior
- obscured evidence IDs or trust boundaries
- stale design docs
