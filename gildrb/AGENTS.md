# Agent Guide

Portfolio router. Read implementation first, then these contracts.

## Setup

- Start with `git status --short` in the portfolio checkout.
- Read generation scripts, templates, CSS, and the rendered route before docs.
- Preserve the static HTML, CSS, and vanilla JavaScript boundary.
- Identify surface: homepage, case study, design system, metadata, verification, or preview.
- Load the minimum set of matching atomic skills. Each skill owns one failure class; never substitute a broad design pass.
- When a reusable behavior changes, update `design.md`, the matching skill reference, and `scripts/check_design_docs.py` in the same change. A live-only fix is incomplete.

## Sources

- `src/page.template.html`: homepage document source.
- `scripts/site-config.mjs`: canonical case-study registry.
- `content/<project>.md`: user-owned case-study writing source.
- `src/case-media/<project>/`: responsive image markup referenced by Markdown.
- `src/sections/`: homepage content sources.
- `src/<project>.template.html` and `src/data/profile.json`: case-study chrome, metadata, and structured profile source.
- `src/styles/`: ordered visual-system source.
- `scripts/build-page.mjs`: generated-page owner.
- `scripts/render-case-markdown.mjs`: Markdown-to-case-study renderer.
- `scripts/verify-page.mjs`: generated-output and asset contract.
- `vercel.json`: route, redirect, header, and deployment contract.
- Rendered desktop and mobile pages outrank prose when layout claims drift.

## Checks

- Build: `node scripts/build-page.mjs`.
- Verify: `node scripts/verify-page.mjs`.
- Public safety: `node scripts/check-public.mjs`.
- Diff: `git diff --check`.
- Metadata: validate JSON, XML, canonical URLs, feed, sitemap, and crawler mirrors.
- Browser: verify homepage and every changed case route at desktop and mobile widths.
- Images: verify full-frame aspect ratios and responsive source selection.
- Design docs: `python3 gildrb/scripts/check_design_docs.py --portfolio-repo <path>`.

## Style

- Keep the homepage a concise, text-only, sortable project index.
- Keep case studies authored, specific, and evidence-bound.
- Treat case-study copy as user-owned. Do not rewrite, replace, expand, summarize, correct, or complete it without an explicit copy request.
- Edit case-study writing only in `content/<project>.md`; never duplicate it in templates or generated HTML.
- Layout, typography, image, route, metadata, generation, and verification tasks never authorize copy edits.
- Keep requested copy suggestions outside source files until the user approves them; use only visibly unfinished `[Author: ...]` placeholders for missing prose.
- Use the existing Inter font, colors, spacing, image radius, and responsive shell.
- Render authored text in `--text-primary`, labels in `--text-secondary`, actionable text links in `--text-tertiary`, and link hover states in `--text-primary`.
- Keep `Gil Rodrigues` at the same top-left location on every page.
- Keep profile links, contact links, email action, and theme control in one shared sidebar partial used by the homepage and every case route.
- Case location uses two lines: `Gil Rodrigues` then `→ <Project>`; only `Gil Rodrigues` links home.
- Use `-0.02em` letter spacing for case titles and zero for other case-study text.
- Use documented type steps. Do not add fluid or arbitrary text sizes.
- Do not add middle-dot separators, horizontal-rule dividers, gradients, cards, or shadows.
- Do not crop images. Use `width: 100%` and `height: auto`.
- Optimize every new image and provide responsive sources.
- Keep hover styles inside `@media (hover: hover)`.
- Keep focus visible and native semantics intact.
- Keep case articles in natural document flow. The desktop theme-toggle boundary is a maximum endpoint for long posts, never a target that stretches short posts.

## Routes

| Task | Load |
| --- | --- |
| Homepage, project ordering, case content, or routes | `skills/gildrb-portfolio/SKILL.md` |
| Margins, padding, gaps, or optical rhythm | `skills/gildrb-spacing/SKILL.md` |
| Font family, size, weight, line height, or letter spacing | `skills/gildrb-typography/SKILL.md` |
| Theme tokens, semantic color, selection, contour, or surfaces | `skills/gildrb-color-audit/SKILL.md` |
| Columns, widths, shared shell, responsive order, or page geometry | `skills/gildrb-shell-layout/SKILL.md` |
| Image import, WebP, srcset, dimensions, paths, or no-crop delivery | `skills/gildrb-media/SKILL.md` |
| Hover, click, touch, theme behavior, demo behavior, or scroll state | `skills/gildrb-interaction/SKILL.md` |
| Semantics, keyboard order, focus, labels, or announcements | `skills/gildrb-accessibility/SKILL.md` |
| Rendered measurement and browser acceptance only | `skills/gildrb-visual-verification/SKILL.md` |
| Private preview, branch, PR, Vercel, merge, or production | `skills/gildrb-publishing/SKILL.md` |

## Contracts

- Homepage biography: `Independent designer and engineer building brand systems, interfaces, and digital products.`
- Homepage project rows are full-width links with Date, Title, Field, and Link columns.
- `Date`, `Title`, and `Field` are native sort buttons; the Link heading is static.
- Canonical case routes are top-level: `/<project>`.
- Legacy public routes redirect permanently; they do not remain canonical.
- Existing and user-supplied case-study prose remains verbatim unless the user explicitly authorizes copy editing.
- Production stays unchanged until the user explicitly approves merge or promotion.

## PR Checklist

- Matching skill loaded.
- Source read before docs.
- Generated files synchronized.
- Exact routes and mirrors synchronized.
- Desktop and mobile render verified.
- No crop, overflow, console error, or stale asset reference.
- Protected preview confirmed before handoff.
