# Troubleshooting

Start with state: armory, materials, index, model, provider, trust boundary.

## No Armory Or Wrong Armory

```bash
heph armory open <path>
heph trust <path>
```

Check:

- path exists
- `materials/` exists
- `.harness/armory.toml` exists
- `HARNESS_ARMORY_HOME` if named armories do not appear

## No Materials

```bash
cp <file> ~/.armories/<name>/materials/
heph index ~/.armories/<name>
```

## Poor Retrieval

```bash
heph health <path>
heph index <path>
```

Then inspect:

```text
/evidence
/materials
```

Common causes:

- unsupported file
- extraction quality
- stale index
- material disabled in `/materials`
- question needs a different model after retrieval succeeds

## Missing Model Or Credentials

```text
/login
/models
/local
```

Generic env vars:

```bash
HARNESS_API_KEY=<api-key>
HARNESS_MODEL=<provider-model-name>
```

## Local Model Fails

```bash
heph local status
heph local revalidate <model-id>
heph local stop
```

A downloaded local model is not usable until validation passes.

## Privacy Questions

```bash
heph trust <path>
```

Explain:

- materials stay local by default
- hosted providers receive active question and selected retrieved chunks
- local models keep prompts local after required assets are available
- diagnostics are opt-in and separate from prompts

## Update Problems

```bash
heph release status
heph update
heph --version
```

Distinguish released installs from source installs before recommending update steps.
