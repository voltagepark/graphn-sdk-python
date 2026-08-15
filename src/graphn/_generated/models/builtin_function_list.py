from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.builtin_function_list_functions import BuiltinFunctionListFunctions


T = TypeVar("T", bound="BuiltinFunctionList")


@_attrs_define
class BuiltinFunctionList:
    """
    Attributes:
        functions (BuiltinFunctionListFunctions):
    """

    functions: BuiltinFunctionListFunctions

    def to_dict(self) -> dict[str, Any]:
        functions = self.functions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "functions": functions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.builtin_function_list_functions import (
            BuiltinFunctionListFunctions,
        )

        d = dict(src_dict)
        functions = BuiltinFunctionListFunctions.from_dict(d.pop("functions"))

        builtin_function_list = cls(
            functions=functions,
        )

        return builtin_function_list
