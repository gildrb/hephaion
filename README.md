# Hephaion

Hephaion is the canonical agent instruction system for Heph.

It exists so agents can work on Heph with the same level of product judgement every time: read the real project first, route to the right skill, apply stable CLI and design rules, preserve privacy and local ownership, and verify the changed surface before shipping.

This repository is intentionally instruction-heavy. The goal is not to document every Heph feature for humans; the goal is to give agents decision-complete rules that turn Heph's product values into repeatable implementation behavior.

## Source Inputs

Hephaion is adapted from the structure of Vercel's public agent guidance, especially the layered shape of:

- always-loaded repository guidance
- a front-door skill for task routing
- deep references for core rules, copy, command contracts, and verification
- focused operational references for product areas

The Heph-specific source of truth comes from:

- `gildrb/heph` `README.md`
- `gildrb/heph` `design.md`
- `gildrb/heph` `cli-design.md`
- `gildrb/heph` docs for armories, CLI reference, models, trust, and getting started

When Heph source and this repository disagree, inspect Heph source and tests first. Then update Hephaion so the rules match reality.

## Repository Shape

```text
AGENTS.md
  Always-loaded guidance for agents working with Hephaion or importing its rules.

.agents/skills/heph-cli-ux/
  Product-grade CLI and TUI UX rules for Heph.

.agents/skills/heph-design-engineering/
  Product-grade design engineering rules for Heph web, brand, CLI, and TUI surfaces.

skills/heph/
  A user-facing Heph operating skill: commands, workflows, troubleshooting, trust, and automation.
```

## How Agents Should Use This

1. Read the project source first.
2. Identify whether the task changes product behavior, CLI/TUI UX, web/design, documentation, automation, or operational usage.
3. Load the narrowest applicable skill.
4. Load only the references named by that skill for the touched surface.
5. Preserve compatibility for command names, config keys, env vars, JSON fields, file layouts, and parseable output unless the task explicitly migrates them.
6. Review the complete changed surface, not only the edited line.

## Heph Product Baseline

Heph is a local document agent. It indexes source files in an armory, answers from those files, and shows cited source passages.

Core product commitments:

- Local-first: armories are normal folders; `.harness/` is inspectable local state.
- Evidence-forward: answers should make retrieved sources visible and reviewable.
- Private by default: provider prompts, diagnostics, and local model choices are explicit trust boundaries.
- Quiet and precise: terminal and web UI avoid decorative effects, hype, and noisy copy.
- Portable: users can copy or sync armories between machines and reconfigure providers locally.
- Agent-ready: non-interactive paths must be explicit, bounded, parseable, and free of trusted prose from user or remote content.

## Change Policy

Durable rule changes should include:

- the Heph source or test evidence behind the rule
- the scope of the rule and its exceptions
- one bad/good example when the rule is mechanical
- a verification gate that prevents drift

Do not promote one screenshot, one review comment, or one legacy string into a universal rule without checking adjacent surfaces.
