# Rule Authoring

Rules make agents consistent without freezing product evolution.

## Documentation Density

- No filler in docs.
- Use blunt, short sentences.
- Keep claims exact. Do not trade accuracy for brevity.
- Every line must route, constrain, define, or verify.
- Root `AGENTS.md`: 60 non-empty lines max unless routing truly requires more.
- Product `AGENTS.md`: 80 non-empty lines max unless product safety requires more.
- Prefer route tables over explanatory prose.
- Move examples, state machines, edge cases, and transcripts into skill references.

## Write Applicable Rules

Good rules include:

- surface: where the rule applies
- trigger: when to use it
- action: what the agent should do
- exception: when not to apply it
- verification: how to know it worked

Avoid vague goals such as `make it nice`, `improve quality`, or `follow best practices` without checkable behavior.

## Keep Layers Separate

- Root: routing, safety, product package shape, shared verification.
- Product package: commands, vocabulary, product UX, runtime paths, compatibility contracts.
- Skill front door: when to load references and how to triage the task.
- Reference files: durable rules, examples, contracts, and review gates.

## Avoid Brittle Assumptions

Do not hardcode repository owners, local clone paths, source attribution, or machine-specific locations. Use repository-relative paths for guidance files and product-runtime paths only when they are part of the product contract.

## Examples

Use placeholders when a value is not a product contract:

```text
<path>
<name>
<value>
<api-key>
```

Use literal product commands only inside the product package that owns them.
