"""Shared request-body helpers for resource modules."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def compact(data: Mapping[str, Any]) -> dict[str, Any]:
    """Drop ``None`` values so optional OpenAPI fields stay omitted."""

    return {key: value for key, value in data.items() if value is not None}


def page_params(
    limit: int | None = None,
    continue_token: str | None = None,
    **extra: Any,
) -> dict[str, Any]:
    return compact({"limit": limit, "continue_token": continue_token, **extra})


def merge_extra(body: dict[str, Any], extra: Mapping[str, Any] | None) -> dict[str, Any]:
    if extra:
        body.update(dict(extra))
    return body
