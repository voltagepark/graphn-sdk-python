"""Full custom-model lifecycle E2E test for the Graphn Python SDK.

Exercises the canonical customer journey end-to-end against real
``cp.graphn.ai`` and ``model.graphn.ai``:

    1. validate       — check the HF model is importable
    2. create         — start the import + deployment
    3. wait_until_ready — poll until the model is serving
    4. list           — confirm the new model appears in the workspace
    5. get            — fetch the model by id and inspect it
    6. chat.completions.create — run a real inference round-trip
    7. delete         — clean up

Defaults to the smallest reasonable model
(``Qwen/Qwen2.5-0.5B-Instruct``, ~1 GB) so deploys finish in a few
minutes. Override with ``--hf-model``.

Usage:
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \\
        python scripts/e2e.py [--hf-model ID] [--name NAME] [--keep]

Exit codes:
    0  full lifecycle succeeded
    1  any step failed (full traceback printed; cleanup still attempted)
    2  required env vars missing
"""

from __future__ import annotations

import argparse
import os
import sys
import time
import traceback
import uuid

import graphn

DEFAULT_HF_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"
DEFAULT_TIMEOUT_SECONDS = 1800.0
DEFAULT_POLL_INTERVAL_SECONDS = 10.0


def _hdr(label: str) -> None:
    print(f"\n=== {label} ===", flush=True)


def _ok(label: str, detail: str = "") -> None:
    msg = f"  [ok] {label}"
    if detail:
        msg += f" — {detail}"
    print(msg, flush=True)


def _info(msg: str) -> None:
    print(f"  ... {msg}", flush=True)


def _fail(label: str, exc: BaseException) -> None:
    print(f"  [FAIL] {label}", flush=True)
    traceback.print_exception(type(exc), exc, exc.__traceback__)


