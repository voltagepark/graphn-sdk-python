from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_item_error import BatchItemError
    from ..models.batch_item_output import BatchItemOutput


T = TypeVar("T", bound="BatchItem")


@_attrs_define
class BatchItem:
    """
    Attributes:
        id (str):
        status (str):
        created_at (str):
        custom_id (str | Unset):
        output (BatchItemOutput | Unset):
        error (BatchItemError | Unset):
        completed_at (str | Unset):
    """

    id: str
    status: str
    created_at: str
    custom_id: str | Unset = UNSET
    output: BatchItemOutput | Unset = UNSET
    error: BatchItemError | Unset = UNSET
    completed_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        created_at = self.created_at

        custom_id = self.custom_id

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "created_at": created_at,
            }
        )
        if custom_id is not UNSET:
            field_dict["custom_id"] = custom_id
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_item_error import BatchItemError
        from ..models.batch_item_output import BatchItemOutput

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        created_at = d.pop("created_at")

        custom_id = d.pop("custom_id", UNSET)

        _output = d.pop("output", UNSET)
        output: BatchItemOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = BatchItemOutput.from_dict(_output)

        _error = d.pop("error", UNSET)
        error: BatchItemError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = BatchItemError.from_dict(_error)

        completed_at = d.pop("completed_at", UNSET)

        batch_item = cls(
            id=id,
            status=status,
            created_at=created_at,
            custom_id=custom_id,
            output=output,
            error=error,
            completed_at=completed_at,
        )

        batch_item.additional_properties = d
        return batch_item

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
