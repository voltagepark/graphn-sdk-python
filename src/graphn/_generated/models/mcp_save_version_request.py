from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_save_version_request_files import McpSaveVersionRequestFiles


T = TypeVar("T", bound="McpSaveVersionRequest")


@_attrs_define
class McpSaveVersionRequest:
    """
    Attributes:
        files (McpSaveVersionRequestFiles | Unset):
        message (str | Unset):
    """

    files: McpSaveVersionRequestFiles | Unset = UNSET
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_save_version_request_files import McpSaveVersionRequestFiles

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: McpSaveVersionRequestFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = McpSaveVersionRequestFiles.from_dict(_files)

        message = d.pop("message", UNSET)

        mcp_save_version_request = cls(
            files=files,
            message=message,
        )

        return mcp_save_version_request
