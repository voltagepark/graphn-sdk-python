# graphn SDK examples

Self-contained, runnable scripts that exercise the `graphn` Python
SDK against a real Graphn workspace. Each one is meant to be
copied + pasted into your editor and modified — they're not part of
the SDK's test suite.

> **v0.1.x covers custom-model import (HuggingFace + S3) and
> OpenAI-compatible inference only.** Agents, knowledge bases,
> workflows, evals, datasets, and guardrails are not yet exposed
> through this SDK — see the main
> [README scope section](../README.md#scope) for the full list of
> what's in / out.

## Running

All examples expect the workspace credentials in the environment:

```bash
export GRAPHN_API_KEY=gn_...
export GRAPHN_WORKSPACE_ID=ws_...
pip install graphn

python examples/import_and_chat.py
```

## What's here

| Example | What it shows |
|---|---|
| [`import_and_chat.py`](import_and_chat.py) | Full lifecycle from HuggingFace: validate → create → wait → chat → delete. The "hello world" of the SDK. |
| [`import_from_s3.py`](import_from_s3.py) | Import weights from S3 — presigned URL or assume-role flavor — then chat. |
| [`streaming.py`](streaming.py) | Streaming chat completions (server-sent events). |
| [`async_client.py`](async_client.py) | Async equivalent of `import_and_chat.py` using `graphn.AsyncClient`. |
| [`openai_compat.py`](openai_compat.py) | Calling Graphn from the official `openai` Python SDK directly, for migrating existing code. |

If you want to add an example, keep it under ~80 lines, self-contained,
and runnable with a single `python examples/your_example.py`.
