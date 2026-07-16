# Media And Interaction

## Homepage

- The homepage is text-only: it has no images, showcase/gallery entries, or Heph demo.
- Case-study media and showcase/gallery rules remain active on case pages.
- Each `.portfolio-card-link` is one full-row navigation target containing date, title, and arrow.
- The arrow is a real `<span class="portfolio-card-arrow" aria-hidden="true">→</span>`, not a pseudo-element. A pseudo-element does not reliably repaint to white on ancestor `:hover` in this subgrid layout; a real element does.
- At rest, the link carries `--text-tertiary`, and its date and arrow use `color: inherit`; on hover-capable devices, the link's `currentColor` changes to `--text-primary`, so the whole row changes as one unit while the title stays primary.
- Keep the hover rule inside `@media (hover: hover)`. Do not add arrow transitions, transforms, background boxes, or `Read` label swaps.
- Use `.portfolio-card-link:focus-visible` with the shared `1px` primary outline and `6px` offset; focus turns the title and arrow primary.

## Case media

- Use real images with `width: 100%` and `height: auto`.
- Never use `object-fit: cover` for portfolio evidence.
- Never create crop derivatives.
- Provide responsive optimized sources without upscaling.
- Preserve intrinsic dimensions and the existing `22px` media radius.

## Heph demo

- Derive the terminal body surface with `color-mix(in srgb, var(--bg) 96%, var(--text-primary))`.
- Derive the prompt and composer row surfaces with `color-mix(in srgb, var(--bg) 94%, var(--text-primary))`.
- On mobile only, place those surfaces inside an outer frame derived with `color-mix(in srgb, var(--bg) 92%, var(--text-primary))`. The frame is lighter than the terminal in dark mode and darker than it in light mode, giving the padded boundary a legible surface without a border.
- The terminal uses no private flat colors other than the red, yellow, and green macOS window controls. Its surfaces, text, cursor, outlines, and responsive frame derive from shared theme tokens.
- Separate mixed label/value rows so each label receives its label token and each value receives its value token independently. For example, preserve the distinct tokens in `ARMORY classics`, `SCOPE 4/4`, and `EXCERPTS 4`.

- Own the Heph terminal markup once in `src/partials/heph-demo.html`. The case route includes that partial and never forks or copies the terminal markup.
- In `content/heph.md`, place `![Heph demo](media:heph-demo)` after the authored prose and immediately before the GitHub repository link. The Heph case bundle must include the shared demo data and interaction scripts so this remains the live demo, not a screenshot.
- Use primary for human-readable content, tertiary for labels and tool context, and secondary for values. Keep the traffic lights colored, but do not introduce terminal-only text grays.
- Keep showcase/gallery media full-frame, responsive, uncropped, and outside unrelated navigation targets.
- Keep hover inside `@media (hover: hover)` and focus visible.
- Keep anchors for navigation and buttons for preview actions.
- Do not add editorial divider rules, middle dots, gradients, decorative cards, or shadows.
