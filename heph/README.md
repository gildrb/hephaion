# Package

Agent documentation.

Local document agent: indexes armory files, answers from them, and shows citations.

## Quick Start

```text
Read AGENTS.md
Choose the skill for the task
Inspect current source and tests
Apply product contracts
Verify the changed surface
```

## Armory Layout

Work uses local armories:

```text
<armory>/
├── materials/
├── .harness/
└── README.md
```

`materials/` contains user materials. `.harness/` contains local state: indexes, memory, chats, traces, usage snapshots, and ignore rules.

## Map

```text
AGENTS.md
  product router

skills/heph/
  operations, commands, troubleshooting, trust, SDK, automation

skills/cli-ux/
  CLI/TUI UX, copy, command contracts, machine output, verification

skills/design/
  web, brand, terminal, TUI design

design.md
  web and brand contract

cli-design.md
  terminal and Textual contract

scripts/check_design_docs.py
  design-doc drift checker against a Heph source tree
```

## Source

Inspect current source first. Use tests, docs, command help, and design docs as immediate truth. Update this package after confirming durable rules.

## Safety

Do not expose material text, retrieved chunks, prompts, traces, API keys, credentials, or private data unless the user asks for an inspection surface that should show it.
