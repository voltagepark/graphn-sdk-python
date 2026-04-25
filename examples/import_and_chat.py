"""Import a HuggingFace model and chat with it — the canonical flow.

Usage:
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \
        python examples/import_and_chat.py

What this script does, in plain terms:
    1. Optionally validate the HF model is importable.
    2. Create the custom model (kicks off the import + deployment).
    3. Wait until the deployment is "ready".
    4. Run a chat completion. The first call after a cold period will
       transparently wake the model and retry; you don't have to know
       or care about the gateway's autoscaling internals.
    5. Delete the model so we don't leave anything behind.

If you want to keep the model around after the script (so subsequent
calls don't pay the cold-start cost), pass --keep.
"""

from __future__ import annotations

import argparse
import time

import graphn


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--hf-model",
        default="Qwen/Qwen3-0.6B",
        help="HuggingFace model id to import (default: Qwen/Qwen3-0.6B).",
    )
    parser.add_argument(
        "--prompt",
        default="In one sentence, what is a Markov chain?",
        help="Prompt to send the model.",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="Skip the final delete step (model stays in your workspace).",
    )
    args = parser.parse_args()

    name = f"example-{int(time.time())}"

    with graphn.Client() as c:
        print(f"importing {args.hf_model!r} as {name!r} ...", flush=True)
        model = c.custom_models.create(
            name=name,
            huggingface_model_id=args.hf_model,
            weight_source="huggingface",
        )
        print(f"  created {model.id} (status={model.status})", flush=True)

        print("  waiting for deployment to be ready ...", flush=True)
        model = c.custom_models.wait_until_ready(model.id, timeout=1800)
        print(f"  ready in status={model.status}", flush=True)

        print("\nchatting (auto_wake handles cold start, may take a few min) ...")
        resp = c.chat.completions.create(
            model=model.qualified_name,
            messages=[{"role": "user", "content": args.prompt}],
            max_tokens=120,
            temperature=0.0,
            wake_timeout=600,
        )
        print(f"\nQ: {args.prompt}\nA: {resp.choices[0].message.content}\n")

        if args.keep:
            print(f"keeping model {model.id} (delete with: client.custom_models.delete)")
        else:
            c.custom_models.delete(model.id)
            print(f"cleaned up {model.id}")


if __name__ == "__main__":
    main()
