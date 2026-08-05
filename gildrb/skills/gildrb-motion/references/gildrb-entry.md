# Gildrb Entry

## Status

This is the approved homepage entry animation for `gildrb.com`. Preserve its visible character and exact timing unless the user explicitly requests a new motion direction.

Implementation source:

```text
src/styles/15-homepage-entry.css
```

Bundle owner:

```text
scripts/site-config.mjs → siteConfig.homepage.styles
```

The animation was approved after direct visual review. It replaced both a static page and an earlier slower implementation that used a JavaScript readiness sequence and a full-page visibility gate.

## Visual Intent

The sequence establishes three layers:

1. **Immediate identity:** `Gil Rodrigues` and the About biography are present at first paint.
2. **Context reveal:** Links and the portfolio frame resolve from soft blur and transparency.
3. **Evidence sequence:** Individual links, the table header, and project rows rise and fade in with a short stagger.

The page never presents an empty loading state. Identity gives the viewer an immediate anchor while the secondary information arrives. The overlap between container fade and child rise creates the depth: groups become legible as a surface while their children resolve as ordered items.

## Exact Source

```css
@keyframes homepage-fade {
  from {
    opacity: 0;
    filter: blur(6px);
  }

  to {
    opacity: 1;
    filter: blur(0);
  }
}

@keyframes homepage-rise {
  from {
    opacity: 0;
    transform: translateY(12px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media screen and (prefers-reduced-motion: no-preference) {
  html:not([data-homepage-entry-complete]) .links,
  html:not([data-homepage-entry-complete]) .portfolio-scroll-frame {
    animation: homepage-fade 700ms cubic-bezier(0.16, 1, 0.3, 1) both;
    animation-delay: 80ms;
  }

  html:not([data-homepage-entry-complete]) .links > *,
  html:not([data-homepage-entry-complete]) .portfolio-table-header,
  html:not([data-homepage-entry-complete])
    .portfolio-list
    > .portfolio-card-link {
    animation: homepage-rise 900ms cubic-bezier(0.16, 1, 0.3, 1) both;
    animation-delay: var(--homepage-entry-delay, 120ms);
  }

  .links > :nth-child(2) {
    --homepage-entry-delay: 170ms;
  }

  .links > :nth-child(3) {
    --homepage-entry-delay: 220ms;
  }

  .links > :nth-child(4) {
    --homepage-entry-delay: 270ms;
  }

  .links > :nth-child(5) {
    --homepage-entry-delay: 320ms;
  }

  .links > :nth-child(6) {
    --homepage-entry-delay: 370ms;
  }

  .links > :nth-child(7) {
    --homepage-entry-delay: 420ms;
  }

  .links > :nth-child(8) {
    --homepage-entry-delay: 470ms;
  }

  .links > :nth-child(9) {
    --homepage-entry-delay: 520ms;
  }

  .links > :nth-child(10) {
    --homepage-entry-delay: 570ms;
  }

  .portfolio-table-header {
    --homepage-entry-delay: 120ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(1) {
    --homepage-entry-delay: 165ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(2) {
    --homepage-entry-delay: 210ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(3) {
    --homepage-entry-delay: 255ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(4) {
    --homepage-entry-delay: 300ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(5) {
    --homepage-entry-delay: 345ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(6) {
    --homepage-entry-delay: 390ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(7) {
    --homepage-entry-delay: 435ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(8) {
    --homepage-entry-delay: 480ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(9) {
    --homepage-entry-delay: 525ms;
  }

  .portfolio-list > .portfolio-card-link:nth-child(10) {
    --homepage-entry-delay: 570ms;
  }

  /* Mobile orders Links and Contact by visual row, not DOM column. */
  @media (max-width: 767px) {
    html:not([data-homepage-entry-complete]) .links {
      animation-delay: 480ms;
    }

    .links > :nth-child(1),
    .links > :nth-child(7) {
      --homepage-entry-delay: 525ms;
    }

    .links > :nth-child(2),
    .links > :nth-child(8) {
      --homepage-entry-delay: 570ms;
    }

    .links > :nth-child(3),
    .links > :nth-child(9) {
      --homepage-entry-delay: 615ms;
    }

    .links > :nth-child(4),
    .links > :nth-child(10) {
      --homepage-entry-delay: 660ms;
    }

    .links > :nth-child(5) {
      --homepage-entry-delay: 705ms;
    }

    .links > :nth-child(6) {
      --homepage-entry-delay: 750ms;
    }
  }
}
```

Do not minify the authored source into opaque shorthand. The explicit delay map is a reviewable choreography contract.

## Timing Model

All animations use:

```css
cubic-bezier(0.16, 1, 0.3, 1)
```

This curve moves quickly away from the initial state, then decelerates for a controlled landing. It gives the rise a spring-like finish without JavaScript spring integration, overshoot, or bounce.

### Containers

