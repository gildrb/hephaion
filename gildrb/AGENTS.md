# Agent Guide

Portfolio router. Read implementation first, then these contracts.

## Setup

- Start with `git status --short` in the portfolio checkout.
- Read generation scripts, templates, CSS, and the rendered route before docs.
- Preserve the static HTML, CSS, and vanilla JavaScript boundary.
- Identify surface: homepage, case study, design system, metadata, verification, or preview.
- Load one matching skill.

## Sources

- `src/page.template.html`: homepage document source.
- `src/sections/`: homepage content sources.
- `src/filen.template.html`: first case-study reference implementation.
- `src/styles/`: ordered visual-system source.
- `scripts/build-page.mjs`: generated-page owner.
- `scripts/verify-page.mjs`: generated-output and asset contract.
- `vercel.json`: route, redirect, header, and deployment contract.
- Rendered desktop and mobile pages outrank prose when layout claims drift.

## Checks

- Build: `node scripts/build-page.mjs`.
- Verify: `node scripts/verify-page.mjs`.
- Diff: `git diff --check`.
- Metadata: validate JSON, XML, canonical URLs, feed, sitemap, and crawler mirrors.
- Browser: verify homepage and every changed case route at desktop and mobile widths.
- Images: verify full-frame aspect ratios and responsive source selection.
- Design docs: `python3 gildrb/scripts/check_design_docs.py --portfolio-repo <path>`.

## Style

- Keep the homepage image-led.
- Keep case studies authored, specific, and evidence-bound.
- Use the existing Inter font, colors, spacing, image radius, and responsive shell.
- Keep `Gil Rodrigues` at the same top-left location on every page.
- Case location is `Gil Rodrigues → <Project>`; only `Gil Rodrigues` links home.
- Use zero letter spacing in case-study-specific styles.
- Use documented type steps. Do not add fluid or arbitrary text sizes.
- Do not add middle-dot separators, horizontal-rule dividers, gradients, cards, or shadows.
- Do not crop images. Use `width: 100%` and `height: auto`.
- Optimize every new image and provide responsive sources.
- Keep hover styles inside `@media (hover: hover)`.
- Keep focus visible and native semantics intact.

## Routes

| Task | Load |
| --- | --- |
| Homepage, project ordering, case content, or routes | `skills/gildrb-portfolio/SKILL.md` |
| CSS, typography, spacing, media, interaction, or accessibility | `skills/gildrb-design/SKILL.md` |
| Private preview, branch, PR, Vercel, merge, or production | `skills/gildrb-publishing/SKILL.md` |

## Contracts

- Homepage biography: `Designing brands, interfaces, and the systems that connect them.`
- Homepage project titles are plain text unless a project contract says otherwise.
- A case-study project uses one designated clickable image on the homepage.
- Canonical case routes are top-level: `/<project>`.
- Legacy public routes redirect permanently; they do not remain canonical.
- Production stays unchanged until the user explicitly approves merge or promotion.

## PR Checklist

- Matching skill loaded.
- Source read before docs.
- Generated files synchronized.
- Exact routes and mirrors synchronized.
- Desktop and mobile render verified.
- No crop, overflow, console error, or stale asset reference.
- Protected preview confirmed before handoff.
