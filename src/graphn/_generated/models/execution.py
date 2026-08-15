from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Execution")


@_attrs_define
class Execution:
    """
    Attributes:
        id (str | Unset):
        execution_id (str | Unset):
        status (str | Unset):
        output (Any | Unset):
        error (Any | Unset):
        created_at (str | Unset):
        completed_at (str | Unset):
    """

    id: str | Unset = UNSET
    execution_id: str | Unset = UNSET
    status: str | Unset = UNSET
    output: Any | Unset = UNSET
    error: Any | Unset = UNSET
    created_at: str | Unset = UNSET
    completed_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        execution_id = self.execution_id

        status = self.status

        output = self.output

        error = self.error

        created_at = self.created_at

        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if status is not UNSET:
            field_dict["status"] = status
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        execution_id = d.pop("execution_id", UNSET)

        status = d.pop("status", UNSET)

        output = d.pop("output", UNSET)

        error = d.pop("error", UNSET)

        created_at = d.pop("created_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        execution = cls(
            id=id,
            execution_id=execution_id,
            status=status,
            output=output,
            error=error,
            created_at=created_at,
            completed_at=completed_at,
        )

        execution.additional_properties = d
        return execution

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
