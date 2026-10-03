from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishedRouterDecision")


@_attrs_define
class PublishedRouterDecision:
    """
    Attributes:
        name (str):
        lane (str):
        candidate_refs (list[str]):
        priority (int):
        constraints (list[str] | Unset):
    """

    name: str
    lane: str
    candidate_refs: list[str]
    priority: int
    constraints: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lane = self.lane

        candidate_refs = self.candidate_refs

        priority = self.priority

        constraints: list[str] | Unset = UNSET
        if not isinstance(self.constraints, Unset):
            constraints = self.constraints

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "lane": lane,
                "candidate_refs": candidate_refs,
                "priority": priority,
            }
        )
        if constraints is not UNSET:
            field_dict["constraints"] = constraints

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        lane = d.pop("lane")

        candidate_refs = cast(list[str], d.pop("candidate_refs"))

        priority = d.pop("priority")

        constraints = cast(list[str], d.pop("constraints", UNSET))

        published_router_decision = cls(
            name=name,
            lane=lane,
            candidate_refs=candidate_refs,
            priority=priority,
            constraints=constraints,
        )

        published_router_decision.additional_properties = d
        return published_router_decision

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
