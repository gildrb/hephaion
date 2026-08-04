---
version: "1.3.0"
name: "gildrb"
description: "Visual and interaction contract for the gildrb portfolio and project case studies."
default_theme: "dark"
web_stack:
  document: "HTML"
  styling: "CSS"
  behavior: "vanilla JavaScript"
  build_step: "static generation only"
  frameworks: "none"
  component_libraries: "none"
  routing: "static directory indexes"
  font: "Inter Variable"
---

# Design

This document defines the visible portfolio system. It covers the homepage, project case studies, shared navigation, typography, media, interaction, responsive behavior, accessibility, and verification.

## Authority

Use sources in this order:

1. Explicit user instruction.
2. Rendered approved portfolio behavior.
3. Portfolio templates, CSS, scripts, and verifier.
4. This document and `case-studies.md`.
5. Product skills.
6. General design heuristics.

Do not preserve a documented rule when current approved source intentionally replaced it. Update the package instead.

## Atomic Skill Architecture

Design work is routed by failure class. No broad design skill exists.

| Failure class | Sole owner |
| --- | --- |
| Margins, padding, gaps, optical rhythm | `gildrb-spacing` |
| Font metrics and type roles | `gildrb-typography` |
| Semantic tokens and theme color correctness | `gildrb-color-audit` |
| Shell columns, widths, ordering, and responsive geometry | `gildrb-shell-layout` |
| Asset conversion, responsive sources, and full-frame delivery | `gildrb-media` |
| Pointer, click, lifecycle, theme, demo, and navigation behavior | `gildrb-interaction` |
| Semantics, keyboard, focus, accessible names, and announcements | `gildrb-accessibility` |
| Read-only rendered measurement and acceptance evidence | `gildrb-visual-verification` |

Load every atomic skill required by a cross-cutting task, but let each skill change only its owned concern. Each skill must declare `Mission`, `Owns`, `Excludes`, `Fixed Contract` or `Required Matrix`, `Procedure`, `Reject`, `Verify`, and `Done`. The package checker rejects the retired `gildrb-design` skill, missing sections, ambiguous ownership, TODO text, or stale router entries.

## Intent

- Keep the homepage a concise, text-only, sortable project index.
- Let project evidence carry the claim.
- Keep navigation stable across routes.
- Make case studies read as part of the portfolio, not a separate magazine.
- Use typography, whitespace, media scale, and neutral color for hierarchy.
- Avoid marketing-page components and decorative systems.
- Show complete evidence. Do not crop process images.

## Stack

```toml
[web]
document = "HTML"
styling = "CSS"
behavior = "vanilla JavaScript"
framework = "none"
component_library = "none"
router = "static directory index"
bundler = "none"
deployment = "static files on Vercel"
```

Do not add React, Next.js, Vue, Svelte, Astro, Tailwind, Sass, TypeScript, a component library, a router, or a content framework without an explicit architecture change.

## Tokens

The live portfolio token names remain authoritative.

```css
:root {
  --bg: #000000;
  --text-primary: #ffffff;
  --text-secondary: #b3b3b3;
  --text-tertiary: #767676;
  --highlight-bg: #b3b3b3;
  --highlight-text: #ffffff;
  --section-gap: 24px;
  --section-content-gap: 6px;
  --text-media-gap: 32px;
  --case-title-text-gap: 24px;
  --all-case-gap: calc(var(--case-title-text-gap) * 1.618);
  --link-line-height: 24px;
  --theme-toggle-size: 32px;
  --theme-toggle-optical-offset: 2px;
  --sidebar-column: 240px;
  --content-column: 760px;
  --layout-gap: 48px;
  --media-radius: 22px;
}

:root[data-theme="light"] {
  --bg: #ffffff;
  --text-primary: #000000;
  --text-secondary: #4d4d4d;
  --text-tertiary: #767676;
}
```

