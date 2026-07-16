# Verification

Verify mobile and desktop:

- location coordinate and equal text size
- title and prose computed type
- zero case letter spacing
- no horizontal overflow
- no middle dots or horizontal-rule dividers
- complete image aspect ratio
- responsive image source
- keyboard focus
- theme toggle
- home navigation
- identical profile and contact links on every route
- working email copy action on case routes
- case article before shared links on mobile
- no CSS-only reordering of focusable case navigation; the visible mobile instance follows the article in the DOM
- no repeated case-study email footer
- centered, left-aligned case intro and prose columns inside the wider media container
- centered `760px` maximum case article with all images and grids contained inside it
- tertiary case home link at rest and primary on hover
- project image navigation
- primary authored text, secondary labels, tertiary resting links, and primary link hover in both themes
- console errors
- homepage biography-to-group gap uses `--text-media-gap`, and group-to-group gap is `28px`
- homepage row padding is `8px 0` on every entry, with faint separators between adjacent rows
- `24px` between LinkedIn and Contact as the text-to-text comparison
- no visible `Portfolio` heading, while the project section retains an accessible `Portfolio` name
- homepage order is Engineering (`This website`, `Heph`) then Design (`Filen`, `n0thing`, `mL7`) in both DOM and rendered order
- homepage dates, titles, and arrows are `16px/24px`, weight `400`, aligned through the shared subgrid
- every homepage row spans the card width and remains clickable at its far-right edge
- every homepage row shows a real right-aligned arrow; case interactive media remains independently operable
- a short case page keeps its final content directly after the preceding content with no viewport-filling gap
- a long desktop case page ends at or above the theme toggle when scrolled to the bottom; the ending is never pushed down merely to align with it
- `32px` is applied once from prose to media and once from media to following prose or links on desktop and mobile
- `/heph` renders exactly one Heph demo from `src/partials/heph-demo.html`; no copied terminal markup exists
- the `/heph` order is authored prose, live Heph demo, then GitHub repository link
- submitting a question in either Heph demo produces a cited response without console errors
