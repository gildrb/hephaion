# Product Routing

Hephaion routes work from root guidance to product packages.

## Root Routing

Root `AGENTS.md` should answer only:

- Which product package owns this task?
- Which skill inside that product package should be loaded?
- Which universal safety and compatibility rules apply before product rules?

Root files should not explain a product's full command set, UI copy, design tokens, or runtime paths.

## Product Discovery

To identify the product:

1. Check changed paths.
2. Check task wording for product names, command names, package names, UI surfaces, and docs names.
3. Inspect root folders for matching product package names.
4. Load the product package `AGENTS.md` after a product is identified.
5. If more than one product is touched, load each relevant product package.

## Product Package Shape

A product package should use this shape:

```text
<product>/
├── AGENTS.md
├── README.md
└── skills/
    └── <skill>/
        ├── SKILL.md
        └── references/
```

Product packages may add command, design, operations, review, or release skills as needed.

## Cross-Product Changes

A rule belongs at root only when it applies to every product package without product vocabulary. If the rule names product commands, product files, product runtime paths, or product-specific UI surfaces, put it in the product package.
