# Changelog

All notable changes to the `graphn` Python SDK are documented here.
This project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] — 2026-04-25

Initial public release. Targets the v0.1.0 hand-authored OpenAPI spec
served from `cp.graphn.ai` (control plane) and `model.graphn.ai`
(inference / OpenAI-compatible gateway).

**Scope is intentionally narrow:** v0.1.0 covers custom-model import
and inference end-to-end. The broader Graphn platform — agents,
knowledge bases, workflows, evals, datasets, guardrails, full BYO
inference CRUD, billing/usage, workspace administration — is **not
yet exposed** through this SDK and will be added in subsequent
minor releases. See the README's "Scope" section for the exact
boundary.

### Added

- Sync (`graphn.Client`) and async (`graphn.AsyncClient`) entrypoints,
  configured by env (`GRAPHN_API_KEY`, `GRAPHN_WORKSPACE_ID`,
  `GRAPHN_BASE_URL`, `GRAPHN_INFERENCE_URL`) or constructor args.
- Custom-model lifecycle: `client.custom_models.access`, `validate`,
  `create`, `list`, `get`, `refresh`, `wait_until_ready`, `wake`,
  `delete`. Pagination via cursor iterators.
- Secrets management: `client.secrets.create`, `list`, `get`,
  `refresh`, `delete`. HuggingFace token bring-your-own.
- Inference: `client.chat.completions.create` (sync + async,
  streaming + non-streaming), `client.models.list`, `client.tts`
  (`voices`, `synthesize`). Chat delegates to the official `openai`
  Python SDK so all OpenAI-compatible features (tools, structured
  outputs, multi-modal) work out of the box.
- `CustomModel.qualified_name` property returning `f"custom:{id}"`,
  the inference-host identifier the gateway requires for custom
  models.
- **Auto-wake on cold start** for chat completions: when a request
  to a custom model returns `503 scaled to zero / warming up`, the
  SDK transparently calls `POST /custom-models/{id}/wake` and
  retries with exponential backoff (default 180s budget,
  configurable per call via `wake_timeout`). Disable with
  `auto_wake=False`. Built-in / imported models are unaffected.
- HTTP transport with `Authorization: Bearer` injection,
  `X-Workspace-Id` default header, `X-Request-Id` round-tripping,
  bounded retries on 429 / 5xx with exponential backoff, and
  structured `APIError` subclasses.
- Public Pydantic types (`CustomModel`, `CustomModelAccess`,
  `Secret`, `ValidateModelResponse`, etc.) re-exported from
  `graphn.*`.
- `scripts/regenerate.sh` to refresh `_generated/` from the upstream
  OpenAPI spec; `scripts/smoke.py` and `scripts/e2e.py` for
  read-only and full-lifecycle validation against production.
- CI: lint + test matrix on Python 3.10, 3.11, 3.12; spec-sync
  workflow that opens a PR when the upstream OpenAPI spec changes;
  release workflow that builds + publishes to PyPI on `v*` tags via
  OIDC trusted publishing.

### Notes

- Requires Python 3.10+.
- Apache 2.0 licensed (matches the `graphn` CLI).

[Unreleased]: https://github.com/voltagepark/graphn-sdk-python/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/voltagepark/graphn-sdk-python/releases/tag/v0.1.0
