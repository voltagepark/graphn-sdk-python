from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.published_router_custom_lane_match import PublishedRouterCustomLaneMatch

T = TypeVar("T", bound="PublishedRouterCustomLane")


@_attrs_define
class PublishedRouterCustomLane:
    """
    Attributes:
        reference (str):
        match (PublishedRouterCustomLaneMatch):
        phrases (list[str]):
    """

    reference: str
    match: PublishedRouterCustomLaneMatch
    phrases: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        match = self.match.value

        phrases = self.phrases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
                "match": match,
                "phrases": phrases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reference = d.pop("reference")

        match = PublishedRouterCustomLaneMatch(d.pop("match"))

        phrases = cast(list[str], d.pop("phrases"))

        published_router_custom_lane = cls(
            reference=reference,
            match=match,
            phrases=phrases,
        )

        published_router_custom_lane.additional_properties = d
        return published_router_custom_lane

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
