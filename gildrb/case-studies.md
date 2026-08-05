# Case Studies

This document defines the path from a homepage project row to an authored project page.

## Route Contract

- Use one top-level route per case study: `/<project>`.
- Generate `/<project>/index.html`.
- Link the complete homepage project row directly to `/<project>`.
- Use the same project slug in canonical metadata, social metadata, JSON-LD, sitemap, feed, machine-readable mirrors, analytics route, and verifier assertions.
- Add permanent redirects when a previously exposed route changes.

Current routes:

- `/site`
- `/t3`
- `/ben-davis`
- `/heph`
- `/filen`
- `/n0thing`
- `/curves`
- `/ml7`
- `/all`

A slug may contain a hyphen. Preserve it unchanged in the registry, route, template, content file, media directory, homepage row ID, and every metadata mirror.

Use only the current project name for the browser-tab title: `Gil Rodrigues` on `/`, `All` on `/all`, then `gildrb.com`, `T3`, `Ben Davis`, `Heph`, `Filen`, `n0thing`, `CURVES`, or `mL7` on each case route. Keep longer descriptive wording in social metadata rather than the `<title>` element.

## Homepage Entry

- Keep all projects in one global table with Date, Project, Scope, and All columns.
- Make the complete row the case-study link and give it a precise accessible name.
- Preserve exact source scopes: gildrb.com `Design Engineering`; Heph `Product/Design Engineering`; T3 and Ben Davis `Logomark`; Filen `Brand Identity`; CURVES `Typeface`; n0thing and mL7 `Wordmark`.
- `portfolio-engineering.html` and `portfolio-design.html` are ordered segments of one global list, not visible discipline categories. Insert new rows where their dates belong.
- Keep `Date`, `Project`, and `Scope` sortable across the complete list while preserving DOM, visual, and keyboard order. The All link carries the active sort to `/all`.

## Continuous Projects

- Generate `/all/index.html` from the existing homepage project rows and case-study Markdown renderer; do not duplicate project metadata or case copy.
- Start with the first case study. Do not add an introductory heading or summary.
- Build the default in `scripts/build-page.mjs`: newest first with `site` pinned last. An explicit sort in `src/scripts/60-all-sort.js` orders every article, including `site`.
- For title/scope, descending reads A→Z; scope ties break on title. Date uses its literal direction. Preserve `data-slug` on every `.all-case`.
- Separate adjacent `.all-case` articles with `var(--all-case-gap)`, exactly `24px × 1.618` (`38.832px`) from the case-title-to-text boundary.
- Reveal `View →` on direct row hover and keyboard focus without changing weight or shifting layout.
- Do not add project summaries, marketing copy, images, or category-divider wrappers to the homepage list.

## View Next

Every canonical case route receives one generated suggestion table:

```text
scripts/site-config.mjs:siteConfig.caseStudies
  - current route slug
  -> scripts/build-page.mjs
  -> <nav class="case-next" aria-label="All projects">
  -> every other project once, in homepage order
```

- Never include a self-row or self-link.
- Reuse the shared Date / Project / Scope / affordance grid contract. Tracks derive from visible content in that table; they do not copy homepage pixel widths.
- Preserve proportional dates. Mobile shows years, uses `7px` row padding, and adds the shared `10px` trailing reserve to Date and Project cells.
- Desktop `.case-next` consumes spare main-column height with `margin-top: auto`, then restores the normal `48px` boundary with `padding-top: 48px`.
- Footer bottom padding centers the final `24px` row directly with the visible theme icon. Do not apply the retired additional `4px` downward offset.
- This footer rule applies to all case pages. Validate every route at `1440×900` and `1440×2000`, including short `/ml7` with no scrolling.

## Persistent Location

Each case page starts in the exact homepage name position:
The location uses two lines: `Gil Rodrigues` then `→ <Project>`.

```text
Gil Rodrigues
→ <Project>
```

