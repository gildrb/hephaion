# Case Studies

This document defines the path from a homepage image to an authored project page.

## Route Contract

- Use one top-level route per case study: `/<project>`.
- Generate `/<project>/index.html`.
- Link the designated homepage image directly to `/<project>`.
- Use the same project slug in canonical metadata, social metadata, JSON-LD, sitemap, feed, machine-readable mirrors, analytics route, and verifier assertions.
- Add permanent redirects when a previously exposed route changes.

Current routes:

- `/filen`
- `/ml7`

## Homepage Entry

- Show the project title in the existing section-title treatment.
- Do not link the title.
- Do not add a project summary.
- Do not add `Read the case study` or equivalent copy.
- Show only the images approved for that project’s homepage entry.
- Make the designated logo image the only case-study link.
- Preserve its entire frame and responsive sources.
- Give the anchor a precise accessible name.

## Persistent Location

Each case page starts in the exact homepage name position:

```text
Gil Rodrigues → <Project>
```

- `Gil Rodrigues` links to `/`.
- `Gil Rodrigues` and the arrow are secondary gray; the current project is primary.
- All three parts share the same inherited `19px` size and weight.
- The project name preserves its public casing, including `mL7`.
- Do not add Index navigation.
- Do not repeat a tiny project/category kicker above the title.

## Article Order

Use this sequence when evidence supports it:

1. Decision-led title.
2. Factual deck.
3. Compact contribution, scope, and context metadata.
4. Primary result image.
5. Problem and constraints.
6. Exploration and rejected directions.
7. Selection reasoning.
8. Typography, color, geometry, and visual-language decisions.
9. System applications.
10. Interface or implementation details.
11. Tradeoffs, reflection, and next improvements.

Do not force a section when evidence does not exist. Add a precise placeholder or omit it until the user provides proof.

## Evidence Types

Useful evidence includes:

- original sketches
- exploration boards
- rejected directions
- symbol and wordmark combinations
- scale tests
- construction grids
- spacing rules
- typography comparisons
- color studies
- app icons
- UI components
- responsive states
- motion studies
- campaign applications
- implementation excerpts
- design tokens
- documentation
- shipped interface captures

Explain what each artifact proves. Do not use images as decoration.

## Writing

- Lead each section with the decision or problem.
- Name constraints precisely.
- Explain why rejected directions failed.
- Separate observed evidence from retrospective interpretation.
- Prefer facts over adjectives.
- Avoid `passionate`, `meaningful experiences`, `innovative`, and similar marketing language.
- Do not claim measurable outcomes without evidence.
- End with tradeoffs and what should improve next.

## Filen

- Project label: `Filen`.
- Route: `/filen`.
- Homepage entry: white Filen mark and wordmark on black.
- Homepage image count: one.
- Required process evidence: complete exploration board.
- The board must never be cropped.
- Do not link to `filen.io` from the case page.
- Location: `Gil Rodrigues → Filen`.

## mL7

- Project label: `mL7`.
- Route: `/ml7`.
- Homepage entry: approved mL7 logo image.
- Make that logo image the designated case-study link.
- Location: `Gil Rodrigues → mL7`.
- Reuse the Filen shell, type steps, media treatment, section spacing, shared sidebar behavior, theme behavior, and responsive layout.
- Replace only project content and evidence.
- Do not copy Filen-specific claims into mL7.
- If evidence is incomplete, write only what the visible artifacts establish and leave further sections for later evidence.

## Completion

A case study is complete when its route, homepage entry, persistent location, narrative, evidence, responsive media, metadata mirrors, generated output, verifier, browser rendering, and protected preview agree.