| Target | Start | Duration | End | Initial state |
| --- | ---: | ---: | ---: | --- |
| `.links` desktop | 80ms | 700ms | 780ms | opacity 0, blur 6px |
| `.links` mobile | 480ms | 700ms | 1180ms | opacity 0, blur 6px |
| `.portfolio-scroll-frame` | 80ms | 700ms | 780ms | opacity 0, blur 6px |

### Desktop link children

| Child | Start | Duration | End |
| ---: | ---: | ---: | ---: |
| 1 | 120ms | 900ms | 1020ms |
| 2 | 170ms | 900ms | 1070ms |
| 3 | 220ms | 900ms | 1120ms |
| 4 | 270ms | 900ms | 1170ms |
| 5 | 320ms | 900ms | 1220ms |
| 6 | 370ms | 900ms | 1270ms |
| 7 | 420ms | 900ms | 1320ms |
| 8 | 470ms | 900ms | 1370ms |
| 9 | 520ms | 900ms | 1420ms |
| 10 | 570ms | 900ms | 1470ms |

The desktop `50ms` interval is legible as a sequence without making the sidebar feel typed or mechanically stepped.

### Mobile Links and Contact visual rows

Mobile places Links and Contact in two visual columns. DOM siblings in the same visual row share a delay:

| Visual row | DOM children | Start | Duration | End |
| ---: | --- | ---: | ---: | ---: |
| 1 | 1 and 7 | 525ms | 900ms | 1425ms |
| 2 | 2 and 8 | 570ms | 900ms | 1470ms |
| 3 | 3 and 9 | 615ms | 900ms | 1515ms |
| 4 | 4 and 10 | 660ms | 900ms | 1560ms |
| 5 | 5 | 705ms | 900ms | 1605ms |
| 6 | 6 | 750ms | 900ms | 1650ms |

Do not apply desktop DOM-order delays to mobile. It makes the right Contact column appear out of visual sequence. Desktop declarations remain unchanged.

### Portfolio children

| Target | Start | Duration | End |
| --- | ---: | ---: | ---: |
| Header | 120ms | 900ms | 1020ms |
| Row 1 | 165ms | 900ms | 1065ms |
| Row 2 | 210ms | 900ms | 1110ms |
| Row 3 | 255ms | 900ms | 1155ms |
| Row 4 | 300ms | 900ms | 1200ms |
| Row 5 | 345ms | 900ms | 1245ms |
| Row 6 | 390ms | 900ms | 1290ms |
| Row 7 | 435ms | 900ms | 1335ms |
| Row 8 | 480ms | 900ms | 1380ms |
| Row 9 | 525ms | 900ms | 1425ms |
| Row 10 | 570ms | 900ms | 1470ms |

The `45ms` row interval makes the denser table read as one flowing surface. It is slightly tighter than the sidebar interval because the rows are spatially adjacent and visually uniform.

## Why Each Value Exists

### `6px` blur

Enough to make the group arrival perceptible without turning text into a large glowing field. A stronger blur increases raster/compositing cost and makes the first half of the fade feel muddy.

### `12px` travel

Visible at desktop and mobile sizes while remaining subordinate to the static layout. The earlier `4px` experiment felt static. The external inspiration used `16px`; `12px` retained the rise while fitting gildrb's denser table.

### `700ms` container fade

Long enough to read as refinement rather than a flash. It completes before the last child, so the viewer stops perceiving the group as blurred while later rows finish settling.

### `900ms` child rise

The curve front-loads movement, so the sequence feels responsive despite the nominal duration. The long tail provides the smooth landing that made the approved version feel refined.

### `80ms` group delay

Preserves one clear frame where identity and biography establish orientation before secondary content begins.

### Bounded final starts

Desktop's last child starts at `570ms` and completes at `1470ms`. Mobile's last visual row starts at `750ms` and completes at `1650ms`. Extending either bound makes lower content feel unavailable rather than intentionally sequenced.

## Selector Architecture

Animate groups and children separately.

- Group fade supplies atmosphere and shared arrival.
- Child rise supplies order and directional movement.
- Nested opacity is intentional. It creates a softer early phase than either animation alone.
- `.name` and `.profile-summary` are deliberately absent from all selectors.
- `.portfolio-scroll-frame` owns the shared table surface; individual header and rows own order.
- Each `.portfolio-card-link` moves as one row. Do not animate its four cells independently; that creates too many simultaneous layers and weakens row cohesion.
- `html:not([data-homepage-entry-complete])` owns every animated target. The first sort sets that terminal marker before copying values into stable row slots.
- Desktop Links use DOM order. Mobile Links/Contact pair siblings by visual row and use their own delay map; do not change desktop timing to solve mobile order.

The style file belongs only in the homepage bundle. Case-study routes must not inherit this entry sequence.

## Runtime Architecture

Use CSS for animation. Sorting JavaScript may only set the terminal `data-homepage-entry-complete` marker before its local value update; it does not schedule or drive entry frames.