- `Gil Rodrigues` links to `/`.
- `Gil Rodrigues` and the arrow are tertiary gray; the current project is primary.
- All three parts share the same inherited `19px` size and weight.
- The project name preserves its public casing, including `mL7`.
- Do not add Index navigation.
- Do not repeat a tiny project/category kicker above the title.

## Article Order

Use this sequence when evidence supports it:

1. Decision-led title.
2. Optional factual deck.
3. Compact contribution, scope, and context metadata.
4. Primary result image.
5. Problem and constraints.
6. Exploration and rejected directions.
7. Selection reasoning.
8. Typography, color, geometry, and visual-language decisions.
9. System applications.
10. Interface or implementation details.
11. Tradeoffs, reflection, and next improvements.

Do not force a section when evidence does not exist. Add an explicit author placeholder or omit it until the user provides proof. A placeholder must be visibly unfinished, such as `[Author: explain the rejected direction]`; it must not masquerade as publishable prose.

## Markdown Authoring

- Author each case study in `content/<project>.md`; this is the only source for its visible title, deck, metadata rows, section headings, paragraphs, captions, links, lists, and code examples.
- Keep `src/<project>.template.html` structural. It contains the shell and one `<!-- @case-markdown:<project> -->` insertion token, not authored article prose.
- Keep responsive image markup in `src/case-media/<project>/<media-id>.html` so writing never requires editing `srcset`, dimensions, loading behavior, or layout HTML.
- Register each case in `scripts/site-config.mjs`; reuse shared case bundles and add route-scoped `30-<project>.css` only to that case's styles list.
- Reference assets from Markdown with `![Caption](media:<media-id>)`. Every image needs a concise, evidence-specific visible caption. Approved captions are user-owned and have no hard word-count limit. Consecutive media references form the existing two-column grid.
- Begin every file with one `#` title. Finished studies may add exactly three `- **Label:** Value` metadata rows; unfinished image-led drafts omit the entire metadata group rather than showing placeholder contribution, scope, or context values. A `>` deck may appear after the title, but authors may omit it rather than inventing introductory copy.
- Structure unfinished drafts as title, available media with concise evidence-specific captions, then `## MORE SOON` as the final block. Preserve an explicitly required project link, such as Heph's repository link, between the title and final marker.
- Generate the static route with `node scripts/build-page.mjs`; never edit `<project>/index.html` directly.
- Preserve ordinary Markdown support for `##` and `###` headings, paragraphs, lists, emphasis, strong text, inline code, external links, and fenced code blocks.
- Keep `content/README.md` synchronized with the supported authoring syntax.

## Evidence Types

Useful evidence includes:

- original sketches
- exploration boards
- rejected directions
- symbol and wordmark combinations
- scale tests
- construction grids
- spacing rules
- typography comparisons
- color studies
- app icons
- UI components
- responsive states
- motion studies
- campaign applications
- implementation excerpts
- design tokens
- documentation
- shipped interface captures

Explain what each artifact proves. Do not use images as decoration.

## Authorship Boundary

Case-study prose is author-owned. The user writes the titles, decks, captions, metadata descriptions, and article body.

- Never rewrite, replace, expand, summarize, or “improve” existing case-study copy unless the user explicitly asks for that exact operation.
- Never fill an empty section with publishable prose on the user's behalf.
- Preserve user-supplied wording verbatim when implementing it, apart from an explicitly requested correction.
- Agents may maintain document structure, insert visibly unfinished author placeholders, or identify missing and unclear sections.
- Agents may offer suggested copy only when requested. Keep suggestions separate from the source until the user approves or supplies the final wording.
- A request to change layout, typography, images, routes, metadata wiring, or generation does not authorize copy edits.
- Grammar, spelling, tone, and clarity edits also require an explicit copy-editing request.

## Writing Guidance

Use these principles only when the user explicitly requests suggestions, drafting, or copy editing. They guide review; they do not grant permission to overwrite the author's prose.

