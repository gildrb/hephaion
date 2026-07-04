---
name: heph-design-engineering
description: Use for Heph web, brand, static site, design-system, CSS, HTML, visual UI, accessibility, responsive layout, palette, typography, forms, media, motion, CLI/TUI styling, Textual layout, or design-doc changes.
---

# Heph Design Engineering

Canonical front door for implementing Heph's design system in code.

## Stance

Act like a design engineer who ships production UI.

- Read the existing implementation before drawing a new component.
- Treat Heph design docs as product contracts, not mood boards.
- Use native platform behavior before custom interaction.
- Make the real product object visible: armories, materials, evidence, models, paths, citations, trust boundaries.
- Prefer dense, scannable product surfaces over marketing composition.
- Keep visual hierarchy mostly in typography, spacing, neutral color, and content structure.

## Decision Authority

Resolve conflicts in this order:

1. The user's explicit goal and constraints.
2. Verified Heph source, tests, and screenshots.
3. Heph design docs in the target repository.
4. `heph/AGENTS.md` and this skill.
5. Existing Heph implementation patterns.
6. General accessibility, web, terminal, and design-system heuristics.

## When To Load References

| Task surface | Load |
| --- | --- |
| Any design engineering work | `references/core.md` |
| Web, brand, static pages, CSS, HTML, browser components | `references/core.md` + `references/web.md` |
| CLI/TUI styling, Textual layout, palette roles, terminal components | `references/core.md` + `references/tui.md` |
| Visual QA, accessibility, screenshots, design-doc drift | `references/verification.md` |
| Copy inside terminal or TUI UI | `../cli-ux/references/copy.md` from `heph/skills/` context or `heph/skills/cli-ux/references/copy.md` from repository root |

## Minimum Done State

A design change is not done until it uses Heph tokens and semantic roles, respects the web versus CLI/TUI boundary, includes relevant states, keeps text fitting, and verifies accessibility and documentation drift.
