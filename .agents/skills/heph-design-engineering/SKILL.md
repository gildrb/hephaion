---
name: heph-design-engineering
description: Use for Heph web, brand, static site, design-system, CSS, HTML, visual UI, accessibility, responsive layout, palette, typography, forms, media, motion, CLI/TUI styling, Textual layout, or design-doc changes. Do not load for backend-only changes with no visual or interaction surface.
---

# Heph Design Engineering

Canonical front door for implementing Heph's design system in code.

Heph design engineering bridges product taste and implementation: quiet, local-first, evidence-forward interfaces built with plain technology, exact semantics, accessible controls, and no decorative excess.

## Stance

Act like a design engineer who ships production UI.

- Read the existing implementation before drawing a new component.
- Treat `design.md` and `cli-design.md` as product contracts, not mood boards.
- Use native platform behavior before custom interaction.
- Make the real product object visible: armories, materials, evidence, models, paths, citations, trust boundaries.
- Prefer dense, scannable product surfaces over marketing composition.
- Keep visual hierarchy mostly in typography, spacing, neutral color, and content structure.
- Add an abstraction only when it removes real duplication or aligns with existing local patterns.

## Decision Authority

Resolve conflicts in this order:

1. The user's explicit goal and constraints.
2. Verified Heph source, tests, and screenshots.
3. `cli-design.md` for CLI/TUI surfaces and `design.md` for web/brand surfaces.
4. This skill and its references.
5. Existing Heph implementation patterns.
6. General accessibility, web, terminal, and design-system heuristics.

If a design doc and running app disagree, inspect code and tests first, then fix the drift deliberately.

## Workflow

1. Surface map: identify web page, app shell, TUI panel, terminal output, docs page, component, form, table, evidence panel, or command palette.
2. Audience map: name whether the surface is for first-time users, daily users, contributors, agents, or scripts.
3. Source map: load the correct reference: web, TUI, core design, or verification.
4. Token map: identify color, typography, spacing, radius, elevation, and motion roles before writing CSS or Textual styles.
5. Interaction map: list keyboard, pointer, touch, focus, disabled, loading, empty, error, and success states.
6. Content map: apply Heph vocabulary and evidence/trust copy rules.
7. Verification map: inspect at desktop and mobile or narrow terminal widths, check focus, contrast, text fit, and no layout shift.

## When To Load References

| Task surface | Load |
| --- | --- |
| Any design engineering work | `references/core.md` |
| Web, brand, static pages, CSS, HTML, browser components | `references/core.md` + `references/web.md` |
| CLI/TUI styling, Textual layout, palette roles, terminal components | `references/core.md` + `references/tui.md` |
| Visual QA, accessibility, screenshots, design-doc drift | `references/verification.md` |
| Copy inside UI | `.agents/skills/heph-cli-ux/references/copy.md` when terminal/TUI, or `references/core.md` content rules when web |

## Quality Bar

Every changed interface should answer:

- What product object is visible?
- What state is current?
- What action is available?
- What evidence or trust boundary matters?
- What happens on keyboard, touch, narrow width, loading, empty, error, and disabled states?

A strong Heph interface is quiet but not vague, dense but not cramped, and precise without becoming brittle.

## Minimum Done State

A design change is not done until:

- it uses Heph tokens and semantic roles instead of ad hoc styling
- it respects the web vs CLI/TUI boundary
- text fits at expected widths
- controls have real semantics and focus states
- empty, loading, error, disabled, and success states exist where relevant
- color is not the only carrier of state
- no framework or component library was introduced without explicit product direction
- docs and implementation remain in sync, or drift is named with evidence
