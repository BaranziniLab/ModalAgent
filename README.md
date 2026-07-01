# ModalAgent

MCP helper for Modal compute projects, deployment planning, environment validation, and guarded command/API invocation for cloud scientific jobs.

This repository follows the BioRouter `.brxt` extension convention used by `SPOKEAgent` and `UCSFOMOPAgent`: a root `manifest.json`, Python package under `src/`, and optional bundled skills under `skills/`.

## Tools

- `get_modalagent_status`: report configured environment variables without revealing secrets.
- `get_modalagent_request_plan`: explain whether an API request is read-only or requires explicit mutation approval.
- `call_modalagent_api`: call a platform API endpoint with write methods blocked unless `allow_mutation=true`.
- `summarize_modalagent_resource`: summarize a JSON export or API payload without making a network call.

## Configuration

| Variable | Required | Secret | Purpose |
|---|---:|---:|---|
| `MODAL_TOKEN_ID` | true | true | Modal token id |
| `MODAL_TOKEN_SECRET` | true | true | Modal token secret |
| `MODAL_LOG_LEVEL` | false | false | Logging level |


## Build

```bash
uv sync
scripts/build_brxt.sh
```

The bundle is written to `dist/modalagent.brxt`.

## Install in BioRouter

```bash
biorouter extension install dist/modalagent.brxt
```

Add the required secrets with `--secret KEY=value` or configure them in the BioRouter UI.

## License

Apache-2.0. See `LICENSE`.
