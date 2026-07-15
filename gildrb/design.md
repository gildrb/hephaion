---
version: "1.1.0"
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

## Intent

- Keep the homepage an image-led index.
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
  --link-line-height: 24px;
  --theme-toggle-size: 32px;
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
- Use Geist Mono only for code examples already using the case-study code treatment.
- Keep case-study code examples flat: no border, fill, radius, or shadow. Use Geist Mono with horizontal scrolling for wide source. Syntax highlighting is palette-only: keys, properties, table headers, and keywords use `--text-primary`; strings, values, numbers, and hex values use `--text-secondary`; comments, punctuation, and operators use `--text-tertiary`. Add no hues or color tokens.
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

Case-specific letter spacing is always `0`. Do not use negative letter spacing.

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
- Homepage project-entry gap: `32px` at every viewport; this optically compensates text-to-media boundaries against the `24px` text-to-text sidebar group gap.
- Case-study section gap: `80px` at every viewport.
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
- Main content uses `48px` vertical padding.
- `Gil Rodrigues` begins at the same wrapper coordinate on every route.

### Mobile

- At `768px` and below, the layout becomes a two-column grid: content plus `32px` theme-control column.
- Wrapper uses `12px` inline padding.
- Layout uses `32px` vertical padding.
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
- Current project text is not a link.
- Use an arrow, not a middle dot, slash, breadcrumb chevron component, or Index button.
- Do not add separate `Index`, `Back`, or `Return to index` navigation.
- Keep the theme toggle in its existing location.
- Preserve each route's per-tab scroll position for browser back and forward navigation. Store on `pagehide` and when the document becomes hidden, restore only for back/forward or bfcache traversal, and tolerate unavailable `sessionStorage`. Fresh visits must retain their normal initial position.
- On desktop case-study routes, keep authored content in its natural document flow. Reserve bottom padding derived from the shared footer and theme-toggle tokens so a long post's final authored line, whether prose or `MORE SOON`, cannot end below the theme toggle when the reader reaches the bottom. Never stretch a short post or push its final content downward to manufacture that alignment. Keep the mobile toggle in its top-mounted position.
- Treat that desktop boundary as a maximum endpoint, not a target baseline. Article `min-height`, flex distribution, `margin-top: auto`, and last-child top padding are forbidden ending mechanisms.
- Own the live Heph terminal once in `src/partials/heph-demo.html` and include it on both the homepage and `/heph`. The Heph case order is authored prose, the shared live demo, then the GitHub repository link.
- Separate authored thoughts with ordinary Markdown paragraph breaks. Use the shared `--text-media-gap` (`32px`) in both directions around case media: from preceding prose to the image, and from the caption to following prose. This mirrors the homepage's optical LinkedIn-to-Contact transition without introducing a heading or divider.

## Homepage

- Keep biography first and concise.
- Derive the Heph terminal surface with `color-mix(in srgb, var(--bg) 96%, var(--text-primary))` and its prompt/composer rows with `color-mix(in srgb, var(--bg) 94%, var(--text-primary))`. These remain the two internal terminal surfaces.
- On mobile only, place those surfaces inside an outer frame derived with `color-mix(in srgb, var(--bg) 92%, var(--text-primary))`. This frame is outside the terminal: it is lighter than the terminal in dark mode and darker than it in light mode, making the padded boundary legible without a border.
- Inside the Heph terminal, primary prompts, answers, and input use `--text-primary`; labels use `--text-tertiary`; values use `--text-secondary`.
- Wrap mixed label/value rows such as `ARMORY classics`, `SCOPE 4/4`, `EXCERPTS 4`, and command hints so the label and value receive their correct shared tokens independently.
- Keep tool output and the complete `materials: ... Details: /evidence.` source line in `--text-tertiary`.
- The terminal may contain no private flat colors other than the red, yellow, and green macOS window controls; its two surfaces, text, cursor, outlines, and responsive frame derive from shared tokens.
- Order homepage projects newest to oldest: `Heph`, `Filen`, `n0thing`, then `mL7`. DOM, visual, and keyboard order must agree at every viewport.
- Keep the homepage content and every project image inside the same centered `760px` content boundary used by case studies.
- Approved biography: `Designing brands, interfaces, and the systems that connect them.`
- Render the approved biography in `--text-primary`; it is authored content, not a label.
- Do not show a `Portfolio` heading on the homepage; keep `Portfolio` only as the accessible name of the project section.
- Use `32px` from the biography to the first project title on desktop and `32px` from that title to its solid media. On mobile, keep the intervening biography, Links, and project-title text groups at `24px`, then use `32px` from the project title to its media.
- Put each project date and title below its media, never inside a mobile media or demo frame.
- Render project dates at `14px/20px` in `--text-tertiary` and project titles at `16px/24px` in `--text-secondary`.
- Make every below-media metadata strip a full-width link target. Keep the date on its own row, then align the project title left and an Inter `→` right on the same row.
- For interactive media such as the Heph terminal, keep the media controls usable and enlarge only the metadata link beneath it; do not place an external-link overlay over the demo.
- Use the same optically compensated `32px` gap between every adjacent homepage project entry on desktop and mobile.
- Use the same `32px` gap from the final project title to the `Metadata` group; never pull the footer upward with a negative margin.
- A project with a case study exposes one designated clickable image.
- Do not append `Read the case study`, `View project`, summaries, tags, roles, or marketing copy.
- The designated image uses the same image-wrapper shape as the gallery.
- Clicking the designated image navigates; it does not open the image preview.
- Keep the homepage free of detached personal-image preview sections.

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
- Do not add `border-top` or `border-bottom` as editorial dividers.
- Code blocks use the same flat, borderless treatment as the surrounding page.
- Use whitespace, heading hierarchy, and text color for section boundaries.

