from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.inference_router_lane_match import InferenceRouterLaneMatch
from ..types import UNSET, Unset

T = TypeVar("T", bound="InferenceRouterLane")


@_attrs_define
class InferenceRouterLane:
    """
    Attributes:
        id (str):
        reference (str): The value to put in a router candidate's `lanes`.
        display_name (str):
        match (InferenceRouterLaneMatch):
        phrases (list[str]):
        version (int):
        used_by (list[str]): IDs of routers whose draft, pending, active, or draining revision references this lane. A
            previous revision keeps draining from its shard for a while after a newer one activates, so a router can stay
            listed (and DELETE can stay 409) after its current revisions have dropped the lane.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (str | Unset):
    """

    id: str
    reference: str
    display_name: str
    match: InferenceRouterLaneMatch
    phrases: list[str]
    version: int
    used_by: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reference = self.reference

        display_name = self.display_name

        match = self.match.value

        phrases = self.phrases

        version = self.version

        used_by = self.used_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "reference": reference,
                "display_name": display_name,
                "match": match,
                "phrases": phrases,
                "version": version,
                "used_by": used_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        reference = d.pop("reference")

        display_name = d.pop("display_name")

        match = InferenceRouterLaneMatch(d.pop("match"))

        phrases = cast(list[str], d.pop("phrases"))

        version = d.pop("version")

        used_by = cast(list[str], d.pop("used_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        inference_router_lane = cls(
            id=id,
            reference=reference,
            display_name=display_name,
            match=match,
            phrases=phrases,
            version=version,
            used_by=used_by,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )

        inference_router_lane.additional_properties = d
        return inference_router_lane

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
