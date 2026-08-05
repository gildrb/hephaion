# Verification

## Establish Baseline

1. Build the static version from the same commit or a controlled animation-disabled variant.
2. Copy its complete publish output to a temporary directory.
3. Build the motion version.
4. Serve both with the same local runtime on separate ports.
5. Use one browser binary, viewport, throttling profile, and Lighthouse version.

Do not compare local motion against a remote baseline or mix desktop and mobile profiles.

## Metrics

Record at least three runs when results vary. Report median:

- performance score;
- First Contentful Paint;
- Largest Contentful Paint;
- Speed Index;
- Total Blocking Time;
- Cumulative Layout Shift;
- transferred and uncompressed HTML/CSS/JavaScript bytes.

Motion can intentionally affect Speed Index. It must not conceal regressions in FCP, LCP, blocking, or layout stability.

## Frames

Use real elapsed time after navigation. Capture:

- early orientation frame;
- midpoint with visible progression;
- final frame after the maximum calculated end time.

A frame set must prove both motion and final-state correctness. One final screenshot cannot prove choreography.

## Interaction During Motion

While the sequence runs:

- tab through available controls;
- activate one link or button;
- confirm hit boxes use final geometry;
- confirm no pointer-blocking overlay exists;
- confirm sorting or local updates do not restart entry motion;
- confirm browser back/forward restores the intended state.

## Reduced Motion

Emulate `prefers-reduced-motion: reduce` before navigation. Confirm:

- no hidden initial state;
- no animation delay;
- final opacity, filter, and transform immediately;
- unchanged semantic and focus order.

## Rendering

Check desktop and mobile widths in light and dark themes when filters or transparent colors are involved. Review console errors, overflow, clipped focus, font swaps, and final pixel alignment.

## Report

Return:

```text
commit:
browser/runtime:
viewport/profile:
immediate selectors:
animated selectors:
maximum end time:
reduced motion:
frame captures:
baseline metrics:
changed metrics:
payload delta:
interaction result:
console status:
verdict:
```
