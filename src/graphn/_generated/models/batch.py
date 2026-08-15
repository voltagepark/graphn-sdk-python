from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_request_counts import BatchRequestCounts


T = TypeVar("T", bound="Batch")


@_attrs_define
class Batch:
    """
    Attributes:
        id (str):
        status (str):
        created_at (str):
        request_counts (BatchRequestCounts):
        completed_at (str | Unset):
    """

    id: str
    status: str
    created_at: str
    request_counts: BatchRequestCounts
    completed_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        created_at = self.created_at

        request_counts = self.request_counts.to_dict()

        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "created_at": created_at,
                "request_counts": request_counts,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_request_counts import BatchRequestCounts

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        created_at = d.pop("created_at")

        request_counts = BatchRequestCounts.from_dict(d.pop("request_counts"))

        completed_at = d.pop("completed_at", UNSET)

        batch = cls(
            id=id,
            status=status,
            created_at=created_at,
            request_counts=request_counts,
            completed_at=completed_at,
        )

        batch.additional_properties = d
        return batch

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
