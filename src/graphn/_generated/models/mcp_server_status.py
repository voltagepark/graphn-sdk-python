from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="McpServerStatus")


@_attrs_define
class McpServerStatus:
    """
    Attributes:
        server_id (str):
        status (str):
        runtime_status (str | Unset):
    """

    server_id: str
    status: str
    runtime_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_id = self.server_id

        status = self.status

        runtime_status = self.runtime_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_id": server_id,
                "status": status,
            }
        )
        if runtime_status is not UNSET:
            field_dict["runtime_status"] = runtime_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        server_id = d.pop("server_id")

        status = d.pop("status")

        runtime_status = d.pop("runtime_status", UNSET)

        mcp_server_status = cls(
            server_id=server_id,
            status=status,
            runtime_status=runtime_status,
        )

        mcp_server_status.additional_properties = d
        return mcp_server_status

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