Use `--bg`, `--text-primary`, `--text-secondary`, and `--text-tertiary` for resting portfolio colors. Primary is authored content, secondary is labels and supporting metadata, and tertiary is inactive or actionable navigation. `--highlight-bg` reuses the approved bright gray for temporary image and text-selection highlighting; `--highlight-text` keeps selected text white in every theme. Do not create project color palettes, gradients, translucent panels, glow effects, or decorative fills.
Text selection uses `--highlight-text` over `--highlight-bg`; do not restore the outdated tertiary-gray selection background.

## Typography

### Family

- Use self-hosted Inter Variable for headings, prose, labels, navigation, and controls.
- Keep the existing system fallbacks: `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`.
- Use Ioskeley Mono only for code examples already using the case-study code treatment.
- Case-study headings use the compact `###` treatment and its `19px/28px` step. Do not use `##` section wrappers in case studies.
- Keep case-code `pre` in pure `"Ioskeley Mono", monospace`; wrap arrow glyphs in an explicit `.case-code-arrow` span using `"Inter", sans-serif` so they match the breadcrumb and card arrows.
- Do not change the global font family for one case study.

### Rendering

- Keep `-webkit-font-smoothing: antialiased`.
- Keep `-moz-osx-font-smoothing: grayscale`.
- Keep `-webkit-text-size-adjust: 100%`.
- Keep `text-rendering: optimizeLegibility`.
- Do not use weights below `400`.
- Keep weight stable on hover, focus, active, and selected states.

### Portfolio shell

- Name and persistent project location: `19px`, weight `400`.
- Navigation, biography, labels, project titles, links, and default controls: `16px`, weight `400`.
- Link line height: `24px`.
- Preserve the homepage shell values. Do not restyle them in project CSS.

### Case-study steps

Case titles use `-0.02em` letter spacing. Other case-study text uses `0`; do not add negative spacing to those roles.

- Page title desktop: `28px`, weight `500`, line height `36px`.
- Page title mobile: `24px`, weight `500`, line height `32px`.
- Section heading: `24px`, weight `500`, line height `32px`.
- Compact heading: `19px`, weight `500`, line height `28px`.
- Prose and deck: `16px`, weight `400`, line height `24px`.
- Metadata label and caption: `14px`, weight `400`, line height `20px`.
- Stack case metadata as three rows in a two-column definition grid: a shared `104px` label column and one flexible value column with a `24px` gap. On mobile use `88px` and `16px`. Labels and values share a top baseline so copy length cannot unbalance the group.
- Keep every visible case-media caption between one and five words.
- Code: `14px`, weight `400`, line height `20px`.

On desktop, the top edge of the page title must align with the top edge of `Gil Rodrigues` in the persistent location. Use zero top margin on the title; do not compensate by moving the article or sidebar independently.

Do not use `clamp()` for case-study type. Do not invent intermediate values such as `15px` or `17px`, or viewport-scaled headings. The existing `19px` shell location is also the compact-heading step; `28px` is reserved for desktop page titles.

## Spacing

Use the existing 4px-derived rhythm and homepage constants.

- Compact gap: `4px`.
- Small gap: `8px`.
- Text group gap: `12px` or `16px`.
- Image/grid gap: `20px`.
- Related group gap: `24px` or `32px`.
- Major internal gap: `48px` or `64px`.
- Homepage biography-to-table gap: `32px`.
- Homepage table header and row vertical padding: `8px`; adjacent rows remain contiguous.
- Homepage table column gap: `16px` on desktop and `clamp(8px, 3vw, 16px)` on mobile.
- Case-study section gap: `80px` at every viewport.
- Case-title-to-text gap: `var(--case-title-text-gap)`, exactly `24px`.
- Continuous `/all` case gap: `var(--all-case-gap)`, exactly `24px × 1.618` (`38.832px`). It derives from the established case-title-to-text boundary; apply it once between adjacent `.all-case` articles.
- Desktop wrapper padding: `48px`.
- Wrapper padding below `1400px`: `32px`.
- Current mobile wrapper padding: `12px`.