- Lead each section with the decision or problem.
- Name constraints precisely.
- Explain why rejected directions failed.
- Separate observed evidence from retrospective interpretation.
- Prefer facts over adjectives.
- Avoid `passionate`, `meaningful experiences`, `innovative`, and similar marketing language.
- Do not claim measurable outcomes without evidence.
- End with tradeoffs and what should improve next.

## T3

- Project label: `T3`.
- Route: `/t3`.
- Homepage entry: dated `T3` row tagged `Logomark`.
- Location uses two lines: `Gil Rodrigues` then `→ T3`.
- Preserve authored T3 copy verbatim unless the user explicitly requests copy editing.
- T3 is self-initiated and unadopted; never describe it as commissioned or shipped. Preserve its exploration canvas, rejected drawings, color passes, before/after refinement, and product applications.

## Ben Davis

- Project label: `Ben Davis`.
- Route: `/ben-davis`.
- Homepage entry: dated `Ben Davis` row tagged `Logomark`.
- Location uses two lines: `Gil Rodrigues` then `→ Ben Davis`.
- Ben Davis is an unsolicited redesign, not a commission. Show the previous mark with the redesign.
- Use the Ben Davis-specific bundle for sizing only. Both marks use the shared `.theme-adaptive-monochrome-artwork` capability so standalone and aggregate routes receive identical theme contrast.

## CURVES

- Project label: `CURVES`.
- Route: `/curves`.
- Homepage entry: dated `CURVES` row tagged `Typeface`.
- Location uses two lines: `Gil Rodrigues` then `→ CURVES`.
- Keep typeface evidence full-frame and uncropped. Its tall source may be sliced into sequential panels only on empty background; no panel may lose content.
- Preserve the public download and original-publication links inside the article.

## n0thing

- Project label: `n0thing`.
- Route: `/n0thing`.
- Homepage entry: dated `n0thing` row tagged `Wordmark`.
- Location uses two lines: `Gil Rodrigues` then `→ n0thing`.
- Keep the animated blinking-underscore wordmark documented in the gildrb motion inventory.

## Filen

- Project label: `Filen`.
- Route: `/filen`.
- Homepage entry: dated `Filen` row tagged `Brand Identity`.
- Required process evidence: complete exploration board.
- The board must never be cropped.
- Do not link to `filen.io` from the case page.
- Location uses two lines: `Gil Rodrigues` then `→ Filen`.

## Heph

- Project label: `Heph`.
- Route: `/heph`.
- Homepage entry: dated `Heph` row tagged `Product/Design Engineering`.
- Link the complete row to `/heph`; do not link the homepage directly to the source repository.
- Keep the interactive terminal only inside the Heph case study.
- Link `https://github.com/gildrb/heph` from inside the case-study article.
- Describe only behavior supported by the current Heph documentation and repository.
- Location uses two lines: `Gil Rodrigues` then `→ Heph`.

## mL7

- Project label: `mL7`.
- Route: `/ml7`.
- Homepage entry: dated `mL7` row tagged `Wordmark`.
- Location uses two lines: `Gil Rodrigues` then `→ mL7`.
- Reuse the Filen shell, type steps, media treatment, section spacing, shared sidebar behavior, theme behavior, and responsive layout.
- Replace only project content and evidence.
- Do not copy Filen-specific claims into mL7.
- If evidence is incomplete, write only what the visible artifacts establish and leave further sections for later evidence.

## gildrb.com

- Project label: `gildrb.com`.
- Route: `/site`.
- Homepage entry: current local date row tagged `Design Engineering`.
- Keep the authored build narrative in `content/site.md` and the route chrome in `src/site.template.html`.
- Synchronize `llms.txt`, `.well-known/llms.txt`, `humans.txt`, `sitemap.xml`, `feed.xml`, and `src/data/profile.json` whenever the public portfolio route set changes.
- Location uses two lines: `Gil Rodrigues` then `→ gildrb.com`.

## Completion

A case study is complete when its route, homepage entry, persistent location, narrative, evidence, responsive media, metadata mirrors, generated output, verifier, browser rendering, and verified Pages deployment agree.
