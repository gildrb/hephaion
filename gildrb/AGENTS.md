# Agent Guide

Portfolio router. Read implementation first, then these contracts.

## Setup

- Start with `git status --short` in the portfolio checkout.
- Read generation scripts, templates, CSS, Functions, deployment controls, and the rendered route before docs.
- Preserve static HTML, CSS, and vanilla JavaScript with bounded Cloudflare Pages Functions.
- Identify surface: homepage, case study, design system, motion, metadata, agent discovery, verification, or publishing.
- Load the minimum matching atomic skills. Each skill owns one failure class.
- When reusable behavior changes, update `design.md` or `platform.md`, the owning skill reference, and `scripts/check_design_docs.py`. A live-only fix is incomplete.

## Sources

- `src/page.template.html`: homepage document source.
- `scripts/site-config.mjs`: canonical case registry and bundle order.
- `content/<project>.md`: user-owned case-study writing.
- `src/case-media/<project>/`: responsive media markup.
- `src/sections/`, `src/partials/`, `src/styles/`, `src/scripts/`: shared interface source.
- `scripts/build-page.mjs`: generated-page owner.
- `scripts/verify-page.mjs`, `scripts/verify-agent-readiness.mjs`: output contracts.
- `functions/`, `_headers`, `_redirects`, `_routes.json`: Cloudflare runtime contract.
- `.well-known/`, `openapi.json`, `api-docs.md`, `auth.md`: public agent contracts.
- Rendered desktop/mobile pages and validated production behavior outrank prose when claims drift.

## Checks

- Build: `npm run build`.
- Verify: `npm run verify`.
- Public safety: `node scripts/check-public.mjs`.
- Diff: `git diff --check`.
- Local Pages: `npx wrangler pages dev public`.
- Design docs: `python3 gildrb/scripts/check_design_docs.py --portfolio-repo <path>`.
- Browser: verify homepage and changed routes at desktop/mobile widths, reduced motion, console, and relevant machine endpoints.

## Style

- Keep the homepage a concise, text-only, sortable project index.
- Treat case-study copy as user-owned. Never change it without an explicit copy request.
- Edit case writing only in `content/<project>.md`; never in templates or generated HTML.
- Reuse Inter, semantic colors, spacing, radius, responsive shell, and documented motion.
- Keep `Gil Rodrigues` at the same top-left location on every page.
- Use one shared sidebar partial for profile links, contact, email, and theme control.
- Do not add middle dots, editorial rules, gradients, cards, shadows, crop, or arbitrary type sizes.
- Keep hover inside `@media (hover: hover)` and focus visibly operable.
- Optimize new media and preserve source aspect ratio.

## Routes

| Task | Load |
| --- | --- |
| Homepage, case content, routes, metadata, generation | `skills/gildrb-portfolio/SKILL.md` |
| Margins, padding, gaps, optical rhythm | `skills/gildrb-spacing/SKILL.md` |
| Font metrics and type roles | `skills/gildrb-typography/SKILL.md` |
| Semantic colors and theme tokens | `skills/gildrb-color-audit/SKILL.md` |
| Shell widths, columns, order, responsive geometry | `skills/gildrb-shell-layout/SKILL.md` |
| Media encoding, responsive sources, no-crop delivery | `skills/gildrb-media/SKILL.md` |
| State logic, hover, click, touch, theme, scroll | `skills/gildrb-interaction/SKILL.md` |
| Animation, transitions, easing, reduced motion | `skills/gildrb-motion/SKILL.md` |
| Semantics, keyboard, focus, names, announcements | `skills/gildrb-accessibility/SKILL.md` |
| Rendered measurement and browser evidence | `skills/gildrb-visual-verification/SKILL.md` |
| Git-backed Cloudflare preview, production, propagation, rollback | `skills/gildrb-publishing/SKILL.md` |

## Contracts

- Biography: `Brand designer based in Germany, building identity systems for software.`
- Homepage rows are full-width Date / Project / Scope / All links and controls.
- Canonical cases are top-level routes; `/all` is the continuous sequence.
- Case location uses two lines: `Gil Rodrigues` then `→ <Project>`.
- Legacy public routes redirect permanently.
- Approved homepage motion is the exact `gildrb-motion` entry contract.
- Public agent APIs remain truthful, read-only, bounded, and unauthenticated.
- Production stays unchanged until explicit user approval.
- Production is Git-backed: push the exact approved commit, then require the Pages deployment `Source` to match it.
- Direct Upload is exceptional and must never leave production ahead of `origin/main`.

## PR Checklist

- Matching skills loaded; source read before docs.
- Generated files, routes, mirrors, and Functions synchronized.
- Build, verifiers, public safety, and package drift checker pass.
- Desktop, mobile, reduced motion, and changed machine contracts verified.
- No crop, overflow, console error, stale asset, secret, or private evidence.
- Exact commit and Pages deployment recorded before production handoff.
