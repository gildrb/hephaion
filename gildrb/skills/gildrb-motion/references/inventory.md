# Motion Inventory

This is the complete approved motion registry for the gildrb portfolio. A source search that finds an animation or transition not represented here is a documentation failure.

## Homepage Entry

| Field | Contract |
| --- | --- |
| Route | `/` only |
| Source | `src/styles/15-homepage-entry.css` |
| Keyframes | `homepage-fade`, `homepage-rise` |
| Targets | `html:not([data-homepage-entry-complete])` Links/table groups and children |
| Purpose | Establish identity first, then reveal navigation and project evidence |
| Bound | Desktop completes at `1470ms`; mobile visual-row Links/Contact completes at `1650ms` |
| Reduced motion | Entire sequence absent under `prefers-reduced-motion: reduce` |
| Exact reference | `gildrb-entry.md` |

Do not reproduce this sequence on case routes or `/all`. The first homepage sort sets `data-homepage-entry-complete` before stable-slot value updates, permanently removing entry animation ownership from that document presentation.

## Mobile Portfolio Edge Fades

| Field | Contract |
| --- | --- |
| Route | Mobile homepage |
| Source | `src/styles/90-responsive.css` |
| Transition | `opacity 160ms ease-out` |
| Targets | `.portfolio-scroll-frame::before`, `.portfolio-scroll-frame::after` |
| Trigger | `has-scroll-top` and `has-scroll-bottom` classes on the horizontal portfolio section |
| Purpose | Indicate additional horizontally scrollable content without moving layout |
| Bound | `160ms` |

This is interaction feedback, not entry choreography. `gildrb-interaction` owns the scroll-state classes; `gildrb-motion` owns the opacity timing. The pseudo-elements use `pointer-events: none` and cannot intercept the table.

Reduced-motion treatment is not required for this non-spatial `160ms` orientation fade unless testing identifies user harm. Do not increase duration or add transform.

## Heph Demo Cursor

| Field | Contract |
| --- | --- |
| Route | `/heph` and the Heph section inside `/all` |
| Source | `src/styles/30-heph-demo.css` |
| Keyframe | `heph-demo-cursor-blink` |
| Target | `.heph-demo-cursor` |
| Trigger | `.heph-demo-composer.is-empty:not(.is-running)` |
| Timing | `1s steps(1, end) infinite` |
| States | opacity `0.9` through `49%`; opacity `0` from `50%` through `100%` |
| Purpose | Functional text-cursor affordance while the simulated composer is idle |

The loop stops when input is non-empty or the demo is running because the selector no longer matches. It is functional, not decorative. Preserve `pointer-events: none`.

If reduced-motion policy changes, prefer a steady visible cursor rather than removing the input affordance.

## n0thing Animated Evidence

| Field | Contract |
| --- | --- |
| Route | `/n0thing` and its article inside `/all` |
| Source partial | `src/case-media/n0thing/n0thing-wordmark-animation.html` |
| Assets | responsive `480`, `720`, `960`, and `1280` GIF variants |
| Purpose | Show the authored blinking-underscore wordmark behavior as case-study evidence |
| Loading | lazy, asynchronous decode |
| Ownership | `gildrb-media` owns encoding/srcset; `gildrb-motion` owns motion purpose and reduced-motion review |

This loop is evidence, not page decoration. Preserve its specific alt text. A future format migration should provide an equivalent static frame for `prefers-reduced-motion: reduce`; do not silently remove evidence or substitute an unrelated still.

## Scheduling That Is Not Motion

These `requestAnimationFrame` uses coordinate state or geometry and are not visual animation declarations:

- `src/scripts/10-core.js`: repeated scroll restoration after bfcache/back-forward traversal.
- `src/scripts/20-theme.js`: theme-toggle rectangle measurement refresh.
- `src/scripts/50-heph-demo.js`: composer overflow/state synchronization.

Do not register them as animation unless they begin interpolating visual values over multiple frames.

## Forbidden by Default

The current website has no approved:

- route transition;
- case-page entry animation;
- sorting animation;
- theme transition;
- email-copy animation;
- project-row hover transform;
- parallax effect;
- scroll-linked animation;
- JavaScript animation library;
- Web Animations API sequence.

Adding one requires an inventory entry, exact owner, reduced-motion behavior, bounded timing, visual frames, and performance evidence.

## Audit Command

```sh
grep -RInE '@keyframes|animation(-name|-duration|-delay|-timing-function)?:|transition(-property|-duration|-delay|-timing-function)?:|\.animate\(|requestAnimationFrame|setInterval|\.(gif|apng|webm|mp4)' src content
```

Classify every match as approved motion, animated evidence, state scheduling, or a violation. Do not suppress unexplained matches.
