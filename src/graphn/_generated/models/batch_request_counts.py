from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="BatchRequestCounts")


@_attrs_define
class BatchRequestCounts:
    """
    Attributes:
        total (int):
        completed (int):
        failed (int):
        canceled (int):
    """

    total: int
    completed: int
    failed: int
    canceled: int

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        completed = self.completed

        failed = self.failed

        canceled = self.canceled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "completed": completed,
                "failed": failed,
                "canceled": canceled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total")

        completed = d.pop("completed")

        failed = d.pop("failed")

        canceled = d.pop("canceled")

        batch_request_counts = cls(
            total=total,
            completed=completed,
            failed=failed,
            canceled=canceled,
        )

        return batch_request_counts
