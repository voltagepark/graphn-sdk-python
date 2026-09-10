from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_dry_run_request_files import FunctionDryRunRequestFiles
    from ..models.function_dry_run_request_input import FunctionDryRunRequestInput


T = TypeVar("T", bound="FunctionDryRunRequest")


@_attrs_define
class FunctionDryRunRequest:
    """
    Attributes:
        files (FunctionDryRunRequestFiles | Unset):
        input_ (FunctionDryRunRequestInput | Unset):
        timeout (int | Unset):
        async_execution (bool | Unset):
        memory_mb (int | Unset):
    """

    files: FunctionDryRunRequestFiles | Unset = UNSET
    input_: FunctionDryRunRequestInput | Unset = UNSET
    timeout: int | Unset = UNSET
    async_execution: bool | Unset = UNSET
    memory_mb: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        timeout = self.timeout

        async_execution = self.async_execution

        memory_mb = self.memory_mb

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if input_ is not UNSET:
            field_dict["input"] = input_
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if async_execution is not UNSET:
            field_dict["async_execution"] = async_execution
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.function_dry_run_request_files import (
            FunctionDryRunRequestFiles,
        )
        from ..models.function_dry_run_request_input import (
            FunctionDryRunRequestInput,
        )

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: FunctionDryRunRequestFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = FunctionDryRunRequestFiles.from_dict(_files)

        _input_ = d.pop("input", UNSET)
        input_: FunctionDryRunRequestInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = FunctionDryRunRequestInput.from_dict(_input_)

        timeout = d.pop("timeout", UNSET)

        async_execution = d.pop("async_execution", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        function_dry_run_request = cls(
            files=files,
            input_=input_,
            timeout=timeout,
            async_execution=async_execution,
            memory_mb=memory_mb,
        )

        return function_dry_run_request