Do not add arbitrary values when an existing step expresses the relationship. Width constraints may use content-specific maxima; spacing still follows this scale.

## Shell

### Desktop

- Wrapper maximum width: `1900px`.
- Wrapper centers with auto inline margins.
- Layout uses a `240px` sidebar and a `760px` content column. This preserves the previous combined column width while transferring `40px` from navigation to reading space.
- At `1100px` and below, the sidebar is `240px`; with `32px` wrapper padding and a `32px` gap, the available content width is `calc(100vw - 336px)`.
- Center the complete desktop composition—sidebar, gap, and content—as one unit so the outer whitespace is equal.
- Layout gap is `48px`, reduced to `32px` below `1400px`.
- Sidebar is sticky at `top: 0`, height `100vh`, with `48px` vertical padding.
- The same sidebar content persists on the homepage and every case-study route: location, Links group, Contact group, email action, Signal link, and theme control.
- On desktop, reserve two `24px` location lines before the shared `24px` section gap so the Links group begins at the same coordinate on homepage and case routes.
- Keep the Links and Contact markup in one shared source partial. Case templates must include it instead of maintaining route-specific copies.
- The homepage location is `Gil Rodrigues`; case routes replace only that location row with a two-line `Gil Rodrigues` then `→ <Project>` location.
- Main content uses shared `48px` vertical padding declared once in `src/styles/10-base.css`, which every homepage and case-study bundle loads. This keeps the desktop content top, case title, and `Gil Rodrigues` at the same `48px` coordinate; mobile resets `.content` padding to `0` inside the responsive shell.
- `Gil Rodrigues` begins at the same wrapper coordinate on every route.

### Mobile

- At `767px` and below, the layout becomes a two-column grid: content plus `32px` theme-control column.
- Wrapper uses `12px` inline padding.
- The mobile layout container has no vertical padding. The name supplies `24px` top and `8px` bottom padding. On the homepage, every case-study route, and `/all`, the shared name and theme control use the same sticky `56px` row at `top: 0` in both themes and center both icon sizes inside their content areas so switching cannot move or resize the button. The name uses the existing case-page `linear-gradient(to bottom, var(--bg) 60%, transparent)` treatment; do not add a separate homepage backdrop. It shifts that shared icon center `2px` lower with `--theme-toggle-optical-offset`, using `26px` top and `6px` bottom padding for optical alignment with the first `Gil Rodrigues` line. `.content` uses `display: contents` with `0` padding.
- Sidebar and content use `display: contents` so the same elements enter the shared mobile grid.
- On case-study routes, keep the desktop Links and Contact group in the sidebar. On mobile, render the article immediately after the location row and place the mobile instance of that same shared partial after the article so DOM, focus, and visual order agree.
- The mobile grid still requires article order `5` and shared navigation order `6`: `display: contents` exposes both sets of descendants to the wrapper grid, so these values preserve the same order already established in the DOM rather than contradicting it.
- Do not hide or silently remove the shared Links or Contact groups; change only their mobile order.
- Persistent location occupies column one and order one.
- Theme toggle occupies column two and order one.
- Main article occupies both columns after the location row.
- Do not add a second page header above or below this shell.

## Persistent Location

Homepage:

```text
Gil Rodrigues
```

Project page:

```text
Gil Rodrigues
→ Filen

Gil Rodrigues
→ mL7
```

Rules:

- Keep the location in the exact `.name` position used by the homepage.
- Render the full location at `19px` with inherited line height and weight.
- Link only `Gil Rodrigues` to `/` and render it in `--text-tertiary`.
- Render the arrow in `--text-tertiary`.
- Render the current project in `--text-primary` so the active location is the strongest part of the row.
- Use no additional vertical gap between the two location lines; the inherited line height provides their separation.
- Link the current project text to `#top` and keep it in `--text-primary`; only the `Gil Rodrigues` link leaves the page for `/`.
- Use an arrow, not a middle dot, slash, breadcrumb chevron component, or Index button.
- Do not add separate `Index`, `Back`, or `Return to index` navigation.
- Keep the theme toggle in its existing location.
- Preserve each route's per-tab scroll position for browser back and forward navigation. Store on `pagehide` and when the document becomes hidden, restore only for back/forward or bfcache traversal, and tolerate unavailable `sessionStorage`. Fresh visits must retain their normal initial position.
- On desktop case-study routes, keep authored content in its natural document flow. Reserve bottom padding derived from the shared footer and theme-toggle tokens so a long post's final authored line, whether prose or `MORE SOON`, cannot end below the theme toggle when the reader reaches the bottom. Never stretch a short post or push its final content downward to manufacture that alignment. Keep the mobile toggle in its top-mounted position.
- Treat that desktop boundary as a maximum endpoint, not a target baseline. Article `min-height`, flex distribution, `margin-top: auto`, and last-child top padding are forbidden ending mechanisms.
- Own the live Heph terminal once in `src/partials/heph-demo.html` and include it only on `/heph`. The Heph case order is authored prose, the live demo, then the GitHub repository link.
- Separate authored thoughts with ordinary Markdown paragraph breaks. Use the shared `--text-media-gap` (`32px`) in both directions around case media: from preceding prose to the image, and from the caption to following prose. This mirrors the homepage's optical LinkedIn-to-Contact transition without introducing a heading or divider.

## Homepage

- Keep biography first and concise.
- Keep the homepage free of project images, previews, and the Heph terminal; all project evidence belongs inside case-study routes.
- Order homepage projects newest to oldest by default: `gildrb.com`, `Heph`, `Filen`, `n0thing`, then `mL7`. DOM, visual, and keyboard order must agree at every viewport.
- Place one `Date` / `Project` / `Scope` / `All` header row before the single global project list. Render all four labels in explicit Inter `16px/24px` and `--text-secondary` on the same four-column subgrid as the project rows; `All` is a right-aligned link to `/all` that includes the active sort state.
- Size the desktop Project and Scope tracks to their longest content. Use the existing `16px` column gap between `gildrb.com`, the longest project title, and Scope. Use `Design Engineering`, `Product/Design Engineering`, `Brand Identity`, and `Wordmark` exactly as authored in the current rows. Render scope values at `16px/24px` in `--text-tertiary`.
- On mobile, `.portfolio-scroll-frame` owns the `max-content max-content minmax(0, 1fr) auto` tracks with `clamp(8px, 3vw, 16px)` column gaps. The header row and `.portfolio-section` both subgrid into that frame so their Date, Project, Scope, and arrow columns share one geometry. Keep the width query container on the frame, where it swaps full dates for years at the documented threshold. Keep the table at Inter `16px/24px`, hide `View`, and truncate long Scope values with an ellipsis so the row never creates page overflow.
- Treat the header and five project rows as one compact table block. The first project row begins immediately below the header rule with no section gap or category-divider space.
- On desktop, align the header row's text line box exactly with the sidebar `Links` label line box. Do not add top padding that drops `Date`, `Project`, `Scope`, or `All` below it.
- Keep `Date`, `Project`, and `Scope` as native buttons. The first inactive Date sort is newest-first; Project and Scope begin A–Z. Repeated activation toggles direction. Apply the chosen ordering across the complete homepage project list, update DOM order as well as visual order, announce the result, expose the active direction accessibly, preserve focus after keyboard activation, and keep this behavior off case-study routes. Do not retain category wrappers that prevent a true global order.
- Do not underline `Date`, `Project`, or `Scope` on hover. They follow the site's existing restrained control language and may not introduce a bespoke text-decoration hover exception.
- Keep the homepage content and project table inside the same centered `760px` content boundary used by case studies.
- Approved biography: `Brand designer based in Germany, building identity systems for software.`
- Render the approved biography in `--text-primary`; it is authored content, not a label.
- Do not show a `Portfolio` heading on the homepage; keep `Portfolio` only as the accessible name of the project section.
- Use `32px` from the biography to the project table. Keep the header rule and all five rows contiguous with `8px` vertical padding and faint `12%` primary separators.
- Render project dates and scopes at `16px/24px` in `--text-tertiary`; render project titles at `16px/24px` in `--text-primary`.
- Make every project row a full-width link target. Align date, project, scope, and the Inter `View →` affordance on the shared four-column subgrid.
- On mobile, measure the Links/Contact grid's second-column start from the first body-row Scope cell, falling back to the first case-page `View next` Scope cell and then the header Scope cell. Store that offset in `--mobile-contact-start`; routes without a column table, such as `/all`, retain the `3fr 4fr` ratio fallback.
- Reveal `View` immediately left of the arrow only while the row is directly hovered or keyboard-focused. Hide `View` at `767px` and below so touch layouts retain all data columns without overflow.

