from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="BlueprintDeployResponse")


@_attrs_define
class BlueprintDeployResponse:
    """
    Attributes:
        workflow_id (str):
        name (str):
    """

    workflow_id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workflow_id": workflow_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workflow_id = d.pop("workflow_id")

        name = d.pop("name")

        blueprint_deploy_response = cls(
            workflow_id=workflow_id,
            name=name,
        )

        return blueprint_deploy_response
