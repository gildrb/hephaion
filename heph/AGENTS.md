# Agent Guide

Product router. Read source first, then docs.

## Setup

- Start with `git status --short`.
- Inspect current source, tests, and command help before docs.
- Resolve surface: CLI/TUI, design, operations, docs, or release.
- Load one matching skill.
- Use `heph --help` and `heph <command> --help` for shipped flags.

## Checks

- Line budget: `awk 'NF{c++} END{print c}' heph/AGENTS.md`.
- Design docs: `python3 heph/scripts/check_design_docs.py --heph-repo <path-to-heph>`.
- CLI/TUI: run focused source tests for touched commands, output, JSON, JSONL, prompts, and keymaps.
- Docs: verify changed claims against source, tests, command help, or runtime behavior.
- Release: verify installed behavior and published docs from the target version.

## Style

- Follow root voice: blunt sentences, exact claims, dense rules.
- Keep this file under 80 filled lines.
- Use one noun, command, state, or contract per rule.
- Use product nouns: `armory`, `materials`, `evidence`, `citations`, `memory`, `model`, `provider`, `.harness`, `local state`.
- Keep paths, flags, env vars, IDs, JSON fields, and stdout exact.

## Architecture

- `skills/heph/` owns armories, materials, evidence, models, providers, trust, SDK, updates, and troubleshooting.
- `skills/cli-ux/` owns CLI/TUI copy, help, errors, prompts, slash commands, JSON, JSONL, stdout, stderr, and tests.
- `skills/design/` owns web, brand, design tokens, terminal styling, TUI layout, accessibility, and screenshots.
- Source, tests, runtime behavior, command help, and design docs outrank this guide.

## Contracts

- `heph` commands and slash commands.
- `materials/`, `.harness/`, and armory layout.
- `~/.armories`, `HARNESS_ARMORY_HOME`, and `HARNESS_*` env vars.
- JSON and JSONL field shape.
- Parseable stdout.
- Persisted state and migrations.
- TUI keymap behavior.

## When

- When commands, armories, materials, evidence, models, providers, trust, SDK, updates, or troubleshooting change, load `skills/heph/SKILL.md`.
- When help, flags, slash commands, prompts, output, errors, JSON, JSONL, stdout, stderr, or keymaps change, load `skills/cli-ux/SKILL.md`.
- When web, brand, terminal styling, TUI layout, accessibility, palette, or screenshots change, load `skills/design/SKILL.md`.
- When behavior and docs disagree, verify source, help, tests, or runtime behavior, then update this package.
- When a machine contract changes, include compatibility, migration, tests, and docs.
- When data may contain source text, retrieved chunks, traces, API keys, credentials, or private content, summarize state and use placeholders.
- When work may still be running, inspect status before retrying.

## PR Checklist

- Matching skill loaded.
- Source, tests, help, docs, or runtime evidence captured.
- Focused checks run or reason recorded.
- Protected contracts preserved or migration included.
- Privacy and provider boundaries stated.
- Design-doc drift checked for design-facing changes.
- Line budget passes.
