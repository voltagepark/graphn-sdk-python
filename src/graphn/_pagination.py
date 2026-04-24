"""Cursor-based pagination iterators.

The Graphn ``*List`` responses (``CustomModelList``, ``SecretList``,
``ModelList``) all share the shape::

    {"items": [...], "count": N, "continue_token": "..."}

These helpers turn that into ``for page in pages`` / ``async for page
in pages`` loops as well as flat ``for item in pages`` iteration that
transparently paginates until the server returns no ``continue_token``.

Resource modules build pages with the :func:`build_sync_page` and
:func:`build_async_page` constructors, passing a callable that knows
how to fetch the next page given a ``continue_token``.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Iterator, Mapping
from typing import (
    Any,
    Callable,
    Generic,
    TypeVar,
)

T = TypeVar("T")

PageFetcher = Callable[[str | None], "RawPage[Any]"]
AsyncPageFetcher = Callable[[str | None], Awaitable["RawPage[Any]"]]
ItemBuilder = Callable[[Mapping[str, Any]], T]


class RawPage(Generic[T]):
    """Single page of items returned by the server."""

    __slots__ = ("continue_token", "count", "items")

    def __init__(
        self,
        *,
        items: list[T],
        count: int,
        continue_token: str | None,
    ) -> None:
        self.items = items
        self.count = count
        self.continue_token = continue_token

    @classmethod
    def from_response(
        cls,
        body: Mapping[str, Any],
        item_builder: ItemBuilder[T],
    ) -> RawPage[T]:
        items = [item_builder(item) for item in body.get("items", []) or []]
        # The spec uses ``count`` for ``SecretList`` but ``total`` for
        # ``CustomModelList``; accept either so the same helper works
        # for both.
        count_value = body.get("count")
        if count_value is None:
            count_value = body.get("total", len(items))
        return cls(
            items=items,
            count=int(count_value),
            continue_token=body.get("continue_token"),
        )


class SyncPage(Generic[T]):
    """Auto-paginating iterable returned by synchronous list calls.

    Iteration over the page yields individual items, transparently
    fetching subsequent pages until the server stops returning a
    ``continue_token``. Use :attr:`pages` if you need to handle each
    page explicitly (e.g. to inspect ``count``).
    """

    def __init__(
        self,
        *,
        first: RawPage[T],
        fetch_next: PageFetcher,
    ) -> None:
        self._first = first
        self._fetch_next = fetch_next

    @property
    def has_more(self) -> bool:
        return self._first.continue_token is not None

    @property
    def items(self) -> list[T]:
        """Items in *this* page only (does not auto-paginate)."""

        return list(self._first.items)

    @property
    def continue_token(self) -> str | None:
        return self._first.continue_token

    def pages(self) -> Iterator[RawPage[T]]:
        page = self._first
        while True:
            yield page
            if page.continue_token is None:
                return
            page = self._fetch_next(page.continue_token)

    def __iter__(self) -> Iterator[T]:
        for page in self.pages():
            yield from page.items


class AsyncPage(Generic[T]):
    """Auto-paginating async iterable returned by async list calls."""

    def __init__(
        self,
        *,
        first: RawPage[T],
        fetch_next: AsyncPageFetcher,
    ) -> None:
        self._first = first
        self._fetch_next = fetch_next

    @property
    def has_more(self) -> bool:
        return self._first.continue_token is not None

    @property
    def items(self) -> list[T]:
        return list(self._first.items)

    @property
    def continue_token(self) -> str | None:
        return self._first.continue_token

    async def pages(self) -> AsyncIterator[RawPage[T]]:
        page = self._first
        while True:
            yield page
            if page.continue_token is None:
                return
            page = await self._fetch_next(page.continue_token)

    async def __aiter__(self) -> AsyncIterator[T]:
        async for page in self.pages():
            for item in page.items:
                yield item
