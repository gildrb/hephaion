# Shell And Navigation

- Reuse `.wrapper`, `.layout`, `.sidebar`, `.content`, `.name`, and `.theme-toggle`.
- Reuse one shared Links and Contact partial on the homepage and every case route.
- Case routes replace only the location row; they do not fork or omit sidebar links, email behavior, or the theme control.
- Keep the location at the homepage name coordinate.
- Project location uses two lines: `Gil Rodrigues` then `→ <Project>`.
- Reserve the same two-line location block on desktop homepage and case routes so the Links group never moves; add no extra vertical gap between those lines.
- Link only `Gil Rodrigues`.
- `Gil Rodrigues` and the arrow are tertiary; the current project is primary at the same size.
- Do not add Index, Back, breadcrumb components, or a tiny kicker.
- Desktop sidebar stays sticky with `48px` vertical padding.
- Mobile uses the existing two-column grid and `display: contents` collapse.
- On case routes, use the same shared partial for the desktop sidebar and the mobile post-article placement. Hide the inactive instance with `display: none` so DOM, focus, and visual order agree.
- Do not repeat the email as a case-study footer call to action.
- Keep the inactive home location tertiary at rest and return it to primary on hover.
