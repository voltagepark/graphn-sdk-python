# graphn — Python SDK

Official Python SDK for the [Graphn API](https://docs.graphn.ai/api):
custom-model lifecycle, secrets management, and OpenAI-compatible
inference (chat completions, model listing, text-to-speech) — all
behind a single typed client.

The SDK is generated from the public OpenAPI 3.1 spec served at
`https://cp.graphn.ai/openapi.yaml`. Inference calls delegate to the
official [`openai`](https://github.com/openai/openai-python) Python SDK
so you get full feature parity (tools, streaming, structured outputs,
etc.) for free.

## Install

```bash
pip install graphn
```

Requires Python 3.10+.

## Quickstart

```python
from graphn import Client

client = Client(api_key="gn_...", workspace_id="ws_abc")

secret = client.secrets.create(name="hf-token", value="hf_...")

model = client.custom_models.create(
    name="my-llama",
    huggingface_model_id="meta-llama/Llama-3-8B",
    hf_token_secret_id=secret.id,
)

client.custom_models.wait_until_ready(model.id, timeout=900)

resp = client.chat.completions.create(
    model=model.name,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(resp.choices[0].message.content)
```

The async variant is identical:

```python
import asyncio
from graphn import AsyncClient

async def main() -> None:
    async with AsyncClient(api_key="gn_...", workspace_id="ws_abc") as client:
        async for model in client.custom_models.list():
            print(model.id, model.status)

asyncio.run(main())
```

## What's in here

| Module                       | Purpose                                                          |
| ---------------------------- | ---------------------------------------------------------------- |
| `graphn.Client`              | Sync entrypoint                                                  |
| `graphn.AsyncClient`         | Async entrypoint                                                 |
| `client.custom_models`       | Create / list / get / delete / wake / refresh / wait_until_ready |
| `client.secrets`             | CRUD for HuggingFace tokens and similar workspace secrets        |
| `client.chat.completions`    | OpenAI-compatible chat completions (delegates to `openai`)       |
| `client.models`              | List models available to the workspace                           |
| `client.tts`                 | Text-to-speech                                                   |
| `client.imported_models`     | Discover and test connections to imported (BYO) inference hosts  |

## Configuration

| Argument        | Default                              | Notes                                                   |
| --------------- | ------------------------------------ | ------------------------------------------------------- |
| `api_key`       | `GRAPHN_API_KEY` env var             | Bearer token starting with `gn_`. Required.             |
| `workspace_id`  | `GRAPHN_WORKSPACE_ID` env var        | Injected into control-plane paths and `X-Workspace-Id`. |
| `base_url`      | `https://cp.graphn.ai`               | Control-plane host.                                     |
| `inference_url` | `https://model.graphn.ai`            | Inference host (passed to the underlying OpenAI client).|
| `timeout`       | `60.0` seconds                       | Per-request HTTPX timeout.                              |
| `max_retries`   | `2`                                  | Retries on connect / 5xx / 429.                         |

## Generating clients in other languages

The OpenAPI spec is the source of truth. To generate a client in
another language, point your favorite generator at:

```
https://cp.graphn.ai/openapi.yaml
```

We test compatibility with `openapi-generator` 6.0+, `openapi-python-client`
0.21+, and `oapi-codegen` 2.0+.

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
ruff check src tests
pytest
```

To regenerate the typed transport layer from the upstream spec:

```bash
./scripts/regenerate.sh
```

## License

Apache 2.0 — see [LICENSE](LICENSE).
