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

## [0.1.6] — 2026-05-21

Spec-sync release plus a matching round of ergonomic wrappers. Picks
up two new custom-model control-plane endpoints, exposes them
through `client.custom_models`, and adds typed LoRA-adapter fields
to the public `CustomModel` and `ValidateModelResponse` Pydantic
models. The low-level generated client (`graphn._generated`) and
the hand-curated resource layer (`graphn.custom_models`) are both
fully in sync with the upstream OpenAPI spec.

### Added

- `client.custom_models.update(model_id, *, name=..., min_replicas=...,
 max_replicas=..., cooldown_seconds=..., extra=...)` (sync and async).
 Issues `PATCH /v1/{workspaceId}/custom-models/{modelId}` against the
 control plane and returns the refreshed :class:`CustomModel`.
 Mutates a vetted set of post-create fields in place against the
 live deployment — no rolling restart, no downtime. Immutable fields
 (`huggingface_model_id`, `weight_source`, GPU topology, …) are not
 exposed; change them by deleting and re-creating the model. The SDK
 refuses an empty PATCH client-side (raises
 `graphn.ValidationError` with code `empty_update`), one round-trip
 earlier than the server's `422`.
- `client.custom_models.supported_architectures()` (sync and async).
 Returns a typed :class:`SupportedArchitectures` catalog of model
 architectures the platform's serving runtimes can deploy, each
 annotated with the capability tags (`tool_calling`, `vision`,
 `image_input`, `video_input`, `streaming`, `json_mode`) it exposes.
 Intended for driving architecture/capability filters in client UIs
 before calling :meth:`client.custom_models.validate`. The list is
 updated alongside platform runtime upgrades; clients should not
 cache it across build cycles.
- LoRA-adapter visibility on the existing types. `CustomModel` gains
 `artifact_type` (`Literal["base", "lora"] | None`), `base_model_id`,
 `lora_adapter_name`, and `lora_rank` typed fields; older control
 planes that predate the LoRA work leave `artifact_type` unset and
 should be treated as `"base"` for compatibility. `ValidateModelResponse`
 gains `artifact_type`, `detected_base_model_id`, and `lora_rank` so
 callers can detect that a HuggingFace repo contains a LoRA adapter
 (via `adapter_config.json`) before deploying. When
 `artifact_type == "lora"` on the validate response, the
 `architectures` / `num_params` / `estimated_memory_gb` /
 `max_context_length` fields describe the **base** model resolved
 from `adapter_config.json`, not the adapter itself.
- `client.custom_models.create(..., base_model_id=...)` (sync and async).
 Required on `weight_source=s3_*` LoRA imports — it's the only way to
 classify the bundle as an adapter at create time; omitting it routes
 the import through the base path, and a LoRA bundle that wasn't
 declared will deploy to `failed` with an actionable error. Optional
 on `weight_source=huggingface`, where it **overrides**
 `adapter_config.json::base_model_name_or_path` from the upstream
 adapter repo — useful when the recorded base id isn't a valid
 HuggingFace id (e.g. a local filesystem path used during training).
 The base id must be one of the platform's allowlisted bases (see
 `client.custom_models.supported_architectures()`).
- `client.custom_models.validate(..., model_size_gb=...)` (sync and
 async). Optional caller-supplied estimate (in GiB) of the on-disk
 weights size. When provided, the platform sizes the model-weights
 PVC from this hint instead of waiting for a HuggingFace head-bytes
 probe; useful for very large models (e.g. 405B) where the probe
 would otherwise stall the validate response.
- New public exports from `graphn`: `ArchitectureInfo`,
 `SupportedArchitectures`, `ArtifactType`.

### Changed

- `CustomModelCreate.huggingface_model_id` is now a **required**
 field on the generated `attrs` dataclass (previously
 `str | Unset`). This mirrors the server-side behavior already
 shipped in v0.1.3 (the control plane has returned `422` for omitted
 `huggingface_model_id` on every weight source since
 voltagepark/takao#1997) and the client-side `ValidationError` the
 high-level `client.custom_models.create` resource has raised since
 v0.1.3. The generated type just catches up; callers using the
 hand-curated `client.custom_models.create` keyword-only API are
 unaffected — the high-level resource still accepts
 `huggingface_model_id` as a keyword argument and the existing
 client-side guard fires before the request is built.
- `CustomModelCreate.s3_role_arn` docstring now records the
 `graphn-byom-*` role-name prefix the platform enforces. No wire or
 validation change in the SDK; the constraint has been server-side
 since 0.1.3 and the customer-facing CloudFormation template
 enforces the same prefix at stack-create time. Doc-only.
- `CustomModel.gpu_memory_utilization` docstring no longer names the
 serving engine (`vLLM`). Engine-agnostic wording aligns with the
 0.1.3 scrub of customer-facing serving-engine references.

## [0.1.5] — 2026-05-14

Patch release. Widens the upper bound on the `openai` runtime
dependency so this SDK installs cleanly alongside projects that have
already upgraded to `openai>=2`. No behavior changes; no spec
changes.

### Changed

- `openai` dependency bound from `<2` to `<3`. The SDK only uses
  `chat.completions.create` and `models` (plus the `OpenAI` /
  `AsyncOpenAI` clients and the `AuthenticationError` /
  `InternalServerError` exception classes), all of which are
  unchanged across the 1.x → 2.x boundary. The single `openai` 2.0.0
  breaking change is in the Responses API
  (`ResponseFunctionToolCallOutputItem.output` /
  `ResponseCustomToolCallOutput.output` now accept array forms in
  addition to strings), which this SDK does not touch. The full
  test suite (`pytest -ra`, 43 tests) passes against `openai==2.36.0`
  with no source changes.

  Customers pinned to `openai<2` keep working unchanged. Customers
  on `openai>=2` can now install `graphn` without resolver
  conflicts.

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
