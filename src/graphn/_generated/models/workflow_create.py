from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_create_input_schema import WorkflowCreateInputSchema
    from ..models.workflow_create_layout import WorkflowCreateLayout
    from ..models.workflow_create_output_schema import WorkflowCreateOutputSchema
    from ..models.workflow_create_source import WorkflowCreateSource


T = TypeVar("T", bound="WorkflowCreate")


@_attrs_define
class WorkflowCreate:
    """
    Attributes:
        name (str):
        dsl (str | Unset):
        layout (WorkflowCreateLayout | Unset):
        input_schema (WorkflowCreateInputSchema | Unset):
        output_schema (WorkflowCreateOutputSchema | Unset):
        description (str | Unset):
        source (WorkflowCreateSource | Unset):
        supported_gateways (list[str] | Unset):
    """

    name: str
    dsl: str | Unset = UNSET
    layout: WorkflowCreateLayout | Unset = UNSET
    input_schema: WorkflowCreateInputSchema | Unset = UNSET
    output_schema: WorkflowCreateOutputSchema | Unset = UNSET
    description: str | Unset = UNSET
    source: WorkflowCreateSource | Unset = UNSET
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

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        supported_gateways: list[str] | Unset = UNSET
        if not isinstance(self.supported_gateways, Unset):
            supported_gateways = self.supported_gateways

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
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
        if source is not UNSET:
            field_dict["source"] = source
        if supported_gateways is not UNSET:
            field_dict["supported_gateways"] = supported_gateways

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_create_input_schema import WorkflowCreateInputSchema
        from ..models.workflow_create_layout import WorkflowCreateLayout
        from ..models.workflow_create_output_schema import WorkflowCreateOutputSchema
        from ..models.workflow_create_source import WorkflowCreateSource

        d = dict(src_dict)
        name = d.pop("name")

        dsl = d.pop("dsl", UNSET)

        _layout = d.pop("layout", UNSET)
        layout: WorkflowCreateLayout | Unset
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = WorkflowCreateLayout.from_dict(_layout)

        _input_schema = d.pop("input_schema", UNSET)
        input_schema: WorkflowCreateInputSchema | Unset
        if isinstance(_input_schema, Unset):
            input_schema = UNSET
        else:
            input_schema = WorkflowCreateInputSchema.from_dict(_input_schema)

        _output_schema = d.pop("output_schema", UNSET)
        output_schema: WorkflowCreateOutputSchema | Unset
        if isinstance(_output_schema, Unset):
            output_schema = UNSET
        else:
            output_schema = WorkflowCreateOutputSchema.from_dict(_output_schema)

        description = d.pop("description", UNSET)

        _source = d.pop("source", UNSET)
        source: WorkflowCreateSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = WorkflowCreateSource.from_dict(_source)

        supported_gateways = cast(list[str], d.pop("supported_gateways", UNSET))

        workflow_create = cls(
            name=name,
            dsl=dsl,
            layout=layout,
            input_schema=input_schema,
            output_schema=output_schema,
            description=description,
            source=source,
            supported_gateways=supported_gateways,
        )

        return workflow_create
