# Shell And Navigation

- Reuse `.wrapper`, `.layout`, `.sidebar`, `.content`, `.name`, and `.theme-toggle`.
- Reuse one shared Links and Contact partial on the homepage and every case route.
- Case routes replace only the location row; they do not fork or omit sidebar links, email behavior, or the theme control.
- Keep the location at the homepage name coordinate.
- Project location is `Gil Rodrigues → <Project>`.
- Link only `Gil Rodrigues`.
- `Gil Rodrigues` and the arrow are secondary; the current project is primary at the same size.
- Do not add Index, Back, breadcrumb components, or a tiny kicker.
- Desktop sidebar stays sticky with `64px` vertical padding.
- Mobile uses the existing two-column grid and `display: contents` collapse.
- Keep the shared sidebar content present on mobile rather than hiding it per route.
