# Agent Guide

Read the portfolio implementation before changing these contracts.

## Setup

- Start with `git status --short` in the portfolio checkout.
- Read the source, rendered route, and one matching skill.
- Preserve the static HTML, CSS, and vanilla JavaScript boundary.
- When reusable behavior changes, update `design.md`, its skill reference, and `scripts/check_design_docs.py`. A live-only fix is incomplete.

## Sources and checks

- Homepage source: `src/page.template.html` and `src/sections/`.
- Case writing: `content/<project>.md`; it is user-owned.
- Visual source: `src/styles/`; generated output belongs to the build scripts.
- Run `node scripts/build-page.mjs`, `node scripts/verify-page.mjs`, and `git diff --check`.
- Design docs: `python3 gildrb/scripts/check_design_docs.py --portfolio-repo <path>`.
- Render desktop and mobile when layout changes.

## Style

- Keep the homepage a text-only grouped index.
- Keep case studies authored, specific, and evidence-bound.
- Treat case-study copy as user-owned.
- Edit case-study writing only in `content/<project>.md`; never duplicate it in templates.
- Use Inter, existing colors, spacing, responsive shell, and documented type steps.
- Render authored text in `--text-primary`, labels in `--text-secondary`, actionable links in `--text-tertiary`, and hover links in `--text-primary`.
- Keep `Gil Rodrigues` at the same top-left location on every page.
- Reuse the shared sidebar partial for profile, contact, email, and theme controls.
- Case location uses two lines: `Gil Rodrigues` then `→ <Project>`; only `Gil Rodrigues` links home.
- Keep case-specific letter spacing at `0`; do not add fluid or arbitrary type.
- Do not add middle-dot separators, horizontal-rule dividers, gradients, cards, or shadows.
- Do not crop images. Use `width: 100%` and `height: auto`.
- Keep hover styles inside `@media (hover: hover)` and focus visible.
- Keep case articles in natural flow. The desktop theme-toggle boundary is a maximum endpoint for long posts, never a target that stretches short posts.

## Routes

| Task | Load |
| --- | --- |
| Homepage, project ordering, case content, or routes | `skills/gildrb-portfolio/SKILL.md` |
| CSS, typography, spacing, media, interaction, or accessibility | `skills/gildrb-design/SKILL.md` |
| Private preview, branch, PR, Vercel, merge, or production | `skills/gildrb-publishing/SKILL.md` |

## Contracts

- Homepage biography: `Designing brands, interfaces, and the systems that connect them.`
- Homepage projects are plain-text full-row links in Engineering and Design groups.
- Case-study pages retain their authored media and interactive Heph demo.
- Canonical case routes are top-level: `/<project>`.
- Legacy public routes redirect permanently; they do not remain canonical.
- Existing and user-supplied case-study prose remains verbatim unless explicitly authorized.
- Production stays unchanged until the user explicitly approves merge or promotion.

## PR Checklist

- Matching skill loaded and source read first.
- Docs, generated files, routes, and mirrors synchronized.
- Desktop and mobile render verified.
- No crop, overflow, console error, or stale asset reference.
- Protected preview confirmed before handoff.
