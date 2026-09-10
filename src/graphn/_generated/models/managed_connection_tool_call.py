from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.managed_connection_tool_call_arguments import (
        ManagedConnectionToolCallArguments,
    )


T = TypeVar("T", bound="ManagedConnectionToolCall")


@_attrs_define
class ManagedConnectionToolCall:
    """
    Attributes:
        resource_id (str):
        version_id (str):
        arguments (ManagedConnectionToolCallArguments):
    """

    resource_id: str
    version_id: str
    arguments: ManagedConnectionToolCallArguments

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        version_id = self.version_id

        arguments = self.arguments.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resource_id": resource_id,
                "version_id": version_id,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.managed_connection_tool_call_arguments import (
            ManagedConnectionToolCallArguments,
        )

        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        version_id = d.pop("version_id")

        arguments = ManagedConnectionToolCallArguments.from_dict(d.pop("arguments"))

        managed_connection_tool_call = cls(
            resource_id=resource_id,
            version_id=version_id,
            arguments=arguments,
        )

        return managed_connection_tool_call
