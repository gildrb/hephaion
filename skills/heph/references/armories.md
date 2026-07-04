# Armories

An armory is Heph's local workspace. It is a normal directory with source files, chat history, retrieval index, traces, usage snapshots, and local memory.

## Structure

```text
~/.armories/<name>/
  materials/        source documents
  .harness/         Heph local state
    armory.toml     armory marker
    rag_index.json  retrieval index
    memory.json     armory memory
    chats/          saved sessions
    traces/         JSONL traces when enabled
    usage/          token and cost snapshots
    ignore          indexing ignore rules
  README.md         optional notes
```

## Ownership

- `materials/` is the source of truth.
- `.harness/` is local Heph state.
- Index files are rebuildable.
- Provider credentials stay machine-local and are not stored in `.armories`.
- Copy or sync `.armories` to move work between machines.

## Creating

```bash
heph armory init <name>
```

Use descriptive names such as `research-course` or `q3-reports`. Avoid opaque names that make later selection ambiguous.

## Moving

Copy the folder:

```bash
cp -r ~/.armories ~/backup/armories
```

On another machine, install Heph, place the folder under `~/.armories`, configure provider credentials, and run `heph <name>`.

## Maintenance

- Add files to `materials/`.
- Use `.harness/ignore` for ignore patterns.
- Run `heph index <path>` after large changes.
- Run `heph health <path>` when retrieval quality is poor.
- Use `/evidence` to inspect retrieval for a turn.

## Recovery

If an armory does not open:

1. Check that `materials/` exists.
2. Check `.harness/armory.toml`.
3. Check for legacy `.hephaion/` state if the armory came from an older release.
4. Avoid guessing when two state directories conflict.
