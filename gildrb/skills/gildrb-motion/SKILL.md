---
name: gildrb-motion
description: Design, implement, document, or verify motion on the gildrb portfolio. Use for homepage entry choreography, staged reveals, opacity/blur transitions, transform timing, easing, cursor animation, scroll-edge fades, animated case evidence, reduced-motion behavior, or motion performance acceptance. Do not use for static spacing, typography, color selection, interaction state logic, media encoding, or editorial copy.
---

# Gildrb Motion

## Mission

Maintain one documented motion system for every animation and transition on the website.

## Owns

- Entry choreography, reveal grouping, sequence order, duration, delay, easing, and travel distance.
- CSS keyframes, transitions, motion selector boundaries, replay behavior, and motion inventory.
- Reduced-motion behavior and motion performance evidence.
- Motion purpose and acceptance criteria for animated case evidence.

## Excludes

- Do not choose static spacing, type metrics, color tokens, or content hierarchy.
- Do not own click, hover, sorting, navigation, persistence, or state logic; use `gildrb-interaction`.
- Do not encode or resize animated media; use `gildrb-media`.
- Do not add a framework or motion library when CSS expresses the behavior.

## Fixed Contract

- `references/inventory.md` lists every intentional keyframe, transition, and animated media surface.
- Primary identity and essential orientation content are usable before secondary motion completes.
- Motion never blocks HTML parsing, font fallback, keyboard access, or browser navigation.
- Every interface sequence defines reduced-motion behavior and a bounded completion time.
- Entry targets are guarded by `html:not([data-homepage-entry-complete])`. The first sort sets the terminal marker before stable-slot value updates, so sorting cannot replay or reposition entry motion.
- Desktop Links keep their approved DOM-order delays and complete by `1470ms`. Mobile pairs side-by-side Links/Contact siblings by visual row and completes by `1650ms`; do not alter desktop timing to solve mobile order.
- Performance acceptance compares the same route, runtime, viewport, browser, and throttling profile before and after.

## Procedure

1. Read `../../design.md` and `references/inventory.md`.
2. Load the exact motion reference when one exists.
3. Name the immediate layer, animated groups, child order, visual order at each breakpoint, and final state.
4. Write a timing table before CSS: start, duration, end, easing, distance, property, and desktop/mobile selector boundary.
5. Prefer opacity, transform, and a bounded filter on a small number of containers.
6. Update implementation, inventory, exact reference, and package checker together.
7. Capture early, middle, and final frames.
8. Compare FCP, LCP, Speed Index, TBT, CLS, score, and payload against a static baseline.

## References

- `references/inventory.md`: complete website motion registry and ownership boundaries.
- `references/gildrb-entry.md`: exact approved homepage fade, blur, rise, stagger, source CSS, timing model, and measured evidence.
- `references/verification.md`: browser, accessibility, and performance acceptance procedure.

## Reject

- Undocumented `animation`, `transition`, Web Animations API call, or animated media.
- Full-body visibility gates or font/load readiness gates.
- Permanent `will-change` on many elements.
- Unbounded springs or ornamental loops.
- A visually imperceptible substitute presented as preserving approved motion.
- “No Lighthouse score change” without metric and visual-frame evidence.

## Verify

Run product build and verifier commands. Search source for keyframes, animation declarations, transitions, Web Animations API calls, timers used for visual motion, and animated media; reconcile every result with the inventory. Test fresh navigation, first sort, reduced motion, keyboard access during motion, bfcache return, desktop DOM order, mobile visual-row order, and the documented viewport matrix.

## Done

Every motion surface is inventoried, purposeful, exactly specified where approved, accessible, deterministically bounded or explicitly justified as functional looping evidence, and backed by visual and performance checks.
