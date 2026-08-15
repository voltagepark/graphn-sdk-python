from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceUsage")


@_attrs_define
class WorkspaceUsage:
    """
    Attributes:
        total (int | Unset):
        pending (int | Unset):
        running (int | Unset):
        completed (int | Unset):
        failed (int | Unset):
        cancelled (int | Unset):
    """

    total: int | Unset = UNSET
    pending: int | Unset = UNSET
    running: int | Unset = UNSET
    completed: int | Unset = UNSET
    failed: int | Unset = UNSET
    cancelled: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        running = self.running

        completed = self.completed

        failed = self.failed

        cancelled = self.cancelled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if pending is not UNSET:
            field_dict["pending"] = pending
        if running is not UNSET:
            field_dict["running"] = running
        if completed is not UNSET:
            field_dict["completed"] = completed
        if failed is not UNSET:
            field_dict["failed"] = failed
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        pending = d.pop("pending", UNSET)

        running = d.pop("running", UNSET)

        completed = d.pop("completed", UNSET)

        failed = d.pop("failed", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        workspace_usage = cls(
            total=total,
            pending=pending,
            running=running,
            completed=completed,
            failed=failed,
            cancelled=cancelled,
        )

        workspace_usage.additional_properties = d
        return workspace_usage

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
