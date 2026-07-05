# Agent Guide

Root router. Product folders own product rules.

## Setup

- Start with `git status --short`.
- List tracked context with `git ls-files`.
- Read root files, then grep docs.
- Identify product from paths, commands, packages, docs, or UI.
- Load `<product>/AGENTS.md` before product edits.
- Load one matching skill before deep work.

## Checks

- Root diff: `git diff -- AGENTS.md README.md .agents/skills`.
- Line budget: `awk 'NF{c++} END{print c}' AGENTS.md`.
- Route check: `test -f heph/AGENTS.md && test -f heph/README.md`.
- Product work: run product guide checks and touched-surface tests.
- Public contract work: verify source, tests, docs, and runtime behavior.

## Style

- Write executable norms: trigger, action, check.
- Use blunt, short sentences.
- Keep root `AGENTS.md` under 60 filled lines.
- Keep product `AGENTS.md` under 80 filled lines.
- Use bullets and tables.
- Put examples, transcripts, and edge cases in skill references.
- Keep commands, paths, env vars, fields, and stdout exact.

## Architecture

- Root owns routing, package shape, shared safety, and shared checks.
- Product folders own vocabulary, commands, runtime paths, UI rules, contracts, and verification.
- `<product>/skills/*` owns specialized rules and examples.
- Source, tests, and runtime behavior outrank docs.

## When

- When task paths name a product, load that product guide.
- When source and docs disagree, inspect source and tests, then update guidance after behavior is confirmed.
- When a rule names product commands, place it in the product package.
- When public contracts change, include migration and tests.
- When data may contain secrets or private content, summarize state and redact values.
- When stdout is machine-read, keep prose in stderr or logs and preserve parseable output.
- When generated or vendor files appear, isolate AGENTS edits and handle cleanup as a separate approved task.

## Routes

| Task | Load |
| --- | --- |
| `heph/` product work | `heph/AGENTS.md` |
| Root routing or package shape | `.agents/skills/hephaion-system/SKILL.md` |
| Shared design rules | `.agents/skills/hephaion-design/SKILL.md` |

## PR Checklist

- Product guide loaded.
- Matching skills loaded.
- Setup and check commands run or reason recorded.
- Contracts preserved or migration included.
- Docs and implementation synchronized for public contracts.
- Routes resolve.
- Line budgets pass.
- Generated and vendor files listed as separate cleanup scope.
