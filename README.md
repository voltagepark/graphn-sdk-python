# graphn — Python SDK

[![PyPI](https://img.shields.io/pypi/v/graphn.svg)](https://pypi.org/project/graphn/)
[![Python](https://img.shields.io/pypi/pyversions/graphn.svg)](https://pypi.org/project/graphn/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Tests](https://github.com/voltagepark/graphn-sdk-python/actions/workflows/test.yml/badge.svg)](https://github.com/voltagepark/graphn-sdk-python/actions/workflows/test.yml)

The official Python SDK for [Graphn](https://graphn.ai). Import any
LLM — from HuggingFace or your own S3 bucket — into your workspace,
get an OpenAI-compatible inference endpoint, and call it from Python
in a handful of lines, without standing up a single GPU yourself.

> **v0.1.x scope** — This release line covers **custom-model import
> (HuggingFace + S3) and OpenAI-compatible inference** end-to-end.
> A lot of the broader Graphn platform
> (agents, knowledge bases, workflows, evals, datasets, guardrails,
> billing, full BYO-inference CRUD, etc.) is **not yet exposed**
> through this SDK. Those surfaces will be added in subsequent
> minor releases as their HTTP APIs stabilize. See
> [Scope](#scope) below for the exact list.

```python
import graphn

with graphn.Client() as c:
    model = c.custom_models.create(
        name="my-llama",
        huggingface_model_id="Qwen/Qwen3-0.6B",
        weight_source="huggingface",
    )
    c.custom_models.wait_until_ready(model.id)

    resp = c.chat.completions.create(
        model=model.qualified_name,
        messages=[{"role": "user", "content": "Hello!"}],
    )
    print(resp.choices[0].message.content)
```

That's it. Cold-start, retry, OpenAI-compatible serialization, and
the `custom:<id>` addressing convention are all handled for you.

## Install

```bash
pip install graphn
```

Requires Python 3.10+. Tested on 3.10, 3.11, 3.12, 3.13.

## Authentication

The SDK reads credentials from the environment by default:

```bash
export GRAPHN_API_KEY=gn_...           # required
export GRAPHN_WORKSPACE_ID=ws_...      # required
export GRAPHN_BASE_URL=https://cp.graphn.ai      # optional
export GRAPHN_INFERENCE_URL=https://model.graphn.ai  # optional
```

Or pass them explicitly:

```python
client = graphn.Client(api_key="gn_...", workspace_id="ws_...")
```

Get an API key from the [Graphn dashboard](https://graphn.ai).

## Scope

### What's in the box (v0.1.x)

| Module | What it does |
|---|---|
| `client.custom_models` | Import models from HuggingFace, S3 presigned URLs, or S3 + IAM role; list, get, refresh, wake, delete, `wait_until_ready`, validate |
| `client.secrets` | CRUD for workspace secrets (HuggingFace tokens, etc) |
| `client.chat.completions` | OpenAI-compatible chat completions, streaming + non-streaming, **with auto-wake on cold start** |
| `client.models` | List models served by the gateway |
| `client.tts` | Text-to-speech: list voices, synthesize |
| `client.imported_models` | Discover and probe BYO inference endpoints (read-only, no full CRUD yet) |

Both `graphn.Client` and `graphn.AsyncClient` exist with identical APIs.

### What's *not* in the box yet

The Graphn platform is broader than what's exposed here. The
following surfaces exist on the platform but do **not** have SDK
coverage in v0.1.x — file an issue on the
[SDK repo](https://github.com/voltagepark/graphn-sdk-python/issues)
to vote on what you need next:

- **Agents** — defining, running, and inspecting agent workflows
- **Knowledge bases / RAG** — corpus management, retrieval, indexing
- **Workflows** — long-running Temporal-backed orchestration
- **Evals & datasets** — eval suites, dataset upload, run results
- **Guardrails** — policy authoring and inference-time enforcement
- **Imported models (BYO inference) — full CRUD** — only listing
  and probe are exposed today
- **Usage & billing** — usage stats, GPU-hour reporting beyond the
  read-only `client.custom_models.gpu_hours()` helper
- **Workspace / member / API-key administration**

Until they land here, those endpoints can be hit via raw HTTP using
your `gn_...` API key. The control plane is documented at
[graphn.ai/docs/api](https://graphn.ai/docs/api) and the OpenAPI
3.1 spec is mirrored at
[voltagepark/graphn-openapi](https://github.com/voltagepark/graphn-openapi).

## The 80% recipe: import a model and chat with it

```python
import graphn

with graphn.Client() as c:
    # 1. Import the model. Use a workspace secret for gated HF repos.
    model = c.custom_models.create(
        name="my-llama",
        huggingface_model_id="meta-llama/Llama-3.1-8B-Instruct",
        weight_source="huggingface",
        hf_token_secret_id="sec_...",  # optional, only for gated models
    )

    # 2. Wait for the deployment to be live.
    c.custom_models.wait_until_ready(model.id, timeout=1800)

    # 3. Chat. The first call will cold-start the model — the SDK
    #    transparently calls wake() and retries until it serves.
    resp = c.chat.completions.create(
        model=model.qualified_name,   # "custom:cm_..."
        messages=[{"role": "user", "content": "Tell me a joke."}],
        wake_timeout=600,             # max time to wait for cold start
    )
    print(resp.choices[0].message.content)
```

## Importing from S3

If your weights aren't on HuggingFace — fine-tunes, internal models,
licensed checkpoints — import them straight from S3. Two flavors,
both of which still require `huggingface_model_id` (see callout
below).

> **`huggingface_model_id` is required for S3 imports too.** It's
> the canonical identifier for the model: Graphn passes it through
> to vLLM as `--served-model-name`, so it's the name the deployed
> model advertises and the name you address it by under the hood.
> Use the upstream `org/model-name` your weights are based on (e.g.
> `Qwen/Qwen3-0.6B`, `meta-llama/Llama-3.1-8B-Instruct`). This is
> the same "Model ID" field the web UI requires for S3 imports.
> Omitting it raises `graphn.ValidationError` client-side; passing
> it but having a mismatched archive will surface as a deploy
> failure on the model record.

**Presigned URL** (no AWS credentials shared with Graphn):

```python
model = c.custom_models.create(
    name="my-finetune",
    weight_source="s3_presigned",
    huggingface_model_id="meta-llama/Llama-3.1-8B-Instruct",
    s3_url="https://my-bucket.s3.amazonaws.com/llama-3.1-8b.tar.gz?X-Amz-Algorithm=...",
    gpu_count=1,
)
```

Package the weights as a single `.tar.gz` archive whose top level
is the model directory (the same layout `huggingface-cli download`
produces). Generate the URL with `aws s3 presign s3://my-bucket/llama-3.1-8b.tar.gz`
or the AWS SDK; Graphn pulls weights through the URL on import.
The URL only needs to be live for the import window (allow at
least a few minutes for the download), not for the model's
lifetime.

**IAM role assumption** (for buckets you control, longer-lived
credentials):

```python
model = c.custom_models.create(
    name="my-finetune",
    weight_source="s3_assume_role",
    huggingface_model_id="meta-llama/Llama-3.1-8B-Instruct",
    s3_url="s3://my-bucket/llama-3.1-8b.tar.gz",
    s3_role_arn="arn:aws:iam::123456789012:role/GraphnImport",
    gpu_count=1,
)
```

The role's trust policy must allow Graphn's importer principal to
`sts:AssumeRole`; ask support for the principal ARN to put in your
trust policy. Graphn re-assumes on every import / refresh, so
rotating credentials underneath is safe.

Everything past the create call — `wait_until_ready`, chat completions,
auto-wake, `qualified_name` addressing — is identical regardless of
weight source. See [`examples/import_from_s3.py`](examples/import_from_s3.py)
for an end-to-end runnable script.

## Streaming

```python
stream = c.chat.completions.create(
    model=model.qualified_name,
    messages=[{"role": "user", "content": "Count to ten."}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

## Async

```python
import asyncio
import graphn

async def main() -> None:
    async with graphn.AsyncClient() as c:
        async for m in c.custom_models.list():
            print(m.id, m.name, m.status)

        resp = await c.chat.completions.create(
            model="custom:cm_abc123",
            messages=[{"role": "user", "content": "Hi!"}],
        )
        print(resp.choices[0].message.content)

asyncio.run(main())
```

## Cold starts and auto-wake

Graphn custom models default to **scale-to-zero**: a model with no
traffic for `cooldown_seconds` is descheduled, and the first request
afterwards has to wait for the gateway to spin up a fresh replica
(typically 60–600 seconds depending on weight size).

Without help, the first chat request after a cold period returns:

```
503 Service Unavailable: Model is scaled to zero and is now warming up.
```

The SDK detects this, calls `POST /custom-models/{id}/wake` to nudge
the autoscaler, and retries with exponential backoff until the model
serves or `wake_timeout` (default 180s) elapses. **You don't have to
do anything**, but the knobs are there if you want them:

```python
# Disable auto-wake — you handle the 503 yourself.
c.chat.completions.create(model=..., messages=[...], auto_wake=False)

# Give the warm-up more headroom (e.g. for large models).
c.chat.completions.create(model=..., messages=[...], wake_timeout=900)
```

See [`docs/cold-starts.md`](docs/cold-starts.md) for the full story.

## Drop-in for `openai`

The chat path is OpenAI-compatible all the way down — under the hood
we delegate to the official [`openai` Python SDK](https://github.com/openai/openai-python),
configured against the Graphn gateway. So tools, structured outputs,
multi-modal inputs, function calling, etc. all work out of the box.

If you already have OpenAI-shaped code and just want to point it at
a Graphn model:

```python
from openai import OpenAI

client = OpenAI(
    api_key="gn_...",
    base_url="https://model.graphn.ai/v1",
    default_headers={"X-Workspace-Id": "ws_..."},
)
resp = client.chat.completions.create(
    model="custom:cm_...",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

The reason to use `graphn.Client` instead is everything around the
chat call: lifecycle management, secrets, auto-wake, typed responses,
and a stable URL contract.

## More examples

See [`examples/`](examples/) for runnable end-to-end scripts:

- [`examples/import_and_chat.py`](examples/import_and_chat.py) — full lifecycle (HuggingFace)
- [`examples/import_from_s3.py`](examples/import_from_s3.py) — S3 presigned + assume-role import
- [`examples/streaming.py`](examples/streaming.py) — streaming chat
- [`examples/async_client.py`](examples/async_client.py) — async usage
- [`examples/openai_compat.py`](examples/openai_compat.py) — drop-in from `openai`

## Configuration reference

| Argument | Default | Notes |
|---|---|---|
| `api_key` | `$GRAPHN_API_KEY` | Bearer token starting with `gn_`. Required. |
| `workspace_id` | `$GRAPHN_WORKSPACE_ID` | Path parameter + `X-Workspace-Id` header. Required. |
| `base_url` | `https://cp.graphn.ai` | Control plane host. |
| `inference_url` | `https://model.graphn.ai` | Inference / OpenAI-compatible host. |
| `timeout` | `60.0` | Per-request HTTPX timeout (seconds). |
| `max_retries` | `2` | Retries on connect failures, 429, and 5xx. |
| `default_headers` | `{}` | Extra headers added to every request. |

## Generating clients in other languages

The OpenAPI 3.1 spec is the source of truth. It's published at:

- **GitHub** — [voltagepark/graphn-openapi](https://github.com/voltagepark/graphn-openapi)
- **Live HTML reference** — [graphn.ai/docs/api](https://graphn.ai/docs/api)
- **Direct download** — `https://cp.graphn.ai/openapi.yaml`

Point your favorite generator at any of these. We test against
`openapi-generator` 6.0+, `openapi-python-client` 0.21+, and
`oapi-codegen` 2.0+.

## Contributing

```bash
git clone https://github.com/voltagepark/graphn-sdk-python
cd graphn-sdk-python
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'

ruff check src tests
pytest
```

Regenerate the typed transport from the upstream spec after a spec
change:

```bash
./scripts/regenerate.sh
```

See [CHANGELOG.md](CHANGELOG.md) for release notes.

## License

Apache 2.0 — see [LICENSE](LICENSE).
