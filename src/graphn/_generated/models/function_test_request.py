from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_test_request_input import FunctionTestRequestInput


T = TypeVar("T", bound="FunctionTestRequest")


@_attrs_define
class FunctionTestRequest:
    """
    Attributes:
        input_ (FunctionTestRequestInput | Unset):
    """

    input_: FunctionTestRequestInput | Unset = UNSET

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
        from ..models.function_test_request_input import (
            FunctionTestRequestInput,
        )

        d = dict(src_dict)
        _input_ = d.pop("input", UNSET)
        input_: FunctionTestRequestInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = FunctionTestRequestInput.from_dict(_input_)

        function_test_request = cls(
            input_=input_,
        )

        return function_test_request