Do not add:

- Framer Motion;
- GSAP;
- a framework;
- a page-entry JavaScript file;
- `window.load` coordination;
- font readiness promises;
- body visibility classes;
- local/session storage entry flags;
- persistent `will-change` declarations.

The CSS is inline in the generated homepage head, so initial animation styles exist before the selected body elements are parsed. There is no flash from a late-loaded animation stylesheet.

If CSS animation is unsupported, the declarations are ignored and normal final styles remain. If JavaScript fails, the entry still runs because it has no script dependency.

## Accessibility

The entire implementation is inside:

```css
@media screen and (prefers-reduced-motion: no-preference)
```

Reduced-motion users receive the normal final layout immediately. No separate override is needed because the initial opacity, blur, and transform exist only inside the media query.

Semantic HTML, focus order, hit targets, and accessible names exist before and during animation. Do not disable pointer events or keyboard focus while elements are transitioning.

## Replay Contract

Run on a fresh document presentation.

Do not intentionally replay when:

- a user sorts Date, Project, or Scope;
- the theme changes;
- email copy feedback changes;
- focus enters a row;
- the browser restores the document from bfcache;
- a local DOM update reorders existing rows.

A future page-transition system needs a separate contract. Do not repurpose this entry animation as an exit animation.

## Performance Evidence

The approved comparison used the same local Cloudflare Pages runtime, browser build, route, viewport, and Lighthouse mobile profile.

| Metric | Static baseline | Approved motion |
| --- | ---: | ---: |
| Performance score | 100 | 100 |
| First Contentful Paint | 0.8s | 0.8s |
| Largest Contentful Paint | 1.4s | 1.4s |
| Speed Index | 0.8s | 1.0s |
| Total Blocking Time | 0ms | 0ms |
| Cumulative Layout Shift | 0 | 0 |

The Speed Index change is expected: secondary content intentionally resolves over time. Acceptance depends on unchanged FCP/LCP, zero blocking, zero layout shift, and retained score—not on pretending the visual sequence has no visual-completeness cost.

The current authored stylesheet is `3313` bytes (`3.2 KiB`) before compression and adds no animation runtime dependency. Sorting JavaScript only supplies the terminal replay guard.

## Frame Acceptance

Capture the same fresh navigation at:

- approximately `100ms`: identity and biography visible; secondary groups beginning or still absent;
- approximately `450ms`: links and upper rows visibly resolving through fade/rise;
- approximately `1600ms` desktop or `1750ms` mobile: every element at its exact static final position and opacity.

Use real elapsed browser time. Virtual-time screenshots can miss compositor frames and produce misleading blank captures.

At every frame:

- layout geometry is already final;
- no element causes reflow during motion;
- no horizontal overflow appears;
- focus remains usable;
- the final frame matches the static layout pixel-for-pixel apart from normal font rasterization.

## Inspiration Boundary

The motion direction was informed by `nelson.co`, which used:

- container opacity `0 → 1`;
- container blur `8px → 0`;
- child opacity `0 → 1`;
- child rise `16px → 0`;
- `700ms` fade/filter transitions;
- `80ms` child staggering;
- spring movement lasting up to `1.4s`;
- a large client-side motion runtime.

Gildrb keeps the layered fade, blur, rise, and stagger while changing the implementation to CSS, reducing blur to `6px`, travel to `12px`, and rise duration to `900ms`. Desktop completes by `1470ms`; mobile's visual-row sequence completes by `1650ms`.

This is design analysis, not a dependency or source-code copy. Do not import the reference site's framework or runtime.

## Adaptation

For another project, preserve the architecture before copying numbers:

1. Identify content that must paint immediately.
2. Group secondary surfaces by meaning.
3. Apply one group fade and one ordered child rise.
4. Choose one interval per density class.
5. Bound the final completion time.
6. Benchmark against a static baseline.

To reproduce this exact gildrb character, keep the documented keyframes, curve, durations, distances, and delay tables unchanged. Change selectors only when markup count changes, and preserve the same start-time progression.

## Failure Modes

Reject:

- initial opacity above zero that makes the fade imperceptible;
- transform travel below the threshold where the page feels static;
- full-page opacity or visibility gates;
- hiding identity or biography;
- per-cell table animation;
- a blur on every child instead of the two containers;
- duration-only review without calculating final end time;
- a reduced-motion override that arrives after initial hidden styles;
- animation attached by late JavaScript;
- score-only performance claims without metric and frame evidence.

## Change Review

Any proposed change must report:

- the exact CSS diff;
- immediate and animated selector sets;
- complete timing tables with final end time;
- reduced-motion result;
- `100ms`, `450ms`, and final screenshots;
- baseline and changed Lighthouse metrics;
- transferred compressed bytes;
- whether animation replays after sort, theme, navigation return, or local state updates.

Without that evidence, preserve the approved implementation.
