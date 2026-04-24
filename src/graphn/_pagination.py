"""Cursor-based pagination iterators.

The Graphn ``*List`` responses (``CustomModelList``, ``SecretList``,
``ModelList``, ...) return ``items``, ``count``, and an optional
``continue_token``. These helpers turn that into ``for`` / ``async for``
loops that transparently fetch additional pages.

The full implementation lands with the ``sdk-client-core`` task; this
stub provides the public types so :mod:`graphn` can re-export them.
"""

from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class _PageBase:
    """Shared metadata for sync and async page iterators."""

    __slots__ = ("_continue_token",)

    def __init__(self, continue_token: str | None = None) -> None:
        self._continue_token = continue_token

    @property
    def has_more(self) -> bool:
        """Whether the server has more pages after this one."""

        return bool(self._continue_token)


class SyncPage(_PageBase, Generic[T]):
    """Iterable page of items returned by a synchronous list call."""


class AsyncPage(_PageBase, Generic[T]):
    """Async-iterable page of items returned by an async list call."""