### Case-study Read Next

Every generated case-study route ends with a build-generated `View next` block in the same content column as the article. It mirrors the homepage row conventions: date, project, scope, and `View →`, without the homepage header or `All` column.

- Use existing tokens only: `--text-primary`, `--text-tertiary`, 16px/24px type, and the existing case-section rhythm.
- Keep 48px between the article's final block and `View next`, matching the existing compact-heading (`###`) top margin. On desktop, remove the article's final-line boundary padding when this block follows; the heading remains in normal document flow.
- On mobile, keep `var(--section-gap)` between the table container and the Links/Contact block on both the homepage and case routes. The 48px article-to-`View next` gap is a separate boundary.
- On desktop, apply the existing footer/theme-toggle endpoint calculation to the case table container's bottom padding and keep the final row unpadded. At maximum scroll, the final row bottom aligns with the theme-toggle bottom while preserving the content column's 48px bottom padding. This is a maximum endpoint only; short pages remain natural flow.
- On the mobile homepage, lock the viewport to the dynamic viewport and keep the project rows in the only scrolling region. The filter row stays outside that region and does not move during row overscroll. Show the existing conditional top and bottom edge fades only when rows remain above or below the current scroll position, and suppress the inner scrollbar so it does not overlap the arrow column. The Links and Contact block remains reachable below the locked table; document pull-to-refresh is intentionally unavailable for this interaction.
- Use the homepage row padding and faint primary separators. Render every project as a real anchor, including the current project with its own href and `aria-current="page"`.
- Keep every row visible in homepage default order. Do not add sort buttons, an `All` column, randomization, visited state, or client JavaScript for this table.
- Do not force the desktop theme-toggle endpoint under the eight-row table. Keep the 48px content-column bottom padding. On mobile, let the homepage grow naturally with every project row and the footer in one document flow.
- On the mobile homepage, keep the shared sticky name and theme toggle at the same top offset as case routes and `/all` while Links/Contact follows the locked table. Keyboard and screen-reader access must still traverse every project row even though touch scrolling belongs to the table region.
- Keep the block text-only. Do not add cards, borders, gradients, new colors, or arbitrary sizes.
- Reveal `View` on hover and keyboard focus using the homepage interaction convention; keep focus visible.
- At mobile widths, preserve the date, project, scope, and arrow columns and hide only the `View` label, as on the homepage.
- The rows and metadata are build-time HTML. The table must not load client JavaScript.
- `/all` starts immediately with the generated case studies. It adds no introduction, duplicates no authored case content, and orders its `.all-case` articles from the `sort` and `direction` URL parameters. Its generated default order always places the homepage-derived `site` entry last; an explicit sort request orders every article, `site` included.
- Keep the homepage Metadata footer only on `/` and only on desktop. It lists `humans.txt`, `llms.txt`, and a `source` link to the site's public repository as a vertical `--section-content-gap` stack; it contains no copyright line.
- Hide the complete Metadata footer at `767px` and below, and do not add it to case-study or `/all` routes.
- Do not append summaries, roles, marketing copy, or detached personal-image preview sections.

