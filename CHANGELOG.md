# Changelog

All notable changes to the `graphn` Python SDK are documented here.
This project follows [Semantic Versioning](https://semver.org/).

## How to release

One PR. In the same PR:

1. Bump `[project].version` in `pyproject.toml` to `X.Y.Z`.
2. Replace `## [Unreleased]` below with `## [X.Y.Z] — YYYY-MM-DD` and
   add a fresh empty `## [Unreleased]` above it.

Merge to `main`. The `auto-tag` job in `.github/workflows/release.yml`
reads the new `pyproject` version, validates that this CHANGELOG has the
matching `## [X.Y.Z]` section, creates `vX.Y.Z`, and pushing the tag
re-fires the workflow's `build` + `publish` jobs which ship to PyPI via
trusted publishing. `pip install graphn==X.Y.Z` works ~1 minute later.

No `git tag`, no `git push --tags`, no Actions clicks.

## [Unreleased]

## [0.1.4] — 2026-04-25

Patch release. Unifies how customers address custom models: pass
`model.id` everywhere, including in chat completions. The SDK adds
the gateway's `custom:` routing prefix internally, so the wire
protocol is unchanged and the inference path is byte-identical to
the prefixed form. No backend changes; no new operations.

### Changed

- `client.chat.completions.create(model=...)` (sync and async) now
  accepts a bare custom-model id (`cm_<hex>`) and prepends the
  gateway's `custom:` routing prefix internally before delegating to
  the OpenAI client. Already-prefixed strings (`custom:cm_...`) and
  first-party catalog ids (`meta-llama/...`, `Qwen/...`) are passed
  through unchanged. Auto-wake on cold-start works against the
  normalized id, so passing `model=model.id` works end-to-end on
  custom models that were scaled to zero.

  Migration: replace `model=model.qualified_name` with
  `model=model.id` in chat calls. The previous prefixed-string form
  still works, so this is opt-in — old code keeps running.

### Removed

- `CustomModel.qualified_name` property. It returned `f"custom:{id}"`
  and existed solely so customers could feed a custom-model id to
  `chat.completions.create`. Now that `chat.completions.create`
  accepts the bare id directly, the property is redundant. Anyone
  using it gets `AttributeError`; the one-line fix is
  `model.id` (for chat addressing) or, if you specifically need the
  wire-level prefixed form, `f"custom:{model.id}"`.

  We're shipping this as a patch despite removing a property: the
  property has only existed since 0.1.0, was undocumented outside
  one example block, and the SDK is pre-1.0. If this causes you
  pain, file an issue and we'll restore it as a deprecated alias.

### Docs

- README, `docs/cold-starts.md`, and all examples now use
  `model=model.id` consistently. The "drop-in for `openai`" example
  keeps the explicit `custom:cm_...` form, with a note explaining
  that the prefix is the cost of bypassing `graphn.Client`.

## [0.1.3] — 2026-04-25

Patch release. Tightens the S3 import flow with a client-side guard,
documents the requirement on the project page, and scrubs the
serving-engine implementation detail from customer-facing wording. No
new operations.

### Changed

- `client.custom_models.create` now raises `graphn.ValidationError`
  (code `missing_huggingface_model_id`) client-side when
  `weight_source` is `s3_presigned` or `s3_assume_role` and
  `huggingface_model_id` is missing or blank. Graphn uses
  `huggingface_model_id` as the canonical model identifier — it's
  the name the inference endpoint advertises and the value you pass
  in `model` for chat completions — so without it the deployed model
  can't be addressed for inference (the request 404s with "model
  does not exist"). This mirrors the "Model ID" requirement the web
  UI's S3 import form has always enforced. The control plane now
  returns 422 for the same shape (voltagepark/takao#1997), so this
  catches the mistake one round-trip earlier.

  Existing callers passing `huggingface_model_id` for S3 are
  unaffected. Callers that omitted it were already producing
  unreachable models; they now get a clear error at create time
  instead.

- README's **"Importing from S3"** section now leads with a callout
  explaining that `huggingface_model_id` is required for S3 imports
  too, with both `s3_presigned` and `s3_assume_role` recipes
  including the field. The PyPI long description (project page on
  pypi.org) reflects this; v0.1.2's README had the S3 sections but
  omitted the requirement.

- Customer-facing wording no longer mentions the serving engine
  (`vLLM`) or its flags (`--served-model-name`). README, the S3
  example's docstring + `--hf-model-id` help, the
  `_S3_WEIGHT_SOURCES` comment, and the `ValidationError` message
  all use engine-agnostic phrasing now ("canonical model identifier
  the inference endpoint advertises"). The error code and the
  asserted "huggingface_model_id is required" substring are
  unchanged, so test code that pattern-matches on either is safe.

## [0.1.2] — 2026-04-25

Documentation-only patch release. No API or behavior changes — S3
import has worked since v0.1.0; this release just makes that
discoverable.

### Added

- README now documents both S3 weight sources end-to-end:
  `s3_presigned` (no AWS credentials shared with Graphn) and
  `s3_assume_role` (longer-lived, IAM-role-based). Includes a
  dedicated **"Importing from S3"** section with copy-pasteable
  recipes.
- New runnable example
  [`examples/import_from_s3.py`](examples/import_from_s3.py)
  covering both S3 flavors via `--weight-source`.
- Tagline updated to mention S3 alongside HuggingFace; the
  `client.custom_models` row in the scope table now lists all three
  sources.

## [0.1.1] — 2026-04-25

Documentation-only patch release. No API or behavior changes.

### Fixed

- `Documentation` URL on PyPI now points to the actual API explorer
  at <https://graphn.ai/api>; the previous v0.1.0 link
  (`docs.graphn.ai`) was a placeholder for a subdomain that was never
  set up.

### Added

- `Changelog` link added to the PyPI sidebar (points at
  `CHANGELOG.md` on GitHub).
- README now opens with an explicit **Scope** callout listing the
  surfaces v0.1.x covers (custom-model import + OpenAI-compatible
  inference) and the surfaces it does **not** yet cover (agents,
  knowledge bases, workflows, evals, datasets, guardrails, full BYO
  inference CRUD, billing/usage, workspace admin).
- New `examples/` directory with runnable scripts:
  - `import_and_chat.py` — full lifecycle demo
  - `streaming.py` — streaming chat completions
  - `async_client.py` — `AsyncClient` usage
  - `openai_compat.py` — using the official `openai` SDK directly
- New `docs/cold-starts.md` guide explaining KServe scale-to-zero
  behavior, 503 detection, and the SDK's `auto_wake` knobs.

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
