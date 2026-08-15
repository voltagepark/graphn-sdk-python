from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_update_input_schema import WorkflowUpdateInputSchema
    from ..models.workflow_update_layout import WorkflowUpdateLayout
    from ..models.workflow_update_output_schema import WorkflowUpdateOutputSchema


T = TypeVar("T", bound="WorkflowUpdate")


@_attrs_define
class WorkflowUpdate:
    """
    Attributes:
        name (str | Unset):
        dsl (str | Unset):
        layout (WorkflowUpdateLayout | Unset):
        input_schema (WorkflowUpdateInputSchema | Unset):
        output_schema (WorkflowUpdateOutputSchema | Unset):
        description (str | Unset):
        supported_gateways (list[str] | Unset):
    """

    name: str | Unset = UNSET
    dsl: str | Unset = UNSET
    layout: WorkflowUpdateLayout | Unset = UNSET
    input_schema: WorkflowUpdateInputSchema | Unset = UNSET
    output_schema: WorkflowUpdateOutputSchema | Unset = UNSET
    description: str | Unset = UNSET
    supported_gateways: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        dsl = self.dsl

        layout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.to_dict()

        input_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_schema, Unset):
            input_schema = self.input_schema.to_dict()

        output_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_schema, Unset):
            output_schema = self.output_schema.to_dict()

        description = self.description

        supported_gateways: list[str] | Unset = UNSET
        if not isinstance(self.supported_gateways, Unset):
            supported_gateways = self.supported_gateways

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if dsl is not UNSET:
            field_dict["dsl"] = dsl
        if layout is not UNSET:
            field_dict["layout"] = layout
        if input_schema is not UNSET:
            field_dict["input_schema"] = input_schema
        if output_schema is not UNSET:
            field_dict["output_schema"] = output_schema
        if description is not UNSET:
            field_dict["description"] = description
        if supported_gateways is not UNSET:
            field_dict["supported_gateways"] = supported_gateways

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_update_input_schema import WorkflowUpdateInputSchema
        from ..models.workflow_update_layout import WorkflowUpdateLayout
        from ..models.workflow_update_output_schema import WorkflowUpdateOutputSchema

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        dsl = d.pop("dsl", UNSET)

        _layout = d.pop("layout", UNSET)
        layout: WorkflowUpdateLayout | Unset
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = WorkflowUpdateLayout.from_dict(_layout)

        _input_schema = d.pop("input_schema", UNSET)
        input_schema: WorkflowUpdateInputSchema | Unset
        if isinstance(_input_schema, Unset):
            input_schema = UNSET
        else:
            input_schema = WorkflowUpdateInputSchema.from_dict(_input_schema)

        _output_schema = d.pop("output_schema", UNSET)
        output_schema: WorkflowUpdateOutputSchema | Unset
        if isinstance(_output_schema, Unset):
            output_schema = UNSET
        else:
            output_schema = WorkflowUpdateOutputSchema.from_dict(_output_schema)

        description = d.pop("description", UNSET)

        supported_gateways = cast(list[str], d.pop("supported_gateways", UNSET))

        workflow_update = cls(
            name=name,
            dsl=dsl,
            layout=layout,
            input_schema=input_schema,
            output_schema=output_schema,
            description=description,
            supported_gateways=supported_gateways,
        )

        return workflow_update
