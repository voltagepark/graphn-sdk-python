from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_test_request_input import ToolTestRequestInput


T = TypeVar("T", bound="ToolTestRequest")


@_attrs_define
class ToolTestRequest:
    """
    Attributes:
        input_ (ToolTestRequestInput | Unset):
    """

    input_: ToolTestRequestInput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tool_test_request_input import ToolTestRequestInput

        d = dict(src_dict)
        _input_ = d.pop("input", UNSET)
        input_: ToolTestRequestInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = ToolTestRequestInput.from_dict(_input_)

        tool_test_request = cls(
            input_=input_,
        )

        return tool_test_request
