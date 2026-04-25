"""Streaming chat completions.

Streams tokens from a model already deployed in your workspace.
Pass --model to point at a specific model id; otherwise uses the
first custom model returned by the gateway.

Usage:
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \
        python examples/streaming.py --model cm_xxx
"""

from __future__ import annotations

import argparse
import sys

import graphn


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--model",
        help=(
            "Model identifier (e.g. 'cm_abc123' for a custom model, "
            "or 'meta-llama/Llama-3.1-8B-Instruct' for a first-party "
            "model). Defaults to the first custom model in your "
            "workspace."
        ),
    )
    parser.add_argument(
        "--prompt",
        default="Write a haiku about distributed systems.",
        help="Prompt to send.",
    )
    args = parser.parse_args()

    with graphn.Client() as c:
        model_id = args.model
        if model_id is None:
            for m in c.custom_models.list(limit=1):
                model_id = m.id
                break
            if model_id is None:
                print("no custom models in this workspace; pass --model", file=sys.stderr)
                sys.exit(1)

        print(f"streaming from {model_id} ...\n", flush=True)
        stream = c.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": args.prompt}],
            max_tokens=200,
            stream=True,
            wake_timeout=600,
        )
        for chunk in stream:
            choices = chunk.choices or []
            if not choices:
                continue
            delta = choices[0].delta.content
            if delta:
                print(delta, end="", flush=True)
        print()


if __name__ == "__main__":
    main()
