from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_discover_tools_request_files import McpDiscoverToolsRequestFiles


T = TypeVar("T", bound="McpDiscoverToolsRequest")


@_attrs_define
class McpDiscoverToolsRequest:
    """
    Attributes:
        files (McpDiscoverToolsRequestFiles | Unset):
    """

    files: McpDiscoverToolsRequestFiles | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_discover_tools_request_files import (
            McpDiscoverToolsRequestFiles,
        )

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: McpDiscoverToolsRequestFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = McpDiscoverToolsRequestFiles.from_dict(_files)

        mcp_discover_tools_request = cls(
            files=files,
        )

        return mcp_discover_tools_request
