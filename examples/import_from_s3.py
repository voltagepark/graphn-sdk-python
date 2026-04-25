"""Import a model from S3 (presigned URL or assume-role) and chat with it.

Usage:
    # Presigned URL (default)
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \
        python examples/import_from_s3.py \
            --hf-model-id Qwen/Qwen3-0.6B \
            --s3-url 'https://my-bucket.s3.amazonaws.com/qwen3-0.6b.tar.gz?X-Amz-...'

    # Assume-role
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \
        python examples/import_from_s3.py \
            --hf-model-id meta-llama/Llama-3.1-8B-Instruct \
            --weight-source s3_assume_role \
            --s3-url s3://my-bucket/llama-3.1-8b.tar.gz \
            --s3-role-arn arn:aws:iam::123456789012:role/GraphnImport

The lifecycle past `create` is identical to a HuggingFace import:
wait until ready, run chat completions, optionally clean up. The
weight source only matters at import time.

Note: --hf-model-id is required for S3 imports too. It is the
canonical identifier the inference endpoint advertises and the
value you pass in `model` for chat completions, so without it
the deployed model has no stable name to address. Use the
upstream org/model-name your weights are based on.
"""

from __future__ import annotations

import argparse
import time

import graphn


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--weight-source",
        choices=["s3_presigned", "s3_assume_role"],
        default="s3_presigned",
        help="How Graphn should authenticate to S3 (default: s3_presigned).",
    )
    parser.add_argument(
        "--hf-model-id",
        required=True,
        help=(
            "Canonical model identifier in 'org/model-name' form (e.g. "
            "Qwen/Qwen3-0.6B). Required: this is the name the inference "
            "endpoint advertises and the value you pass in `model` for "
            "chat completions."
        ),
    )
    parser.add_argument(
        "--s3-url",
        required=True,
        help=(
            "Presigned HTTPS URL (s3_presigned) or s3:// URI (s3_assume_role) "
            "pointing at a SINGLE .tar.gz archive whose top level is the "
            "model directory (config.json, tokenizer*, weights)."
        ),
    )
    parser.add_argument(
        "--s3-role-arn",
        default=None,
        help="IAM role ARN for s3_assume_role mode. Required when "
        "--weight-source s3_assume_role.",
    )
    parser.add_argument(
        "--prompt",
        default="In one sentence, what is a Markov chain?",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="Skip the final delete step.",
    )
    args = parser.parse_args()

    if args.weight_source == "s3_assume_role" and not args.s3_role_arn:
        parser.error("--s3-role-arn is required when --weight-source s3_assume_role")

    name = f"example-s3-{int(time.time())}"

    with graphn.Client() as c:
        print(f"importing from {args.weight_source} as {name!r} ...", flush=True)
        model = c.custom_models.create(
            name=name,
            weight_source=args.weight_source,
            huggingface_model_id=args.hf_model_id,
            s3_url=args.s3_url,
            s3_role_arn=args.s3_role_arn,
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
