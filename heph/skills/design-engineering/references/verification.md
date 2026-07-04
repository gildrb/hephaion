# Heph Design Engineering Verification

Review gates for Heph visual, web, brand, CLI, and TUI design work.

## General Design Matrix

For any design-facing change, verify:

- default, hover/highlighted, focus, selected, loading, empty, disabled, error, and success states where relevant
- keyboard-only operation
- narrow width and small viewport behavior
- text fit in buttons, nav, cards, panels, tables, status lines, and prompts
- no layout shift on hover, focus, active, or selected states
- color is not the only carrier of meaning
- semantics are real: buttons for actions, links for navigation, tables for tabular data, labels for inputs
- product objects are visible: armory, materials, evidence, model, provider, path, state
- trust boundaries are explicit where data leaves the machine

## Web Verification

When changing web surfaces, inspect mobile, tablet, and desktop widths; test keyboard navigation; verify focus rings; verify form semantics; check motion preferences; and verify CSS uses product tokens instead of ad hoc values.

## CLI/TUI Verification

When changing terminal or Textual surfaces, inspect real terminal output or TUI screenshots when feasible; verify semantic palette roles, labels, narrow terminal layout, stable selected rows, and no web radius/shadow metaphors.

## Documentation Drift

When design contracts change, update the Heph design docs in the same change or name the drift with evidence. Run focused tests for palette, terminal helpers, Textual display text, or web components touched by the change.

## Visual Review Checklist

Reject or fix changes that hide the real product object, add ad hoc styling, rely on color alone, change font weight on hover, scale font size with viewport width, use negative letter spacing, create card-in-card layouts, omit narrow behavior, obscure evidence IDs or trust boundaries, or leave design docs stale.
