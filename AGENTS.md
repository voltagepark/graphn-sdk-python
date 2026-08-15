# Agent guide — graphn-sdk-python

This is the official Python SDK for the Graphn API. It is published to
PyPI as the `graphn` package and is generated from the OpenAPI 3.1
spec hosted at `https://cp.graphn.ai/openapi.yaml` (source of truth
lives in `voltagepark/takao` at `svc/graphn-cp/api/openapi.yaml`).

## Layout

| Path                          | Purpose                                                     |
| ----------------------------- | ----------------------------------------------------------- |
| `src/graphn/__init__.py`      | Re-exports public surface (`Client`, `AsyncClient`, types). |
| `src/graphn/_client.py`       | Hand-written `Client` / `AsyncClient` over httpx.           |
| `src/graphn/_exceptions.py`   | Exception hierarchy mapped from HTTP status codes.          |
| `src/graphn/_pagination.py`   | Cursor-based `SyncPage` / `AsyncPage` iterators.            |
| `src/graphn/_generated/`      | Output of `openapi-python-client`. **Never edit by hand.**  |
| `src/graphn/custom_models/`   | Hand-written ergonomic wrapper around generated transport.  |
| `src/graphn/secrets/`         | Hand-written ergonomic wrapper.                             |
| `src/graphn/chat/`            | Thin delegation to the official `openai` SDK.               |
| `src/graphn/models.py`        | `list()` merges CP `GET /v1/models` with inference; `retrieve` still uses OpenAI. |
| `src/graphn/tts.py`           | Hand-written (TTS isn't in the OpenAI SDK).                 |
| `src/graphn/agents.py`        | Agents CRUD / publish / run.                                |
| `src/graphn/functions.py`     | Functions CRUD / test / dry-run.                            |
| `src/graphn/mcp_servers.py`   | MCP servers, tools, runtime.                                |
| `src/graphn/workflows.py`     | Workflows CRUD / publish / run.                             |
| `src/graphn/executions.py`    | Execution get + `wait` (CP vs gateway by id).               |
| `src/graphn/triggers.py`      | Cron / webhook triggers.                                    |
| `src/graphn/knowledgebases.py`| KBs, search, ingest + `wait_ingest`.                        |
| `src/graphn/organizations.py` | Org CRUD.                                                   |
| `src/graphn/workspaces.py`    | Workspace CRUD (org-scoped).                                |
| `src/graphn/api_keys.py`      | Workspace API keys.                                         |
| `src/graphn/blueprints.py`    | Public catalog + deploy.                                    |
| `src/graphn/storages.py`      | REST overlay + S3-host objects.                             |
| `src/graphn/batch.py`         | Gateway batch jobs.                                         |
| `src/graphn/imported_models.py` | BYO CRUD + inference-host probes.                         |
| `tests/`                      | `pytest` + `respx` mocks for both base URLs.                |
| `scripts/regenerate.sh`       | Regenerates `_generated/` from the upstream spec.           |
| `.github/workflows/`          | `test.yml`, `release.yml`, `spec-sync.yml`.                 |

## Conventions

- Public types must be importable from `graphn` directly. New resources
  add re-exports to `src/graphn/__init__.py`.
- Anything in `src/graphn/_generated/` is overwritten on every spec
  sync. Wrap it in hand-written modules instead of editing it.
- Chat completions and embeddings **must** route through the `openai`
  Python SDK so customers get full feature parity for free. `models.list`
  is the exception: inference `GET /v1/models` is not the full catalog
  (prod currently returns imported/custom only), so we merge it with
  the control-plane catalog (`GET /v1/models`, same as `graphn model list`).
- `workflows.create` / `update` auto-link DSL `agents`/`functions`/
  `mcp_servers` via `save_bundle`, matching `graphn wf create`.
- Control-plane requests **must** include `X-Workspace-Id` and the
  `{workspaceId}` path parameter; both come from `Client(workspace_id=...)`.
- Run `ruff check src tests` and `pytest` before opening a PR.

## Spec sync

Pulling spec changes from upstream:

```bash
./scripts/regenerate.sh
```

The nightly `spec-sync.yml` workflow does this automatically and opens a
PR if the regenerated tree differs from `main`.