def _safe_delete(client: graphn.Client, model_id: str) -> None:
    print(f"\n  [cleanup] deleting custom model {model_id}", flush=True)
    try:
        client.custom_models.delete(model_id)
        _ok("cleanup", f"deleted {model_id}")
    except Exception as exc:
        _fail("cleanup", exc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--hf-model",
        default=DEFAULT_HF_MODEL,
        help=f"HuggingFace model id to import (default: {DEFAULT_HF_MODEL}).",
    )
    parser.add_argument(
        "--name",
        default=None,
        help="Custom model name. Defaults to sdk-e2e-<timestamp>.",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="Skip the final delete step (useful for inspection).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"Wait timeout in seconds (default: {DEFAULT_TIMEOUT_SECONDS:g}).",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=DEFAULT_POLL_INTERVAL_SECONDS,
        help=f"Poll interval in seconds (default: {DEFAULT_POLL_INTERVAL_SECONDS:g}).",
    )
    parser.add_argument(
        "--skip-validate",
        action="store_true",
        help="Skip the pre-create validate() call.",
    )
    args = parser.parse_args()

    if not os.environ.get("GRAPHN_API_KEY"):
        print("error: GRAPHN_API_KEY is not set", file=sys.stderr)
        return 2
    if not os.environ.get("GRAPHN_WORKSPACE_ID"):
        print("error: GRAPHN_WORKSPACE_ID is not set", file=sys.stderr)
        return 2

    name = args.name or f"sdk-e2e-{uuid.uuid4().hex[:8]}"
    started = time.monotonic()
    created_id: str | None = None
    failed = False

    with graphn.Client() as client:
        _hdr("Setup")
        _ok("client", f"workspace={client.workspace_id} cp={client.base_url}")
        _ok("inference", client.inference_url)
        _info(f"will import HF model {args.hf_model!r} as {name!r}")

        _hdr("Step 0: access check")
        try:
            access = client.custom_models.access()
        except Exception as exc:
            _fail("custom_models.access", exc)
            return 1
        if not getattr(access, "allowed", False):
            print("  [FAIL] workspace is not allowlisted for custom models")
            return 1
        _ok("custom_models.access", "allowed=True")

        if not args.skip_validate:
            _hdr("Step 1: validate (pre-flight)")
            try:
                v = client.custom_models.validate(huggingface_model_id=args.hf_model)
            except Exception as exc:
                _fail("custom_models.validate", exc)
                return 1
            _ok(
                "custom_models.validate",
                f"valid={getattr(v, 'valid', '?')} "
                f"architectures={getattr(v, 'architectures', None)} "
                f"params={getattr(v, 'num_params', None)} "
                f"est_mem_gb={getattr(v, 'estimated_memory_gb', None)}",
            )
            if not v.valid:
                print(f"  [FAIL] validate said the model is not importable: {v.error}")
                return 1

        _hdr("Step 2: create")
        try:
            model = client.custom_models.create(
                name=name,
                huggingface_model_id=args.hf_model,
                weight_source="huggingface",
            )
            created_id = model.id
        except Exception as exc:
            _fail("custom_models.create", exc)
            return 1
        _ok(
            "custom_models.create",
            f"id={model.id} status={model.status} weight_source={model.weight_source}",
        )

        _hdr(f"Step 3: wait_until_ready (timeout={args.timeout:g}s)")
        deploy_started = time.monotonic()
        last_status: str | None = None

        try:
            deadline = time.monotonic() + args.timeout
            while True:
                m = client.custom_models.refresh(created_id)
                if m.status != last_status:
                    elapsed = time.monotonic() - deploy_started
                    _info(f"[{elapsed:6.1f}s] status={m.status!r}")
                    last_status = m.status
                if m.status in ("ready", "failed"):
                    if m.status == "failed":
                        print(f"  [FAIL] deployment failed: {m.error_message!r}")
                        failed = True
                    else:
                        elapsed = time.monotonic() - deploy_started
                        _ok(
                            "wait_until_ready",
                            f"ready in {elapsed:.1f}s endpoint={m.endpoint!r}",
                        )
                    break
                if time.monotonic() >= deadline:
                    print(
                        f"  [FAIL] timed out after {args.timeout:g}s "
                        f"(last status: {m.status!r})"
                    )
                    failed = True
                    break
                time.sleep(args.poll_interval)
        except Exception as exc:
            _fail("wait_until_ready", exc)
            failed = True

        if failed:
            if created_id and not args.keep:
                _safe_delete(client, created_id)
            return 1

        _hdr("Step 4: list (verify model appears)")
        try:
            models = list(client.custom_models.list(limit=50))
        except Exception as exc:
            _fail("custom_models.list", exc)
            failed = True
        else:
            ids = [m.id for m in models]
            if created_id in ids:
                _ok("custom_models.list", f"{len(models)} total, includes {created_id}")
            else:
                print(
                    f"  [FAIL] {created_id} not in list response: {ids}",
                    flush=True,
                )
                failed = True

        _hdr("Step 5: get (round-trip by id)")
        try:
            fetched = client.custom_models.get(created_id)
        except Exception as exc:
            _fail("custom_models.get", exc)
            failed = True
        else:
            if fetched.id != created_id:
                print(f"  [FAIL] get returned wrong id: {fetched.id}")
                failed = True
            else:
                _ok(
                    "custom_models.get",
                    f"id={fetched.id} status={fetched.status} "
                    f"endpoint={fetched.endpoint!r} "
                    f"capabilities={fetched.capabilities}",
                )

        _hdr("Step 6: list inference models (gateway-side)")
        try:
            inf_models = client.models.list()
        except Exception as exc:
            _fail("models.list", exc)
            failed = True
        else:
            ids = [m.id for m in inf_models]
            _ok("models.list", f"{len(ids)} models — first few: {ids[:5]}")

        _hdr("Step 7: chat.completions.create (non-streaming)")
        chat_model_id = fetched.id
        _info(
            f"using model={chat_model_id!r} (the SDK adds the gateway's "
            "'custom:' routing prefix internally); auto_wake will spin "
            "the model up if it's scaled to zero"
        )

        chat_started = time.monotonic()
        try:
            resp = client.chat.completions.create(
                model=chat_model_id,
                messages=[
                    {
                        "role": "system",
                        "content": "You answer in one short sentence.",
                    },
                    {"role": "user", "content": "Say hello."},
                ],
                max_tokens=64,
                temperature=0.0,
                wake_timeout=600.0,
            )
        except Exception as exc:
            _fail(
                f"chat.completions.create({chat_model_id})",
                exc,
            )
            failed = True
            resp = None
        else:
            _ok(
                "chat.completions.create",
                f"first response in {time.monotonic() - chat_started:.1f}s",
            )

        if resp is not None:
            choices = getattr(resp, "choices", [])
            content = (
                choices[0].message.content if choices and choices[0].message else None
            )
            usage = getattr(resp, "usage", None)
            _ok("chat.completions.create", f"reply={content!r}")
            if usage is not None:
                _ok(
                    "chat.completions.create:usage",
                    f"prompt={getattr(usage, 'prompt_tokens', '?')} "
                    f"completion={getattr(usage, 'completion_tokens', '?')} "
                    f"total={getattr(usage, 'total_tokens', '?')}",
                )

        _hdr("Step 8: chat.completions.create (streaming)")
        try:
            chunks: list[str] = []
            stream = client.chat.completions.create(
                model=chat_model_id,
                messages=[{"role": "user", "content": "Count to three."}],
                max_tokens=64,
                stream=True,
            )
            for chunk in stream:
                ch = getattr(chunk, "choices", [])
                if ch:
                    delta = getattr(ch[0], "delta", None)
                    content = getattr(delta, "content", None) if delta else None
                    if content:
                        chunks.append(content)
            text = "".join(chunks)
        except Exception as exc:
            _fail("chat.completions.create(stream=True)", exc)
            failed = True
        else:
            _ok("streaming chat", f"reply={text!r} ({len(chunks)} chunks)")

        if not args.keep and created_id is not None:
            _safe_delete(client, created_id)
        elif args.keep:
            print(f"\n  [keep] not deleting {created_id} (use the SDK to clean up later)")

    elapsed = time.monotonic() - started
    print()
    print("=" * 60)
    if failed:
        print(f"  [FAIL] E2E failed after {elapsed:.1f}s")
        return 1
    print(f"  [ok] full E2E lifecycle succeeded in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
