---
name: gildrb-portfolio
description: Use for gildrb homepage structure, project ordering, author-owned case-study copy, evidence selection, top-level project routes, metadata mirrors, static generation, or portfolio verification.
---

# Portfolio

Maintain the text-only sortable index and authored case-study system.

## Workflow

1. Read the portfolio source and rendered route.
2. Read `../../case-studies.md`.
3. Load only the relevant reference below.
4. Keep claims bounded by supplied evidence.
5. Preserve case-study copy unless the user explicitly requests copy work.
6. Edit visible case-study writing only in `content/<project>.md`.
7. Update structural templates and media partials before generated files.
8. Synchronize routes and machine-readable mirrors.
9. Build, verify, and render desktop and mobile.

## References

- `references/homepage.md`: sortable homepage rows and project routing.
- `references/case-study.md`: article structure, evidence, and writing.
- `references/routing.md`: top-level routes, generation, metadata, and redirects.
- `references/verification.md`: portfolio completion checks.

## Done

- Homepage stays concise, text-only, and globally sortable.
- Each project row uses one clear internal route.
- Persistent location uses two lines: `Gil Rodrigues` then `→ <Project>`.
- Generated output and metadata agree.
- Evidence is complete, uncropped, optimized, and explained.
