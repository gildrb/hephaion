# Product Routing

Route work from root guidance to product packages.

## Root Routing

Root `AGENTS.md` answers:

- Which product package owns this task?
- Which product guide should load next?
- Which shared safety rules apply first?

Root files must not explain product command sets, copy, tokens, or runtime paths.

## Discovery

1. Check changed paths.
2. Check task wording for product names, commands, package names, UI surfaces, and docs names.
3. Inspect root folders for matching product packages.
4. Load `<product>/AGENTS.md` after identifying the product.
5. Load each relevant product guide for multi-product work.

## Package Shape

```text
<product>/
├── AGENTS.md
├── README.md
└── skills/
    └── <skill>/
        ├── SKILL.md
        └── references/
```

Product packages may add command, design, operations, review, or release skills.

## Cross-Product Work

A rule belongs at root only when it applies without product vocabulary. If it names product commands, files, runtime paths, or UI surfaces, put it in the product package.
