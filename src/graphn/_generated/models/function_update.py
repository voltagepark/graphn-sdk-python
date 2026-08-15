from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_update_files import FunctionUpdateFiles
    from ..models.function_update_parameters_schema import (
        FunctionUpdateParametersSchema,
    )


T = TypeVar("T", bound="FunctionUpdate")


@_attrs_define
class FunctionUpdate:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        files (FunctionUpdateFiles | Unset):
        parameters_schema (FunctionUpdateParametersSchema | Unset):
        workflow_id (str | Unset):
        memory_mb (int | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    files: FunctionUpdateFiles | Unset = UNSET
    parameters_schema: FunctionUpdateParametersSchema | Unset = UNSET
    workflow_id: str | Unset = UNSET
    memory_mb: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        parameters_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters_schema, Unset):
            parameters_schema = self.parameters_schema.to_dict()

        workflow_id = self.workflow_id

        memory_mb = self.memory_mb

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if files is not UNSET:
            field_dict["files"] = files
        if parameters_schema is not UNSET:
            field_dict["parameters_schema"] = parameters_schema
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.function_update_files import FunctionUpdateFiles
        from ..models.function_update_parameters_schema import (
            FunctionUpdateParametersSchema,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _files = d.pop("files", UNSET)
        files: FunctionUpdateFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = FunctionUpdateFiles.from_dict(_files)

        _parameters_schema = d.pop("parameters_schema", UNSET)
        parameters_schema: FunctionUpdateParametersSchema | Unset
        if isinstance(_parameters_schema, Unset):
            parameters_schema = UNSET
        else:
            parameters_schema = FunctionUpdateParametersSchema.from_dict(
                _parameters_schema
            )

        workflow_id = d.pop("workflow_id", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        function_update = cls(
            name=name,
            description=description,
            files=files,
            parameters_schema=parameters_schema,
            workflow_id=workflow_id,
            memory_mb=memory_mb,
        )

        return function_update
