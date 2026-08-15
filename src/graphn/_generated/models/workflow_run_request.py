from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_run_request_input import WorkflowRunRequestInput


T = TypeVar("T", bound="WorkflowRunRequest")


@_attrs_define
class WorkflowRunRequest:
    """
    Attributes:
        input_ (WorkflowRunRequestInput | Unset):
        async_execution (bool | Unset):
    """

    input_: WorkflowRunRequestInput | Unset = UNSET
    async_execution: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        async_execution = self.async_execution

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if async_execution is not UNSET:
            field_dict["async_execution"] = async_execution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_run_request_input import WorkflowRunRequestInput

        d = dict(src_dict)
        _input_ = d.pop("input", UNSET)
        input_: WorkflowRunRequestInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = WorkflowRunRequestInput.from_dict(_input_)

        async_execution = d.pop("async_execution", UNSET)

        workflow_run_request = cls(
            input_=input_,
            async_execution=async_execution,
        )

        return workflow_run_request
