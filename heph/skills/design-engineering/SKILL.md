---
name: heph-design
description: Use for web, brand, static site, design system, CSS, HTML, visual UI, accessibility, responsive layout, palette, typography, forms, media, motion, CLI/TUI styling, Textual layout, or design-doc changes.
---

# Design

Use this skill for design-system implementation in code.

## Stance

Work as a design engineer shipping production UI.

- Read existing implementation before drawing a new component.
- Treat design docs as product contracts.
- Use native platform behavior before custom interaction.
- Show product objects: armories, materials, evidence, models, paths, citations, trust boundaries.
- Prefer dense, scannable product surfaces over marketing composition.
- Keep hierarchy in typography, spacing, neutral color, and content structure.

## Authority

1. User goal and constraints.
2. Verified source, tests, and screenshots.
3. Design docs.
4. `AGENTS.md` and this skill.
5. Existing implementation patterns.
6. General accessibility, web, terminal, and design-system heuristics.

## References

| Task | Load |
| --- | --- |
| Design work | `references/core.md` |
| Web, brand, static pages, CSS, HTML, browser components | `references/core.md` + `references/web.md` |
| CLI/TUI styling, Textual layout, palette roles, terminal components | `references/core.md` + `references/tui.md` |
| Visual QA, accessibility, screenshots, design-doc drift | `references/verification.md` |
| Terminal or TUI copy | `../cli-ux/references/copy.md` |

## Done

A design change is done when it uses product tokens and semantic roles, respects web versus CLI/TUI boundaries, includes relevant states, keeps text fitting, and verifies accessibility and documentation drift.
