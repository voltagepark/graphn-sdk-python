from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_spec_files import FunctionSpecFiles
    from ..models.function_spec_parameters_schema import FunctionSpecParametersSchema


T = TypeVar("T", bound="FunctionSpec")


@_attrs_define
class FunctionSpec:
    """
    Attributes:
        type_ (str | Unset):
        description (str | Unset):
        files (FunctionSpecFiles | Unset):
        parameters_schema (FunctionSpecParametersSchema | Unset):
        builtin_name (str | Unset):
        memory_mb (int | Unset):
    """

    type_: str | Unset = UNSET
    description: str | Unset = UNSET
    files: FunctionSpecFiles | Unset = UNSET
    parameters_schema: FunctionSpecParametersSchema | Unset = UNSET
    builtin_name: str | Unset = UNSET
    memory_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        description = self.description

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        parameters_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters_schema, Unset):
            parameters_schema = self.parameters_schema.to_dict()

        builtin_name = self.builtin_name

        memory_mb = self.memory_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if files is not UNSET:
            field_dict["files"] = files
        if parameters_schema is not UNSET:
            field_dict["parameters_schema"] = parameters_schema
        if builtin_name is not UNSET:
            field_dict["builtin_name"] = builtin_name
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.function_spec_files import FunctionSpecFiles
        from ..models.function_spec_parameters_schema import (
            FunctionSpecParametersSchema,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        _files = d.pop("files", UNSET)
        files: FunctionSpecFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = FunctionSpecFiles.from_dict(_files)

        _parameters_schema = d.pop("parameters_schema", UNSET)
        parameters_schema: FunctionSpecParametersSchema | Unset
        if isinstance(_parameters_schema, Unset):
            parameters_schema = UNSET
        else:
            parameters_schema = FunctionSpecParametersSchema.from_dict(
                _parameters_schema
            )

        builtin_name = d.pop("builtin_name", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        function_spec = cls(
            type_=type_,
            description=description,
            files=files,
            parameters_schema=parameters_schema,
            builtin_name=builtin_name,
            memory_mb=memory_mb,
        )

        function_spec.additional_properties = d
        return function_spec

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
