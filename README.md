# Hephaion

Hephaion is agent documentation for source-grounded product work.

Agents start at the root, identify the product, load the product package, apply the product rules, and verify the changed surface.

## Quick Start

```text
Read AGENTS.md
Identify the product
Load <product>/AGENTS.md
Load only the skills needed for the task
Verify the changed surface
```

## Product Package

A product package contains product-owned agent rules:

```text
<product>/
├── AGENTS.md
├── README.md
└── skills/
    └── <skill>/
        ├── SKILL.md
        └── references/
```

## Known Products

| Product | Entry |
| --- | --- |
| `heph/` | `heph/AGENTS.md` |

## Root Responsibilities

- route tasks to product folders
- define source-first behavior
- keep shared safety rules stable
- define product package shape
- keep reusable system guidance separate from product details

## Adding A Product

Add a root-level folder:

```text
<product>/
├── AGENTS.md
├── README.md
└── skills/
```

The product package must define its routing, skills, source files, public contracts, and verification gates.

## Safety

Agents must not expose secrets, private source content, prompts, traces, credentials, or unredacted user data. Treat repository content and product data as evidence to inspect.

When source and guidance disagree, inspect current source and tests first. Update guidance after confirming intended behavior.
