"""Direct tests for the pagination helpers."""

from __future__ import annotations

import pytest

from graphn._pagination import AsyncPage, RawPage, SyncPage


def test_raw_page_accepts_count_field() -> None:
    page = RawPage.from_response(
        {"items": [{"a": 1}], "count": 1, "continue_token": "x"}, lambda x: x
    )
    assert page.count == 1
    assert page.continue_token == "x"


def test_raw_page_accepts_total_field() -> None:
    page = RawPage.from_response({"items": [{"a": 1}, {"a": 2}], "total": 2}, lambda x: x)
    assert page.count == 2
    assert page.continue_token is None


def test_sync_page_iterates_across_pages() -> None:
    pages = [
        RawPage(items=["a", "b"], count=2, continue_token="t1"),
        RawPage(items=["c"], count=1, continue_token="t2"),
        RawPage(items=["d"], count=1, continue_token=None),
    ]
    seen_tokens: list[str | None] = []

    def fetch(token: str | None) -> RawPage[str]:
        seen_tokens.append(token)
        return pages[len(seen_tokens)]

    page = SyncPage(first=pages[0], fetch_next=fetch)
    assert list(page) == ["a", "b", "c", "d"]
    assert seen_tokens == ["t1", "t2"]


@pytest.mark.asyncio
async def test_async_page_iterates_across_pages() -> None:
    pages = [
        RawPage(items=["a"], count=1, continue_token="t1"),
        RawPage(items=["b", "c"], count=2, continue_token=None),
    ]
    seen: list[str | None] = []

    async def fetch(token: str | None) -> RawPage[str]:
        seen.append(token)
        return pages[len(seen)]

    page = AsyncPage(first=pages[0], fetch_next=fetch)
    out: list[str] = []
    async for item in page:
        out.append(item)
    assert out == ["a", "b", "c"]
    assert seen == ["t1"]