## Heph Case Demo

- Derive the terminal surface with `color-mix(in srgb, var(--bg) 96%, var(--text-primary))` and its prompt/composer rows with `color-mix(in srgb, var(--bg) 94%, var(--text-primary))`.
- On mobile, place those surfaces inside an outer frame derived with `color-mix(in srgb, var(--bg) 92%, var(--text-primary))`; use no border to manufacture that boundary.
- Primary prompts, answers, and input use `--text-primary`; labels use `--text-tertiary`; values use `--text-secondary`.
- Wrap mixed label/value rows such as `ARMORY classics`, `SCOPE 4/4`, `EXCERPTS 4`, and command hints so each role receives the correct token.
- Keep tool output and the complete `materials: ... Details: /evidence.` source line in `--text-tertiary`.
- Allow no private flat colors other than the red, yellow, and green macOS window controls.
- Keep the demo's shared markup and scripts off the homepage and every non-Heph route.

## Media

### Full frame

- Use a real `<img>`.
- Use `display: block`.
- Use `width: 100%`.
- Use `height: auto`.
- Do not use `object-fit: cover`.
- Do not use `object-position` to hide content.
- Do not create cropped derivatives.
- Preserve the source aspect ratio within normal browser rounding.

### Vector marks

- Ship a monochrome brand mark as an SVG file referenced from a normal `<img>`, not as a raster derivative. Vector marks are the one exception to WebP conversion.
- Author the file with white fills, then invert it for light contexts with `filter: brightness(0)`; dark contexts keep `filter: none`.
- Cover all three theme states: `@media (prefers-color-scheme: light)` scoped to `:root:not([data-theme])` for the system default, plus explicit `:root[data-theme="light"]` and `:root[data-theme="dark"]` rules.
- Keep those rules in a route-scoped `src/styles/30-<project>.css` registered only in that case study's `styles` array. A mark class belongs to one route: `.heph-lockup` to `/heph`, `.ben-davis-brandmark` to `/ben-davis`.
- Give marks `border-radius: 0` and no contour. The `--media-radius` contour belongs to raster evidence.
- Keep the intrinsic `width` and `height` attributes from the SVG viewBox so the mark reserves its box like every other image.

### Optimization

- Convert new photographic or raster evidence to WebP unless animation or transparency requires another format.
- Provide responsive widths appropriate to the source, normally `480`, `720`, `960`, `1280`, and `1600` when the original supports them.
- Never upscale beyond the source width.
- Strip unnecessary metadata.
- Use `srcset` and `sizes` so mobile avoids desktop payloads.
- Full-width media uses `(max-width: 768px) calc(100vw - 24px), (max-width: 1100px) calc(100vw - 336px), 760px`; two-column media uses the matching `370px` cap and `calc(50vw - 178px)` intermediate width.
- Keep intrinsic `width` and `height` attributes to prevent layout shift.
- Use `loading="lazy"` below the first viewport.
- Use `decoding="async"` for raster media.
- Use eager loading and high fetch priority only for the route’s primary first-view image.

### Shape

- Reuse `--media-radius: 22px` for portfolio images.
- Give portfolio images a subtle `1px` contour mixed from `--text-primary` at `14%` so black and white media boundaries remain visible in both themes.
- On mobile, apply demo padding, background, and radius to a media-only frame; keep date/title metadata as a sibling below it.
- Do not introduce case-study card radii.
- Code examples may use the documented `8px` radius.
- Do not add shadows or decorative frames around ordinary images.

## Case Layout

