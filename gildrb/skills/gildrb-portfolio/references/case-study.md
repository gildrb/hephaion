# Case Study

## Navigation

- Reuse the homepage shell.
- Keep the persistent location at the homepage name coordinate.
- Link only `Gil Rodrigues` home.
- Render arrow and project at the same inherited size.
- Remove Index links and tiny project kickers.

## Narrative

The user owns every title, deck, caption, metadata description, and body paragraph. Do not draft or alter publishable prose unless the user explicitly requests copy work. Layout, image, route, metadata, or generation tasks never imply permission to edit copy.

- Preserve existing and supplied wording verbatim.
- Use visibly unfinished `[Author: ...]` placeholders for missing sections.
- Keep requested suggestions outside source files until the user approves them.
- Treat spelling, grammar, tone, and clarity changes as copy work requiring explicit authorization.

- State the visual or product problem.
- Name constraints and objectives.
- Show exploration before resolution.
- Explain rejected directions.
- Explain typography, color, geometry, visual language, and implementation when evidence exists.
- End with tradeoffs and next improvements.

## Evidence

- Use original artifacts.
- Explain why each artifact matters.
- Never crop process evidence.
- Never invent research, metrics, authorship, or outcomes.
- Use code only when it demonstrates implementation responsibility.

## Structure

Follow `../../../case-studies.md`. Do not copy project-specific claims between case studies.

- Write in `content/<project>.md`, not in the HTML template or generated route.
- Keep the template limited to its `<!-- @case-markdown:<project> -->` token and structural shell.
- Use `![Caption](media:<media-id>)` for existing responsive media; the matching HTML partial owns technical image attributes.
- Run the build and verifier after every Markdown edit.
