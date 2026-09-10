from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.blueprint_deploy_resource_i_ds import BlueprintDeployResourceIDs


T = TypeVar("T", bound="BlueprintDeployResponse")


@_attrs_define
class BlueprintDeployResponse:
    """
    Attributes:
        workflow_id (str):
        name (str):
        resource_ids (BlueprintDeployResourceIDs):
    """

    workflow_id: str
    name: str
    resource_ids: BlueprintDeployResourceIDs

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        name = self.name

        resource_ids = self.resource_ids.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workflow_id": workflow_id,
                "name": name,
                "resource_ids": resource_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.blueprint_deploy_resource_i_ds import (
            BlueprintDeployResourceIDs,
        )

        d = dict(src_dict)
        workflow_id = d.pop("workflow_id")

        name = d.pop("name")

        resource_ids = BlueprintDeployResourceIDs.from_dict(d.pop("resource_ids"))

        blueprint_deploy_response = cls(
            workflow_id=workflow_id,
            name=name,
            resource_ids=resource_ids,
        )

        return blueprint_deploy_response