- Reuse `.wrapper`, `.layout`, `.sidebar`, `.content`, `.name`, and `.theme-toggle`.
- Keep article copy left-aligned within the content column.
- Copy and intro maximum width: `760px`.
- Center the intro and every prose block within the available case-study content column with auto inline margins. Keep the text itself left-aligned; “centered” describes the reading column, not centered typography.
- Deck maximum width: `680px`.
- Case article maximum width: `760px`, centered within the available content column. This is the outer blog-width boundary for headings, media, grids, and code.
- Code maximum width: `880px`.
- Full media spans the same `760px` case article as the prose, never the entire post-sidebar viewport.
- Two-image comparisons use two equal columns and the existing `20px` gap.
- At mobile width, media grids collapse to one column.
- Keep major sections at `80px` desktop and mobile spacing.

## Dividers

- Do not use middle-dot separators.
- Do not add `<hr>`.
- Do not add horizontal rules between intro, metadata, sections, or footer.
- Do not add `border-top` or `border-bottom` as editorial dividers. The homepage table's faint row separators are structural table rules, not article dividers.
- Code blocks may keep their own enclosing border because it defines the code surface rather than separating sections.
- Use whitespace, heading hierarchy, and text color for section boundaries.

## Interaction

- Links navigate. Buttons act.
- Homepage project rows remain native anchors; Date, Project, and Scope remain native buttons. All is a link to `/all` with the active sort state.
- The homepage biography uses `--text-primary`; case decks, paragraphs, and list items use `--text-secondary` for a quieter reading layer below white headings.
- Labels use `--text-secondary`. This includes `Links`, `Contact`, `Metadata`, `About`, and other non-actionable group labels.
- Homepage project titles use `--text-primary`; dates, scopes, case metadata terms, and image captions use `--text-tertiary`.
- Actionable text links use `--text-tertiary` at rest. This includes profile links, reference links, and email.
- The case-study home link remains `--text-tertiary` beside the tertiary arrow while the current project is `--text-primary`.
- On hover-capable devices, the case-study home link becomes `--text-primary` to make the return action explicit.
- Text-link hover uses `--text-primary`, promoting an actionable item from light gray to white in dark mode.
- Link arrows inherit the link color so the complete link changes as one unit.
- Icon controls use `--text-tertiary` at rest and `--text-primary` on hover unless a documented component state requires otherwise.
- While a project row is hovered or keyboard-focused, reveal `View →` in the reserved rightmost affordance column.
- Use a primary-color `1px` outline with `6px` offset for full-row keyboard focus.
- Hide `View` on touch-width layouts; keep the Inter arrow visible.
- Hover changes color without changing size or weight.
- Put hover behavior inside `@media (hover: hover)`.
- Use `:focus-visible` with a visible primary-color outline.
- Do not leave clicked controls visually selected.
- Theme changes apply immediately without broad transitions.
- Tolerate `localStorage` failures.

## Motion

- Prefer no motion for navigation, sorting, theme changes, email copy, and project-row links.
- Keep interaction motion at `200ms` or below when motion materially improves orientation.
- Respect `prefers-reduced-motion`.
- Do not add looping decorative animation.

### Homepage entry

The homepage runs exactly one entry animation, on first paint. It is the documented exception to the `200ms` interaction limit. Case routes never animate on entry.

- Hide the homepage body while `html.homepage-first-paint-pending` is present so no unstyled, unmeasured, or wrong-theme frame is ever shown. Keep `.name` and `.profile-summary` visible throughout.
- `10-core.js` resolves `window.homepageFirstPaintReady` after the theme, `Inter`, homepage dates, and the mobile column layout are settled; `12-homepage-entry.js` then sets `data-homepage-first-paint-ready` and removes the pending class.
- Reveal with `homepage-enter` from `opacity: 0` and a `-4px` vertical offset: `700ms` for the sidebar sequence, `1s` for the project table.
- Stagger the table as a diagonal wave. One row down or one column right adds `80ms`, expressed as `--row-delay` and `--column-delay`.
- End the sequence on the last contact link's `animationend`, with a `2800ms` timeout fallback, then set `data-homepage-entry-complete` and stop owning opacity.
- Under `prefers-reduced-motion: reduce`, skip every entry animation and reveal the finished page immediately.
- Never gate first paint on work that can fail silently. The pending class must be removed on every path, including the fallback.

