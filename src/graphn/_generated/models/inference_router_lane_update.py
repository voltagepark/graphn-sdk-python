from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.inference_router_lane_update_match import InferenceRouterLaneUpdateMatch
from ..types import UNSET, Unset

T = TypeVar("T", bound="InferenceRouterLaneUpdate")


@_attrs_define
class InferenceRouterLaneUpdate:
    """
    Attributes:
        expected_version (int):
        display_name (str | Unset):
        description (str | Unset):
        match (InferenceRouterLaneUpdateMatch | Unset):
        phrases (list[str] | Unset):
    """

    expected_version: int
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    match: InferenceRouterLaneUpdateMatch | Unset = UNSET
    phrases: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expected_version = self.expected_version

        display_name = self.display_name

        description = self.description

        match: str | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.value

        phrases: list[str] | Unset = UNSET
        if not isinstance(self.phrases, Unset):
            phrases = self.phrases

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expected_version": expected_version,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if match is not UNSET:
            field_dict["match"] = match
        if phrases is not UNSET:
            field_dict["phrases"] = phrases

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        expected_version = d.pop("expected_version")

        display_name = d.pop("display_name", UNSET)

        description = d.pop("description", UNSET)

        _match = d.pop("match", UNSET)
        match: InferenceRouterLaneUpdateMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = InferenceRouterLaneUpdateMatch(_match)

        phrases = cast(list[str], d.pop("phrases", UNSET))

        inference_router_lane_update = cls(
            expected_version=expected_version,
            display_name=display_name,
            description=description,
            match=match,
            phrases=phrases,
        )

        return inference_router_lane_update
