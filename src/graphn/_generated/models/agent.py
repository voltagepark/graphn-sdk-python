from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_spec import AgentSpec
    from ..models.resource_version_ref import ResourceVersionRef


T = TypeVar("T", bound="Agent")


@_attrs_define
class Agent:
    """
    Attributes:
        id (str):
        workspace_id (str):
        name (str):
        spec (AgentSpec):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        owner_id (str | Unset):
        workflow_id (str | Unset):
        versions (list[ResourceVersionRef] | Unset):
        published_version_id (str | Unset):
        has_unpublished_changes (bool | Unset):
        content_hash (str | Unset):
        status (str | Unset):
    """

    id: str
    workspace_id: str
    name: str
    spec: AgentSpec
    created_at: datetime.datetime
    updated_at: datetime.datetime
    owner_id: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    versions: list[ResourceVersionRef] | Unset = UNSET
    published_version_id: str | Unset = UNSET
    has_unpublished_changes: bool | Unset = UNSET
    content_hash: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        name = self.name

        spec = self.spec.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        owner_id = self.owner_id

        workflow_id = self.workflow_id

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        published_version_id = self.published_version_id

        has_unpublished_changes = self.has_unpublished_changes

        content_hash = self.content_hash

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "name": name,
                "spec": spec,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
        if versions is not UNSET:
            field_dict["versions"] = versions
        if published_version_id is not UNSET:
            field_dict["published_version_id"] = published_version_id
        if has_unpublished_changes is not UNSET:
            field_dict["has_unpublished_changes"] = has_unpublished_changes
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.agent_spec import AgentSpec
        from ..models.resource_version_ref import ResourceVersionRef

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        name = d.pop("name")

        spec = AgentSpec.from_dict(d.pop("spec"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        owner_id = d.pop("owner_id", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        _versions = d.pop("versions", UNSET)
        versions: list[ResourceVersionRef] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = ResourceVersionRef.from_dict(versions_item_data)

                versions.append(versions_item)

        published_version_id = d.pop("published_version_id", UNSET)

        has_unpublished_changes = d.pop("has_unpublished_changes", UNSET)

        content_hash = d.pop("content_hash", UNSET)

        status = d.pop("status", UNSET)

        agent = cls(
            id=id,
            workspace_id=workspace_id,
            name=name,
            spec=spec,
            created_at=created_at,
            updated_at=updated_at,
            owner_id=owner_id,
            workflow_id=workflow_id,
            versions=versions,
            published_version_id=published_version_id,
            has_unpublished_changes=has_unpublished_changes,
            content_hash=content_hash,
            status=status,
        )

        agent.additional_properties = d
        return agent

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
