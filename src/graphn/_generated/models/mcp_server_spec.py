from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.mcp_server_spec_type import McpServerSpecType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server_spec_files import McpServerSpecFiles
    from ..models.mcp_server_spec_secrets import McpServerSpecSecrets
    from ..models.mcp_server_spec_tool_capabilities import McpServerSpecToolCapabilities


T = TypeVar("T", bound="McpServerSpec")


@_attrs_define
class McpServerSpec:
    """
    Attributes:
        type_ (McpServerSpecType | Unset):
        files (McpServerSpecFiles | Unset):
        endpoint_url (str | Unset):
        secrets (McpServerSpecSecrets | Unset):
        provider_id (str | Unset):
        connection_id (str | Unset):
        tool_capabilities (McpServerSpecToolCapabilities | Unset):
    """

    type_: McpServerSpecType | Unset = UNSET
    files: McpServerSpecFiles | Unset = UNSET
    endpoint_url: str | Unset = UNSET
    secrets: McpServerSpecSecrets | Unset = UNSET
    provider_id: str | Unset = UNSET
    connection_id: str | Unset = UNSET
    tool_capabilities: McpServerSpecToolCapabilities | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        endpoint_url = self.endpoint_url

        secrets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()

        provider_id = self.provider_id

        connection_id = self.connection_id

        tool_capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_capabilities, Unset):
            tool_capabilities = self.tool_capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if files is not UNSET:
            field_dict["files"] = files
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if tool_capabilities is not UNSET:
            field_dict["tool_capabilities"] = tool_capabilities

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_server_spec_files import McpServerSpecFiles
        from ..models.mcp_server_spec_secrets import (
            McpServerSpecSecrets,
        )
        from ..models.mcp_server_spec_tool_capabilities import (
            McpServerSpecToolCapabilities,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: McpServerSpecType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = McpServerSpecType(_type_)

        _files = d.pop("files", UNSET)
        files: McpServerSpecFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = McpServerSpecFiles.from_dict(_files)

        endpoint_url = d.pop("endpoint_url", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: McpServerSpecSecrets | Unset
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = McpServerSpecSecrets.from_dict(_secrets)

        provider_id = d.pop("provider_id", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        _tool_capabilities = d.pop("tool_capabilities", UNSET)
        tool_capabilities: McpServerSpecToolCapabilities | Unset
        if isinstance(_tool_capabilities, Unset):
            tool_capabilities = UNSET
        else:
            tool_capabilities = McpServerSpecToolCapabilities.from_dict(
                _tool_capabilities
            )

        mcp_server_spec = cls(
            type_=type_,
            files=files,
            endpoint_url=endpoint_url,
            secrets=secrets,
            provider_id=provider_id,
            connection_id=connection_id,
            tool_capabilities=tool_capabilities,
        )

        mcp_server_spec.additional_properties = d
        return mcp_server_spec

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
