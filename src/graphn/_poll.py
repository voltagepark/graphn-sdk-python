"""Bounded polling used by wait helpers (executions, ingest, custom models)."""

from __future__ import annotations

import asyncio
import time
from collections.abc import Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")


def poll_until(
    fetch: Callable[[], T],
    *,
    done: Callable[[T], bool],
    timeout: float,
    interval: float,
    timeout_message: Callable[[T], str],
) -> T:
    deadline = time.monotonic() + timeout
    while True:
        item = fetch()
        if done(item):
            return item
        if time.monotonic() >= deadline:
            raise TimeoutError(timeout_message(item))
        time.sleep(interval)


async def apoll_until(
    fetch: Callable[[], Awaitable[T]],
    *,
    done: Callable[[T], bool],
    timeout: float,
    interval: float,
    timeout_message: Callable[[T], str],
) -> T:
    deadline = time.monotonic() + timeout
    while True:
        item = await fetch()
        if done(item):
            return item
        if time.monotonic() >= deadline:
            raise TimeoutError(timeout_message(item))
        await asyncio.sleep(interval)
