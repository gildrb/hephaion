# Package

Agent documentation for the gildrb portfolio.

## Quick Start

```text
Read AGENTS.md
Inspect the portfolio source and rendered route
Load the minimum set of matching atomic skills
Apply design.md and case-studies.md
Build, verify, and render the changed surface
```

## Map

```text
AGENTS.md
  product router and non-negotiable contracts

design.md
  exact visual, responsive, media, and interaction system

case-studies.md
  homepage-to-case routing, navigation, writing, and evidence contract

skills/gildrb-portfolio/
  homepage, case-study structure, content, routes, metadata, and generation

skills/gildrb-spacing/
  margins, padding, gaps, and optical rhythm only

skills/gildrb-typography/
  font metrics and type roles only

skills/gildrb-color-audit/
  semantic color and theme-token correctness only

skills/gildrb-shell-layout/
  shared columns, widths, ordering, and responsive geometry only

skills/gildrb-media/
  asset conversion, responsive sources, paths, and full-frame delivery only

skills/gildrb-interaction/
  pointer, click, lifecycle, theme, demo, and navigation behavior only

skills/gildrb-accessibility/
  semantics, keyboard, focus, names, and announcements only

skills/gildrb-visual-verification/
  read-only rendered measurement and acceptance evidence only

skills/gildrb-publishing/
  private branches, protected previews, draft PRs, merge, and production safety

scripts/check_design_docs.py
  package and live portfolio drift checker
```

## Product

The homepage is a compact, text-only, sortable project index. Internal project pages carry the authored process evidence, visual decisions, implementation details, and shipped artifacts without turning the homepage into a marketing page.

## Source

Inspect the current portfolio checkout first. Templates, generated output, tests, browser rendering, and deployment configuration are immediate truth. Update this package when a durable contract changes.

Each skill has one mission and one owned failure class. Cross-cutting work loads multiple atomic skills; no skill may absorb another skill's concern. `scripts/check_design_docs.py` rejects broad, unfinished, structurally incomplete, or stale skills.

## Safety

Keep website changes on a protected preview until the user explicitly approves merge or production promotion. Never publish private evidence, drafts, attachments, or unfinished case-study claims without authorization.
