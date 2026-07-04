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

When changing web surfaces:

- inspect at mobile, tablet, and desktop widths
- test keyboard navigation through controls, dialogs, menus, tabs, and command palettes
- verify focus rings are visible and not clipped
- verify forms submit naturally and labels focus controls
- verify dark theme and light theme when both are supported
- verify no framework, router, component library, or build-step drift unless intentional
- verify images have correct alt behavior
- verify `prefers-reduced-motion`
- verify CSS uses tokens instead of ad hoc values
- verify cards are not nested inside cards
- verify sections are not fake floating cards

## CLI/TUI Verification

When changing terminal or Textual surfaces:

- inspect real terminal output or TUI screenshots when feasible
- verify semantic palette roles, not hardcoded colors
- verify labels uppercase and value preservation rules
- verify narrow terminal layout
- verify no web radius, shadow, line-height, or card metaphors leaked into terminal code
- verify focus and selected rows do not resize content
- verify status bars stay one-cell where contracted
- verify screen reader or plain-text fallbacks when relevant

## Documentation Drift

When design contracts change:

- update `design.md` for browser/brand surfaces
- update `cli-design.md` for CLI/TUI surfaces
- update source comments only when they clarify non-obvious behavior
- run or request `uv run python -m scripts.check_design_docs` in the Heph repo
- run focused tests for palette, terminal helpers, Textual display text, or web components touched by the change

If checks cannot run, report why and name the files that need follow-up.

## Visual Review Checklist

Reject or fix changes that:

- use decorative gradients, glassmorphism, glow fields, or stock-like composition for core product UI
- hide the real product object behind abstract marketing copy
- add ad hoc hex values to render code
- rely on color alone for enabled, disabled, selected, missing, or error state
- change font weight on hover/focus/selected state
- scale font size with viewport width in product UI
- use negative letter spacing
- create card-in-card layouts
- ship custom controls without native semantics and keyboard behavior
- omit mobile or narrow-terminal behavior
- obscure evidence IDs, paths, commands, or trust boundaries
- leave design docs stale after changing tokens or semantic roles

## Screenshot Guidance

For substantial visual work, capture screenshots or terminal transcripts for:

- default state
- empty state
- error state
- selected/focused state
- narrow width
- mobile web width when applicable
- dark and light theme when applicable

Review screenshots for overlap, clipped text, invisible focus, excessive whitespace, accidental one-color palette, and decorative UI that distracts from armory/material/evidence work.
