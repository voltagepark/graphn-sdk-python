"""Async equivalent of import_and_chat.py.

Demonstrates graphn.AsyncClient end-to-end. Useful if you're already
in an asyncio event loop (e.g. FastAPI route handler, Celery worker
with aio support, agent framework).

Usage:
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \
        python examples/async_client.py
"""

from __future__ import annotations

import argparse
import asyncio
import time

import graphn


async def run(hf_model: str, prompt: str, keep: bool) -> None:
    name = f"async-example-{int(time.time())}"

    async with graphn.AsyncClient() as c:
        print(f"importing {hf_model!r} as {name!r} ...", flush=True)
        model = await c.custom_models.create(
            name=name,
            huggingface_model_id=hf_model,
            weight_source="huggingface",
        )
        print(f"  created {model.id}", flush=True)

        print("  waiting for ready ...", flush=True)
        model = await c.custom_models.wait_until_ready(model.id, timeout=1800)
        print(f"  ready ({model.status})", flush=True)

        print("  listing custom models in this workspace:", flush=True)
        async for m in c.custom_models.list():
            print(f"    - {m.id}  {m.name}  {m.status}")

        print("\nchatting ...", flush=True)
        resp = await c.chat.completions.create(
            model=model.qualified_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=120,
            wake_timeout=600,
        )
        print(f"\nQ: {prompt}\nA: {resp.choices[0].message.content}\n")

        if not keep:
            await c.custom_models.delete(model.id)
            print(f"cleaned up {model.id}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hf-model", default="Qwen/Qwen3-0.6B")
    parser.add_argument("--prompt", default="What's a neural network in one sentence?")
    parser.add_argument("--keep", action="store_true")
    args = parser.parse_args()
    asyncio.run(run(args.hf_model, args.prompt, args.keep))


if __name__ == "__main__":
    main()
