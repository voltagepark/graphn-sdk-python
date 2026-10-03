from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.inference_router_lane_create_match import InferenceRouterLaneCreateMatch
from ..types import UNSET, Unset

T = TypeVar("T", bound="InferenceRouterLaneCreate")


@_attrs_define
class InferenceRouterLaneCreate:
    """
    Attributes:
        display_name (str):
        phrases (list[str]):
        description (str | Unset):
        match (InferenceRouterLaneCreateMatch | Unset): `any` matches when one phrase appears; `all` requires every
            phrase. Default: InferenceRouterLaneCreateMatch.ANY.
    """

    display_name: str
    phrases: list[str]
    description: str | Unset = UNSET
    match: InferenceRouterLaneCreateMatch | Unset = InferenceRouterLaneCreateMatch.ANY

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        phrases = self.phrases

        description = self.description

        match: str | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "display_name": display_name,
                "phrases": phrases,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if match is not UNSET:
            field_dict["match"] = match

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        phrases = cast(list[str], d.pop("phrases"))

        description = d.pop("description", UNSET)

        _match = d.pop("match", UNSET)
        match: InferenceRouterLaneCreateMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = InferenceRouterLaneCreateMatch(_match)

        inference_router_lane_create = cls(
            display_name=display_name,
            phrases=phrases,
            description=description,
            match=match,
        )

        return inference_router_lane_create
