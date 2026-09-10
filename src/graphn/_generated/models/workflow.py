from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_version_ref import ResourceVersionRef
    from ..models.workflow_input_schema import WorkflowInputSchema
    from ..models.workflow_layout import WorkflowLayout
    from ..models.workflow_output_schema import WorkflowOutputSchema
    from ..models.workflow_source import WorkflowSource


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """
    Attributes:
        id (str):
        workspace_id (str):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        owner_id (str | Unset):
        dsl (str | Unset):
        layout (WorkflowLayout | Unset):
        input_schema (WorkflowInputSchema | Unset):
        output_schema (WorkflowOutputSchema | Unset):
        description (str | Unset):
        source (WorkflowSource | Unset):
        supported_gateways (list[str] | Unset):
        versions (list[ResourceVersionRef] | Unset):
        published_version_id (str | Unset):
        has_unpublished_changes (bool | Unset):
        status (str | Unset):
    """

    id: str
    workspace_id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    owner_id: str | Unset = UNSET
    dsl: str | Unset = UNSET
    layout: WorkflowLayout | Unset = UNSET
    input_schema: WorkflowInputSchema | Unset = UNSET
    output_schema: WorkflowOutputSchema | Unset = UNSET
    description: str | Unset = UNSET
    source: WorkflowSource | Unset = UNSET
    supported_gateways: list[str] | Unset = UNSET
    versions: list[ResourceVersionRef] | Unset = UNSET
    published_version_id: str | Unset = UNSET
    has_unpublished_changes: bool | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        owner_id = self.owner_id

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

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        published_version_id = self.published_version_id

        has_unpublished_changes = self.has_unpublished_changes

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
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
        if versions is not UNSET:
            field_dict["versions"] = versions
        if published_version_id is not UNSET:
            field_dict["published_version_id"] = published_version_id
        if has_unpublished_changes is not UNSET:
            field_dict["has_unpublished_changes"] = has_unpublished_changes
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resource_version_ref import ResourceVersionRef
        from ..models.workflow_input_schema import WorkflowInputSchema
        from ..models.workflow_layout import WorkflowLayout
        from ..models.workflow_output_schema import (
            WorkflowOutputSchema,
        )
        from ..models.workflow_source import WorkflowSource

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        owner_id = d.pop("owner_id", UNSET)

        dsl = d.pop("dsl", UNSET)

        _layout = d.pop("layout", UNSET)
        layout: WorkflowLayout | Unset
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = WorkflowLayout.from_dict(_layout)

        _input_schema = d.pop("input_schema", UNSET)
        input_schema: WorkflowInputSchema | Unset
        if isinstance(_input_schema, Unset):
            input_schema = UNSET
        else:
            input_schema = WorkflowInputSchema.from_dict(_input_schema)

        _output_schema = d.pop("output_schema", UNSET)
        output_schema: WorkflowOutputSchema | Unset
        if isinstance(_output_schema, Unset):
            output_schema = UNSET
        else:
            output_schema = WorkflowOutputSchema.from_dict(_output_schema)

        description = d.pop("description", UNSET)

        _source = d.pop("source", UNSET)
        source: WorkflowSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = WorkflowSource.from_dict(_source)

        supported_gateways = cast(list[str], d.pop("supported_gateways", UNSET))

        _versions = d.pop("versions", UNSET)
        versions: list[ResourceVersionRef] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = ResourceVersionRef.from_dict(versions_item_data)

                versions.append(versions_item)

        published_version_id = d.pop("published_version_id", UNSET)

        has_unpublished_changes = d.pop("has_unpublished_changes", UNSET)

        status = d.pop("status", UNSET)

        workflow = cls(
            id=id,
            workspace_id=workspace_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            owner_id=owner_id,
            dsl=dsl,
            layout=layout,
            input_schema=input_schema,
            output_schema=output_schema,
            description=description,
            source=source,
            supported_gateways=supported_gateways,
            versions=versions,
            published_version_id=published_version_id,
            has_unpublished_changes=has_unpublished_changes,
            status=status,
        )

        workflow.additional_properties = d
        return workflow

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
