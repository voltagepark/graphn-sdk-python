"""End-to-end smoke test for the Graphn Python SDK.

Exercises the read-only surface against real cp.graphn.ai +
model.graphn.ai. Designed to be safe to run repeatedly: it does not
create, modify, or delete any resources unless ``--write`` is passed.

Usage:
    GRAPHN_API_KEY=gn_... GRAPHN_WORKSPACE_ID=ws_... \\
        python scripts/smoke.py [--write]

Exit codes:
    0  all checks passed
    1  at least one check failed (full traceback printed)
"""

from __future__ import annotations

import argparse
import os
import sys
import time
import traceback
from collections.abc import Callable
from typing import Any

import graphn

CHECK = "[ok]"
FAIL = "[FAIL]"
SKIP = "[skip]"


def _hdr(name: str) -> None:
    print(f"\n=== {name} ===")


def _ok(label: str, detail: str = "") -> None:
    msg = f"  {CHECK} {label}"
    if detail:
        msg += f" — {detail}"
    print(msg)


def _skip(label: str, reason: str) -> None:
    print(f"  {SKIP} {label} — {reason}")


def _fail(label: str, exc: BaseException) -> None:
    print(f"  {FAIL} {label}")
    print(
        "    "
        + "\n    ".join(traceback.format_exception_only(type(exc), exc))
        .rstrip()
        .splitlines()[-1]
        .splitlines()[0:1][0]
        if False
        else ""
    )
    traceback.print_exc()


def _run(name: str, fn: Callable[[], Any], failures: list[str]) -> Any:
    try:
        result = fn()
    except Exception as exc:
        _fail(name, exc)
        failures.append(name)
        return None
    return result


def smoke_read_only(client: graphn.Client, failures: list[str]) -> None:
    _hdr("Configuration")
    _ok("client constructed", f"workspace={client.workspace_id} base={client.base_url}")
    _ok("inference url", client.inference_url)

    _hdr("Custom-model access check")

    def _access() -> Any:
        return client.custom_models.access()

    access = _run("custom_models.access", _access, failures)
    if access is not None:
        _ok("custom_models.access", f"allowed={getattr(access, 'allowed', '?')}")

    _hdr("Custom models — list")

    def _list_custom() -> Any:
        page = client.custom_models.list(limit=5)
        return list(page)

    custom = _run("custom_models.list", _list_custom, failures)
    if custom is not None:
        _ok("custom_models.list", f"{len(custom)} returned")
        for m in custom[:3]:
            _ok(
                "  model",
                f"id={getattr(m, 'id', '?')} name={getattr(m, 'name', '?')} "
                f"status={getattr(m, 'status', '?')}",
            )

    _hdr("Secrets — list (metadata only)")

    def _list_secrets() -> Any:
        page = client.secrets.list(limit=5)
        return list(page)

    secrets = _run("secrets.list", _list_secrets, failures)
    if secrets is not None:
        _ok("secrets.list", f"{len(secrets)} returned")

    _hdr("Inference — list models")

    def _models() -> Any:
        return client.models.list()

    models = _run("models.list", _models, failures)
    if models is not None:
        ids = [getattr(m, "id", "?") for m in models]
        _ok("models.list", f"{len(ids)} models — first few: {ids[:5]}")

    _hdr("Inference — list TTS voices (skipped: requires --tts-model)")
    _skip("tts.voices", "needs a TTS model id; use scripts/smoke.py --tts-model <id>")


def smoke_chat(client: graphn.Client, failures: list[str]) -> None:
    _hdr("Inference — chat completion (non-streaming)")

    models = None
    try:
        models = client.models.list()
    except Exception as exc:
        _fail("chat: pre-flight models.list", exc)
        failures.append("chat:pre-flight")
        return

    if not models:
        _skip("chat completion", "no models available in this workspace")
        return

    model_id = getattr(models[0], "id", None)
    if not model_id:
        _skip("chat completion", "first model has no id")
        return

    def _chat() -> Any:
        return client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You answer in one short sentence."},
                {"role": "user", "content": "Say hello."},
            ],
            max_tokens=32,
        )

    resp = _run(f"chat.completions.create({model_id})", _chat, failures)
    if resp is not None:
        choices = getattr(resp, "choices", [])
        first = choices[0] if choices else None
        msg = getattr(getattr(first, "message", None), "content", None) if first else None
        _ok("chat.completions.create", f"reply: {msg!r}")


def smoke_streaming_chat(client: graphn.Client, failures: list[str]) -> None:
    _hdr("Inference — chat completion (streaming)")

    models = None
    try:
        models = client.models.list()
    except Exception as exc:
        _fail("streaming chat: pre-flight models.list", exc)
        failures.append("streaming-chat:pre-flight")
        return

    if not models:
        _skip("streaming chat", "no models available")
        return

    model_id = getattr(models[0], "id", None)
    if not model_id:
        _skip("streaming chat", "first model has no id")
        return

    def _stream() -> Any:
        chunks: list[str] = []
        stream = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": "Count to three."}],
            max_tokens=32,
            stream=True,
        )
        for chunk in stream:
            choices = getattr(chunk, "choices", [])
            if choices:
                delta = getattr(choices[0], "delta", None)
                content = getattr(delta, "content", None) if delta else None
                if content:
                    chunks.append(content)
        return "".join(chunks)

    text = _run(f"chat.completions.create(stream=True,{model_id})", _stream, failures)
    if text is not None:
        _ok("streaming chat", f"reply: {text!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Also exercise write paths (chat completions). Read-only otherwise.",
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Also exercise streaming chat (implies --write).",
    )
    args = parser.parse_args()

    if not os.environ.get("GRAPHN_API_KEY"):
        print("error: GRAPHN_API_KEY is not set", file=sys.stderr)
        return 2
    if not os.environ.get("GRAPHN_WORKSPACE_ID"):
        print("error: GRAPHN_WORKSPACE_ID is not set", file=sys.stderr)
        return 2

    failures: list[str] = []
    started = time.monotonic()

    with graphn.Client() as client:
        smoke_read_only(client, failures)
        if args.write or args.stream:
            smoke_chat(client, failures)
        if args.stream:
            smoke_streaming_chat(client, failures)

    elapsed = time.monotonic() - started

    print()
    print("=" * 60)
    if failures:
        print(f"{FAIL} {len(failures)} check(s) failed in {elapsed:.1f}s:")
        for name in failures:
            print(f"   - {name}")
        return 1
    print(f"{CHECK} all checks passed in {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
