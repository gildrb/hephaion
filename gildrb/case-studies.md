# Case Studies

This document defines the path from a homepage image to an authored project page.

## Route Contract

- Use one top-level route per case study: `/<project>`.
- Generate `/<project>/index.html`.
- Link the designated homepage image directly to `/<project>`.
- Use the same project slug in canonical metadata, social metadata, JSON-LD, sitemap, feed, machine-readable mirrors, analytics route, and verifier assertions.
- Add permanent redirects when a previously exposed route changes.

Current routes:

- `/heph`
- `/filen`
- `/n0thing`
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
The location uses two lines: `Gil Rodrigues` then `→ <Project>`.

```text
Gil Rodrigues
→ <Project>
```

- `Gil Rodrigues` links to `/`.
- `Gil Rodrigues` and the arrow are tertiary gray; the current project is primary.
- All three parts share the same inherited `19px` size and weight.
- The project name preserves its public casing, including `mL7`.
- Do not add Index navigation.
- Do not repeat a tiny project/category kicker above the title.

## Article Order

Use this sequence when evidence supports it:

1. Decision-led title.
2. Optional factual deck.
3. Compact contribution, scope, and context metadata.
4. Primary result image.
5. Problem and constraints.
6. Exploration and rejected directions.
7. Selection reasoning.
8. Typography, color, geometry, and visual-language decisions.
9. System applications.
10. Interface or implementation details.
11. Tradeoffs, reflection, and next improvements.

Do not force a section when evidence does not exist. Add an explicit author placeholder or omit it until the user provides proof. A placeholder must be visibly unfinished, such as `[Author: explain the rejected direction]`; it must not masquerade as publishable prose.

## Markdown Authoring

- Author each case study in `content/<project>.md`; this is the only source for its visible title, deck, metadata rows, section headings, paragraphs, captions, links, lists, and code examples.
- Keep `src/<project>.template.html` structural. It contains the shell and one `<!-- @case-markdown:<project> -->` insertion token, not authored article prose.
- Keep responsive image markup in `src/case-media/<project>/<media-id>.html` so writing never requires editing `srcset`, dimensions, loading behavior, or layout HTML.
- Reference those assets from Markdown with `![Caption](media:<media-id>)`. Consecutive media references form the existing two-column grid.
- Begin every file with one `#` title and exactly three `- **Label:** Value` metadata rows. A `>` deck may appear between them, but authors may omit it rather than inventing introductory copy.
- Generate the static route with `node scripts/build-page.mjs`; never edit `<project>/index.html` directly.
- Preserve ordinary Markdown support for `##` and `###` headings, paragraphs, lists, emphasis, strong text, inline code, external links, and fenced code blocks.
- Keep `content/README.md` synchronized with the supported authoring syntax.

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

## Authorship Boundary

Case-study prose is author-owned. The user writes the titles, decks, captions, metadata descriptions, and article body.

- Never rewrite, replace, expand, summarize, or “improve” existing case-study copy unless the user explicitly asks for that exact operation.
- Never fill an empty section with publishable prose on the user's behalf.
- Preserve user-supplied wording verbatim when implementing it, apart from an explicitly requested correction.
- Agents may maintain document structure, insert visibly unfinished author placeholders, or identify missing and unclear sections.
- Agents may offer suggested copy only when requested. Keep suggestions separate from the source until the user approves or supplies the final wording.
- A request to change layout, typography, images, routes, metadata wiring, or generation does not authorize copy edits.
- Grammar, spelling, tone, and clarity edits also require an explicit copy-editing request.

## Writing Guidance

Use these principles only when the user explicitly requests suggestions, drafting, or copy editing. They guide review; they do not grant permission to overwrite the author's prose.

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
- Location uses two lines: `Gil Rodrigues` then `→ Filen`.

## Heph

- Project label: `Heph`.
- Route: `/heph`.
- Homepage entry: interactive terminal demo followed by full-width date/title metadata.
- Link the metadata strip to `/heph`; do not link the homepage directly to the source repository and do not overlay a link on the interactive terminal.
- Link `https://github.com/gildrb/heph` from inside the case-study article.
- Describe only behavior supported by the current Heph documentation and repository.
- Location uses two lines: `Gil Rodrigues` then `→ Heph`.

## mL7

- Project label: `mL7`.
- Route: `/ml7`.
- Homepage entry: approved mL7 logo image.
- Make that logo image the designated case-study link.
- Location uses two lines: `Gil Rodrigues` then `→ mL7`.
- Reuse the Filen shell, type steps, media treatment, section spacing, shared sidebar behavior, theme behavior, and responsive layout.
- Replace only project content and evidence.
- Do not copy Filen-specific claims into mL7.
- If evidence is incomplete, write only what the visible artifacts establish and leave further sections for later evidence.

## Completion

A case study is complete when its route, homepage entry, persistent location, narrative, evidence, responsive media, metadata mirrors, generated output, verifier, browser rendering, and protected preview agree.
