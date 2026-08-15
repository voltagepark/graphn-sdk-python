from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_spec import AgentSpec


T = TypeVar("T", bound="AgentCreate")


@_attrs_define
class AgentCreate:
    """
    Attributes:
        name (str):
        spec (AgentSpec | Unset):
        workflow_id (str | Unset):
    """

    name: str
    spec: AgentSpec | Unset = UNSET
    workflow_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.agent_spec import AgentSpec

        d = dict(src_dict)
        name = d.pop("name")

        _spec = d.pop("spec", UNSET)
        spec: AgentSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = AgentSpec.from_dict(_spec)

        workflow_id = d.pop("workflow_id", UNSET)

        agent_create = cls(
            name=name,
            spec=spec,
            workflow_id=workflow_id,
        )

        return agent_create
