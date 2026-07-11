---
version: "1.0.0"
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
  --text-secondary: #808080;
  --section-gap: 24px;
  --section-content-gap: 6px;
  --link-line-height: 24px;
  --theme-toggle-size: 32px;
  --sidebar-column: 280px;
  --layout-gap: 48px;
  --media-radius: 22px;
}

:root[data-theme="light"] {
  --bg: #ffffff;
  --text-primary: #000000;
  --text-secondary: #4d4d4d;
}
```

Use `--bg`, `--text-primary`, and `--text-secondary` for every new portfolio color. Do not create project color palettes, gradients, translucent panels, glow effects, or decorative fills.

## Typography

### Family

- Use self-hosted Inter Variable for headings, prose, labels, navigation, and controls.
- Keep the existing system fallbacks: `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`.
- Use Geist Mono only for code examples already using the case-study code treatment.
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

- Page title desktop: `40px`, weight `600`, line height `48px`.
- Page title mobile: `32px`, weight `600`, line height `40px`.
- Section heading: `32px`, weight `600`, line height `40px`.
- Compact heading: `20px`, weight `600`, line height `28px`.
- Prose and deck: `16px`, weight `400`, line height `24px`.
- Metadata label and caption: `14px`, weight `400`, line height `20px`.
- Code: `14px`, weight `400`, line height `20px`.

Do not use `clamp()` for case-study type. Do not invent intermediate values such as `15px`, `17px`, `19px` outside the existing shell, `28px` display copy, or viewport-scaled headings.

## Spacing

Use the existing 4px-derived rhythm and homepage constants.

- Compact gap: `4px`.
- Small gap: `8px`.
- Text group gap: `12px` or `16px`.
- Image/grid gap: `20px`.
- Related group gap: `24px` or `32px`.
- Major internal gap: `48px` or `64px`.
- Desktop section gap: `120px`.
- Mobile section gap: `80px`.
- Desktop wrapper padding: `48px`.
- Wrapper padding below `1400px`: `32px`.
- Current mobile wrapper padding: `12px`.

Do not add arbitrary values when an existing step expresses the relationship. Width constraints may use content-specific maxima; spacing still follows this scale.

## Shell

### Desktop

- Wrapper maximum width: `1900px`.
- Wrapper centers with auto inline margins.
- Layout uses a `280px` sidebar and flexible content column.
- Layout gap is `48px`, reduced to `32px` below `1400px`.
- Sidebar is sticky at `top: 0`, height `100vh`, with `64px` vertical padding.
- The same sidebar content persists on the homepage and every case-study route: location, Links group, Contact group, email action, Signal link, and theme control.
- Keep the Links and Contact markup in one shared source partial. Case templates must include it instead of maintaining route-specific copies.
- The homepage location is `Gil Rodrigues`; case routes replace only that location row with `Gil Rodrigues → <Project>`.
- Main content uses `64px` vertical padding.
- `Gil Rodrigues` begins at the same wrapper coordinate on every route.

### Mobile

- At `768px` and below, the layout becomes a two-column grid: content plus `32px` theme-control column.
- Wrapper uses `12px` inline padding.
- Layout uses `32px` vertical padding.
- Sidebar and content use `display: contents` so the same elements enter the shared mobile grid.
- Do not hide or silently remove the shared Links or Contact groups on case-study routes.
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
Gil Rodrigues → Filen
Gil Rodrigues → mL7
```

Rules:

- Keep the location in the exact `.name` position used by the homepage.
- Render the full location at `19px` with inherited line height and weight.
- Link only `Gil Rodrigues` to `/` and render it in `--text-secondary`.
- Render the arrow in `--text-secondary`.
- Render the current project in `--text-primary` so the active location is the strongest part of the row.
- Current project text is not a link.
- Use an arrow, not a middle dot, slash, breadcrumb chevron component, or Index button.
- Do not add separate `Index`, `Back`, or `Return to index` navigation.
- Keep the theme toggle in its existing location.

## Homepage

- Keep biography first and concise.
- Approved biography: `Designing brands, interfaces, and the systems that connect them.`
- Keep project titles plain text unless explicitly specified.
- A project with a case study exposes one designated clickable image.
- Do not append `Read the case study`, `View project`, summaries, tags, roles, or marketing copy.
- The designated image uses the same image-wrapper shape as the gallery.
- Clicking the designated image navigates; it does not open the image preview.
- Other image-preview buttons retain preview behavior when they remain on the homepage.

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
- Keep intrinsic `width` and `height` attributes to prevent layout shift.
- Use `loading="lazy"` below the first viewport.
- Use `decoding="async"` for raster media.
- Use eager loading and high fetch priority only for the route’s primary first-view image.

### Shape

- Reuse `--media-radius: 22px` for portfolio images.
- Do not introduce case-study card radii.
- Code examples may use the documented `8px` radius.
- Do not add shadows, outlines, or frames around ordinary images.

## Case Layout

- Reuse `.wrapper`, `.layout`, `.sidebar`, `.content`, `.name`, and `.theme-toggle`.
- Keep article copy left-aligned within the content column.
- Copy, intro, and footer maximum width: `720px`.
- Deck maximum width: `680px`.
- Code maximum width: `880px`.
- Full media spans the available content column.
- Two-image comparisons use two equal columns and the existing `20px` gap.
- At mobile width, media grids collapse to one column.
- Keep major sections at `120px` desktop and `80px` mobile spacing.

## Dividers

- Do not use middle-dot separators.
- Do not add `<hr>`.
- Do not add horizontal rules between intro, metadata, sections, or footer.
- Do not add `border-top` or `border-bottom` as editorial dividers.
- Code blocks may keep their own enclosing border because it defines the code surface rather than separating sections.
- Use whitespace, heading hierarchy, and text color for section boundaries.

## Interaction

- Links navigate. Buttons act.
- Image preview controls remain native buttons.
- Case-study entry images remain native anchors.
- Labels use `--text-secondary`. This includes `Links`, `Contact`, `References`, `About`, project titles, metadata terms, captions, and other text that names a group or field without acting.
- Actionable text links use `--text-primary` at rest. This includes profile links, reference links, email, and case-study footer links.
- The case-study home link is the location exception: it remains `--text-secondary` beside the secondary arrow while the current project is `--text-primary`.
- Text-link hover uses `--text-secondary`; it never becomes brighter than its resting state.
- Link arrows inherit the link color so the complete link changes as one unit.
- Icon controls use `--text-primary` at rest and `--text-secondary` on hover unless a documented component state requires otherwise.
- Image-entry hover may continue to use opacity because its navigation target is communicated by the linked image rather than text color.
- Hover changes color or image opacity without changing size or weight.
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

- Use concrete facts and decisions.
- Describe problem, constraints, alternatives, selection logic, implementation, tradeoffs, and next improvements.
- Do not invent research, outcomes, metrics, authorship, or technical responsibility.
- Use captions to explain why evidence matters.
- Keep homepage copy short. Put detailed narrative inside the case route.
- Keep case-study prose readable and direct.

## Metadata

- Canonical project routes are top-level: `/filen`, `/ml7`, and future `/<project>` paths.
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
15. Confirm labels are secondary, actionable text links are primary at rest, and text-link hover is secondary in both themes.
16. Confirm every generated route contains the same shared profile and contact links, and that email copy works on case pages.

Reject a change that introduces crop, arbitrary type sizes, negative case letter spacing, a second navigation system, editorial divider rules, stale generated output, broken metadata, or an unprotected unfinished preview.
