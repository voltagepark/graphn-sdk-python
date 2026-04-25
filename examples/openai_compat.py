"""Calling Graphn from the official `openai` Python SDK.

The Graphn inference gateway speaks OpenAI-compatible HTTP, so any
existing OpenAI-shaped client code works against it with three
changes:

    1. base_url     -> https://model.graphn.ai/v1
    2. api_key      -> your Graphn API key (gn_...)
    3. Set X-Workspace-Id as a default header.

Use this pattern when you're migrating a codebase that already
depends on `openai` and you don't want to introduce a second SDK.

Tradeoffs vs. graphn.Client:
    + Zero new dependencies if you already use openai.
    + Familiar surface for anyone who's used OpenAI.
    - You lose the lifecycle layer (custom_models, secrets, etc.).
    - You lose auto-wake — first request after scale-to-zero is
      your problem, not the SDK's.
    - Model addressing is your problem too: pass `custom:cm_<id>`
      explicitly, not the bare model name.

Usage:
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \
        python examples/openai_compat.py --model custom:cm_xxx
"""

from __future__ import annotations

import argparse
import os
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--model",
        required=True,
        help="Model id as the gateway expects it (e.g. 'custom:cm_abc123').",
    )
    parser.add_argument(
        "--prompt",
        default="Say hello in one short sentence.",
    )
    args = parser.parse_args()

    try:
        from openai import OpenAI
    except ImportError:
        print("install openai first: pip install openai", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(
        api_key=os.environ["GRAPHN_API_KEY"],
        base_url=(
            os.environ.get("GRAPHN_INFERENCE_URL", "https://model.graphn.ai") + "/v1"
        ),
        default_headers={"X-Workspace-Id": os.environ["GRAPHN_WORKSPACE_ID"]},
    )

    resp = client.chat.completions.create(
        model=args.model,
        messages=[{"role": "user", "content": args.prompt}],
    )
    print(resp.choices[0].message.content)


if __name__ == "__main__":
    main()