## Interaction

- Links navigate. Buttons act.
- Image preview controls remain native buttons.
- Case-study entry images remain native anchors.
- The homepage biography uses `--text-primary`; case decks, paragraphs, and list items use `--text-secondary` for a quieter reading layer below white headings.
- Labels use `--text-secondary`. This includes `Links`, `Contact`, `Metadata`, `About`, project titles, and other text that names a group or field without acting.
- Dates, case metadata terms, and image captions use `--text-tertiary`.
- Actionable text links use `--text-tertiary` at rest. This includes profile links, reference links, and email.
- The case-study home link remains `--text-tertiary` beside the tertiary arrow while the current project is `--text-primary`.
- On hover-capable devices, the case-study home link becomes `--text-primary` to make the return action explicit.
- Text-link hover uses `--text-primary`, promoting an actionable item from light gray to white in dark mode.
- Link arrows inherit the link color so the complete link changes as one unit.
- Icon controls use `--text-tertiary` at rest and `--text-primary` on hover unless a documented component state requires otherwise.
- Clickable project media uses a normally blended `--highlight-bg` layer at `0.55` opacity. This reuses the exact approved bright gray and pulls black and white artwork toward it without placing interface copy over the artwork.
- While a project card is hovered or keyboard-focused, change its existing right-aligned metadata arrow from `→` to `Read →`. Keep `Read` beside the existing arrow and outside the image.
- Apply the same `Read →` state to Heph's metadata-only link when its title row is hovered or keyboard-focused.
- Use the same primary-color `1px` outline and `4px` offset for Heph's metadata-only keyboard focus as for image cards. Keep the enclosing `.heph-demo` overflow visible so all four sides of that outline remain unclipped.
- Reserve enough width for `Read →` in the resting metadata grid so revealing it never shifts the project title or arrow.
- Wrap the image in `.portfolio-card-image`; keep the full native anchor interactive without an overlay.
- Preserve the existing focus outline without adding a tint.
- Do not place interaction labels over the image, and do not use opacity-only image dimming or colored tints for case-study entries.
- Hover changes color without changing size or weight.
- Put hover behavior inside `@media (hover: hover)`.
- Use `:focus-visible` with a visible primary-color outline.
- Do not leave clicked controls visually selected.
- Theme changes apply immediately without broad transitions.
- Tolerate `localStorage` failures.

## Motion

- Prefer no motion for navigation, theme changes, email copy, and image entry links.
- Keep interaction motion at `200ms` or below when motion materially improves orientation.
- Respect `prefers-reduced-motion`.
- Do not add looping decorative animation.

## Accessibility

- Use one semantic page heading.
- Use real heading order for case sections.
- Give icon-only buttons explicit accessible names.
- Give meaningful images specific alt text.
- Use empty alt text only for decorative images.
- Keep link purpose clear without relying on hover.
- Preserve keyboard access for home navigation, theme control, project images, email, and preview buttons.
- Ensure focus is visible in both themes.
- Keep page width free of horizontal overflow at `390px`.
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

- Canonical project routes are top-level: `/heph`, `/filen`, `/n0thing`, `/ml7`, and future `/<project>` paths.
- The homepage Heph metadata links to `/heph`. Its GitHub repository link belongs inside the Heph article, not on the homepage.
- Use static directory indexes: `<project>/index.html`.
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
7. Confirm one designated homepage link per case project.
8. Confirm complete image aspect ratios.
9. Confirm responsive source selection.
10. Confirm no middle dots or rule dividers.
11. Confirm no horizontal overflow.
12. Confirm theme switching and home navigation.
13. Check browser console errors.
14. Confirm preview protection before sharing.
15. Confirm authored text is primary, labels are secondary, actionable text links are tertiary at rest, and text-link hover is primary in both themes.
16. Confirm every generated route contains the same shared profile and contact links, and that email copy works on case pages.
17. Confirm case studies do not repeat an email footer and that shared Links and Contact follow the article on mobile.
18. Measure every adjacent homepage project transition and the final project-to-`Metadata` transition at desktop and mobile widths; each must resolve to `32px` while the text-to-text sidebar group gap remains `24px`.
19. Confirm mobile demo metadata is outside the styled media frame and remains exposed to assistive technology.

Reject a change that introduces crop, arbitrary type sizes, negative case letter spacing, a second navigation system, editorial divider rules, stale generated output, broken metadata, or an unprotected unfinished preview.
