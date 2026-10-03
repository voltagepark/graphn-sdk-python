from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PublishedRouterCandidate")


@_attrs_define
class PublishedRouterCandidate:
    """
    Attributes:
        reference (str):
        target (str):
        lanes (list[str]):
        weight (int):
        order (int):
        capabilities (list[str]):
        context_window (int):
        context_length (int):
        quality_score (float):
        prompt_per_1m (float):
        completion_per_1m (float):
    """

    reference: str
    target: str
    lanes: list[str]
    weight: int
    order: int
    capabilities: list[str]
    context_window: int
    context_length: int
    quality_score: float
    prompt_per_1m: float
    completion_per_1m: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        target = self.target

        lanes = self.lanes

        weight = self.weight

        order = self.order

        capabilities = self.capabilities

        context_window = self.context_window

        context_length = self.context_length

        quality_score = self.quality_score

        prompt_per_1m = self.prompt_per_1m

        completion_per_1m = self.completion_per_1m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
                "target": target,
                "lanes": lanes,
                "weight": weight,
                "order": order,
                "capabilities": capabilities,
                "context_window": context_window,
                "context_length": context_length,
                "quality_score": quality_score,
                "prompt_per_1m": prompt_per_1m,
                "completion_per_1m": completion_per_1m,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reference = d.pop("reference")

        target = d.pop("target")

        lanes = cast(list[str], d.pop("lanes"))

        weight = d.pop("weight")

        order = d.pop("order")

        capabilities = cast(list[str], d.pop("capabilities"))

        context_window = d.pop("context_window")

        context_length = d.pop("context_length")

        quality_score = d.pop("quality_score")

        prompt_per_1m = d.pop("prompt_per_1m")

        completion_per_1m = d.pop("completion_per_1m")

        published_router_candidate = cls(
            reference=reference,
            target=target,
            lanes=lanes,
            weight=weight,
            order=order,
            capabilities=capabilities,
            context_window=context_window,
            context_length=context_length,
            quality_score=quality_score,
            prompt_per_1m=prompt_per_1m,
            completion_per_1m=completion_per_1m,
        )

        published_router_candidate.additional_properties = d
        return published_router_candidate

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
