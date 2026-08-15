from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctionTestResponse")


@_attrs_define
class FunctionTestResponse:
    """
    Attributes:
        success (bool):
        output (Any | Unset):
        error (str | Unset):
        stdout (str | Unset):
        stderr (str | Unset):
        duration_ms (int | Unset):
        cold_start (bool | Unset):
        boot_ms (int | Unset):
        execution_id (str | Unset):
    """

    success: bool
    output: Any | Unset = UNSET
    error: str | Unset = UNSET
    stdout: str | Unset = UNSET
    stderr: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    cold_start: bool | Unset = UNSET
    boot_ms: int | Unset = UNSET
    execution_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        output = self.output

        error = self.error

        stdout = self.stdout

        stderr = self.stderr

        duration_ms = self.duration_ms

        cold_start = self.cold_start

        boot_ms = self.boot_ms

        execution_id = self.execution_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if cold_start is not UNSET:
            field_dict["cold_start"] = cold_start
        if boot_ms is not UNSET:
            field_dict["boot_ms"] = boot_ms
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success = d.pop("success")

        output = d.pop("output", UNSET)

        error = d.pop("error", UNSET)

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        cold_start = d.pop("cold_start", UNSET)

        boot_ms = d.pop("boot_ms", UNSET)

        execution_id = d.pop("execution_id", UNSET)

        function_test_response = cls(
            success=success,
            output=output,
            error=error,
            stdout=stdout,
            stderr=stderr,
            duration_ms=duration_ms,
            cold_start=cold_start,
            boot_ms=boot_ms,
            execution_id=execution_id,
        )

        function_test_response.additional_properties = d
        return function_test_response

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