## Accessibility

- Use one semantic page heading.
- Use real heading order for case sections.
- Give icon-only buttons explicit accessible names.
- Give meaningful images specific alt text.
- Use empty alt text only for decorative images.
- Keep link purpose clear without relying on hover.
- Preserve keyboard access for home navigation, theme control, sort buttons, project rows, email, and the Heph case demo.
- Ensure focus is visible in both themes.
- Keep page width free of horizontal overflow at `320px` and `390px`.
- Do not use color as the only state signal.

## Content

- Case-study prose is user-owned. Visual-system work must preserve titles, decks, captions, metadata descriptions, and body copy verbatim unless the user explicitly requests copy work.
- Layout, typography, images, routes, metadata wiring, generation, and verification do not imply permission to alter wording.
- Keep requested writing suggestions outside source files until approved. Missing prose may use only visibly unfinished `[Author: ...]` placeholders.
- Use concrete facts and decisions.
- Describe problem, constraints, alternatives, selection logic, implementation, tradeoffs, and next improvements.
- Do not invent research, outcomes, metrics, authorship, or technical responsibility.
- Use captions to explain why evidence matters.
- Keep homepage copy short. Put detailed narrative inside the case route.
- Keep case-study prose readable and direct.

## Metadata

- Canonical project routes are top-level: `/site`, `/t3`, `/ben-davis`, `/heph`, `/filen`, `/n0thing`, `/curves`, `/ml7`, `/all`, and future `/<project>` paths. Slugs may be hyphenated and are used verbatim everywhere.
- The homepage Heph row links to `/heph`. Its GitHub repository link belongs inside the Heph article, not on the homepage.
- Use static directory indexes: `<project>/index.html` and `all/index.html`.
- Synchronize canonical, Open Graph, Twitter, JSON-LD, sitemap, feed, Markdown mirrors, LLM mirrors, humans file, and structured profile graph.
- Redirect superseded public routes permanently to the canonical route.
- Do not retain a duplicate canonical page at the old path.

## Verification

For every design change:

1. Build generated pages.
2. Run the repository verifier.
3. Validate JSON and XML artifacts.
4. Check `git diff --check`.
5. Render desktop and mobile.
6. Confirm persistent location coordinates and font equality.
7. Confirm one full-width homepage row link per configured project.
8. Confirm Date, Project, and Scope sort the complete list, All preserves that state in its `/all` URL, and each ordering is announced.
9. Confirm `/all` uses `--all-case-gap`, derived as the `24px` case-title-to-text gap multiplied by `1.618`, between generated articles at desktop and mobile widths.
10. Confirm complete case-image aspect ratios and responsive source selection.
11. Confirm no middle dots or rule dividers.
12. Confirm no horizontal overflow.
13. Confirm theme switching and home navigation.
14. Check browser console errors.
15. Confirm preview protection before sharing.
16. Confirm authored text is primary, labels are secondary, actionable text links are tertiary at rest, and text-link hover is primary in both themes.
17. Confirm every generated route contains the same shared profile and contact links, and that email copy works on case pages.
18. Confirm case studies do not repeat an email footer and that shared Links and Contact follow the article on mobile.
19. Measure homepage table alignment and overflow at desktop, `390px`, and `320px`; the header and rows remain one contiguous block.
20. Confirm the Heph demo appears only on `/heph` and remains exposed to assistive technology.
21. Confirm each theme-inverting SVG mark renders light-on-dark and dark-on-light under the system preference and under both explicit themes, and that its class appears on no other route.
22. Confirm the homepage reveals once, in staggered order, with no unstyled or wrong-theme frame, and that reduced motion skips the sequence.

Reject a change that introduces crop, arbitrary type sizes, negative letter spacing outside the case-title role, a second navigation system, editorial divider rules, stale generated output, broken metadata, or an unprotected unfinished preview.
