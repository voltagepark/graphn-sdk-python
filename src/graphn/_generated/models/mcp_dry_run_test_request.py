from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_dry_run_test_request_input import McpDryRunTestRequestInput
    from ..models.mcp_source_files import McpSourceFiles


T = TypeVar("T", bound="McpDryRunTestRequest")


@_attrs_define
class McpDryRunTestRequest:
    """
    Attributes:
        files (McpSourceFiles | Unset): Source content is limited to 1 MiB in aggregate; each file name is limited to
            512 UTF-8 bytes.
        tool_name (str | Unset):
        input_ (McpDryRunTestRequestInput | Unset):
    """

    files: McpSourceFiles | Unset = UNSET
    tool_name: str | Unset = UNSET
    input_: McpDryRunTestRequestInput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        tool_name = self.tool_name

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_dry_run_test_request_input import McpDryRunTestRequestInput
        from ..models.mcp_source_files import McpSourceFiles

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: McpSourceFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = McpSourceFiles.from_dict(_files)

        tool_name = d.pop("tool_name", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: McpDryRunTestRequestInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = McpDryRunTestRequestInput.from_dict(_input_)

        mcp_dry_run_test_request = cls(
            files=files,
            tool_name=tool_name,
            input_=input_,
        )

        return mcp_dry_run_test_request
