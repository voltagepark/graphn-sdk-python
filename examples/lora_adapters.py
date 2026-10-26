"""Serve several LoRA adapters from one shared base.

Usage:
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \
        python examples/lora_adapters.py \
            --adapter my-org/qwen3-8b-support-lora \
            --adapter my-org/qwen3-8b-sql-lora

Creates a shared LoRA base, attaches each adapter, asks every adapter
the same question, then deletes the adapters and the base. Pass --keep
to leave them deployed. Each adapter must be a plain PEFT LoRA trained
on --base with a rank no higher than --max-rank.
"""

from __future__ import annotations

import argparse
import time

import graphn


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="Qwen/Qwen3-8B", help="Hugging Face base model.")
    parser.add_argument("--max-rank", type=int, choices=(16, 64), default=64)
    parser.add_argument(
        "--adapter", action="append", required=True, help="Hugging Face adapter repo."
    )
    parser.add_argument("--prompt", default="In one sentence, what do you do?")
    parser.add_argument("--keep", action="store_true", help="Leave the base and adapters.")
    args = parser.parse_args()

    with graphn.Client() as c:
        base = c.custom_models.create(
            name=f"lora-base-{int(time.time())}",
            huggingface_model_id=args.base,
            lora_enabled=True,
            max_lora_rank=args.max_rank,
        )
        print(f"base {base.id}: waiting for it to be ready ...", flush=True)
        c.custom_models.wait_until_ready(base.id)

        adapters = [
            c.custom_models.adapters.attach(base.id, huggingface_model_id=repo)
            for repo in args.adapter
        ]
        for adapter in adapters:
            adapter = c.custom_models.adapters.wait_until_ready(adapter.id)
            resp = c.chat.completions.create(
                model=adapter.id,
                messages=[{"role": "user", "content": args.prompt}],
                max_tokens=120,
            )
            print(f"\n{adapter.name} ({adapter.id}): {resp.choices[0].message.content}")

        if args.keep:
            print(f"\nkeeping base {base.id} and {len(adapters)} adapter(s)")
            return
        for adapter in adapters:
            c.custom_models.adapters.delete(adapter.id)
        for adapter in adapters:
            c.custom_models.adapters.wait_until_deleted(adapter.id)
        c.custom_models.delete(base.id)
        print(f"\ncleaned up base {base.id}")


if __name__ == "__main__":
    main()
