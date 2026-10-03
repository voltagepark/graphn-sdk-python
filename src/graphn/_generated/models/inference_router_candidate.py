from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="InferenceRouterCandidate")


@_attrs_define
class InferenceRouterCandidate:
    """
    Attributes:
        target (str): Unprefixed built-in alias or `custom:cm_...` logical reference.
        lanes (list[str]):
        weight (int):
        order (int):
    """

    target: str
    lanes: list[str]
    weight: int
    order: int

    def to_dict(self) -> dict[str, Any]:
        target = self.target

        lanes = self.lanes

        weight = self.weight

        order = self.order

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target": target,
                "lanes": lanes,
                "weight": weight,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        target = d.pop("target")

        lanes = cast(list[str], d.pop("lanes"))

        weight = d.pop("weight")

        order = d.pop("order")

        inference_router_candidate = cls(
            target=target,
            lanes=lanes,
            weight=weight,
            order=order,
        )

        return inference_router_candidate
