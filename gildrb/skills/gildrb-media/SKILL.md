---
name: gildrb-media
description: Prepare and wire gildrb media only. Use for importing local images, WebP conversion, responsive derivatives, srcset and sizes, intrinsic dimensions, loading priority, image partials, full-frame rendering, alt text supplied by the user, or asset-reference verification. Do not use for copywriting, page spacing, typography, colors, shell layout, or interaction behavior.
---

# Gildrb Media

## Mission

Publish complete, uncropped, optimized evidence with deterministic responsive delivery.

## Owns

- Raster conversion and responsive derivatives.
- Asset paths, image partials, `src`, `srcset`, `sizes`, intrinsic dimensions, loading, and decoding.
- Preservation of source aspect ratio and frame completeness.

## Excludes

- Do not write or rewrite captions, alt text, prose, titles, or metadata. Preserve supplied wording verbatim.
- Do not change spacing, type, colors, page geometry, hover behavior, or project routing.
- Media-grid column geometry belongs to `gildrb-shell-layout`; media boundary rhythm belongs to `gildrb-spacing`.

## Fixed Contract

- Keep real `<img>` elements with `display:block`, `width:100%`, `height:auto`.
- Never use `object-fit:cover`, content-hiding `object-position`, crop derivatives, or upscaling.
- Convert new raster evidence to WebP unless animation or transparency requires another format.
- Generate only widths supported by the original, normally `480`, `720`, `960`, `1280`, `1600`.
- Strip unnecessary metadata and retain intrinsic `width`/`height` attributes.
- Use `loading="lazy"` and `decoding="async"` below the first viewport.
- Use eager/high priority only for the route's first-view primary image.
- Full-width sizes: `(max-width: 768px) calc(100vw - 24px), (max-width: 1100px) calc(100vw - 336px), 760px`.
- Two-column sources use the documented `370px` cap and `calc(50vw - 178px)` intermediate width.
- Markdown references use `media:<slug>` and resolve through `src/case-media/<project>/`.
- Keep captions between one and five words only when the user supplied or explicitly authorized them.

## Procedure

1. Inspect original format, dimensions, alpha, animation, and orientation.
2. Locate the route's existing media naming and partial convention.
3. Generate deterministic derivatives without upscaling or cropping.
4. Wire one media partial and replace absolute/local Markdown paths with `media:<slug>`.
5. Preserve authored text byte-for-byte outside the path substitution.
6. Build, then inspect selected current source and natural/displayed aspect ratios at desktop and mobile.

## Reject

- Missing original content at any edge.
- A derivative larger than its source.
- Absolute filesystem paths in published Markdown or HTML.
- Missing intrinsic dimensions or stale asset references.
- Caption or prose invention under an optimization request.

## Verify

Run the build, repository verifier, and `git diff --check`. Confirm every generated asset exists, no orphaned derivative was added, browser-selected sources fit the viewport, natural and displayed aspect ratios match within rounding, and there is no layout shift or overflow.

## Done

All referenced media is optimized, responsive, full-frame, path-safe, and verified without changing authored language or unrelated design.
