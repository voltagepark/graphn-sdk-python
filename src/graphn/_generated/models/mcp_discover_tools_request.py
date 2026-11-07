from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_source_files import McpSourceFiles


T = TypeVar("T", bound="McpDiscoverToolsRequest")


@_attrs_define
class McpDiscoverToolsRequest:
    """
    Attributes:
        files (McpSourceFiles | Unset): Source content is limited to 1 MiB in aggregate; each file name is limited to
            512 UTF-8 bytes.
    """

    files: McpSourceFiles | Unset = UNSET

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
        from ..models.mcp_source_files import McpSourceFiles

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: McpSourceFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = McpSourceFiles.from_dict(_files)

        mcp_discover_tools_request = cls(
            files=files,
        )

        return mcp_discover_tools_request
