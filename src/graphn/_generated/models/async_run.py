from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_run_error import AsyncRunError
    from ..models.async_run_metadata import AsyncRunMetadata
    from ..models.async_run_output import AsyncRunOutput
    from ..models.async_run_result_error import AsyncRunResultError
    from ..models.async_run_usage import AsyncRunUsage


T = TypeVar("T", bound="AsyncRun")


@_attrs_define
class AsyncRun:
    """
    Attributes:
        id (str):
        status (str):
        created_at (str):
        completed_at (str | Unset):
        output (AsyncRunOutput | Unset):
        usage (AsyncRunUsage | Unset):
        error (AsyncRunError | Unset):
        result_error (AsyncRunResultError | Unset):
        metadata (AsyncRunMetadata | Unset):
    """

    id: str
    status: str
    created_at: str
    completed_at: str | Unset = UNSET
    output: AsyncRunOutput | Unset = UNSET
    usage: AsyncRunUsage | Unset = UNSET
    error: AsyncRunError | Unset = UNSET
    result_error: AsyncRunResultError | Unset = UNSET
    metadata: AsyncRunMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        created_at = self.created_at

        completed_at = self.completed_at

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        result_error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result_error, Unset):
            result_error = self.result_error.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "created_at": created_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if output is not UNSET:
            field_dict["output"] = output
        if usage is not UNSET:
            field_dict["usage"] = usage
        if error is not UNSET:
            field_dict["error"] = error
        if result_error is not UNSET:
            field_dict["result_error"] = result_error
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.async_run_error import AsyncRunError
        from ..models.async_run_metadata import AsyncRunMetadata
        from ..models.async_run_output import AsyncRunOutput
        from ..models.async_run_result_error import AsyncRunResultError
        from ..models.async_run_usage import AsyncRunUsage

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        created_at = d.pop("created_at")

        completed_at = d.pop("completed_at", UNSET)

        _output = d.pop("output", UNSET)
        output: AsyncRunOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = AsyncRunOutput.from_dict(_output)

        _usage = d.pop("usage", UNSET)
        usage: AsyncRunUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = AsyncRunUsage.from_dict(_usage)

        _error = d.pop("error", UNSET)
        error: AsyncRunError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AsyncRunError.from_dict(_error)

        _result_error = d.pop("result_error", UNSET)
        result_error: AsyncRunResultError | Unset
        if isinstance(_result_error, Unset):
            result_error = UNSET
        else:
            result_error = AsyncRunResultError.from_dict(_result_error)

        _metadata = d.pop("metadata", UNSET)
        metadata: AsyncRunMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AsyncRunMetadata.from_dict(_metadata)

        async_run = cls(
            id=id,
            status=status,
            created_at=created_at,
            completed_at=completed_at,
            output=output,
            usage=usage,
            error=error,
            result_error=result_error,
            metadata=metadata,
        )

        async_run.additional_properties = d
        return async_run

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
