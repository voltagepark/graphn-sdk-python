from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.inference_router_create_fallback_policy import (
    InferenceRouterCreateFallbackPolicy,
)
from ..models.inference_router_create_preset import InferenceRouterCreatePreset
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inference_router_candidate import InferenceRouterCandidate


T = TypeVar("T", bound="InferenceRouterCreate")


@_attrs_define
class InferenceRouterCreate:
    """
    Attributes:
        name (str):
        preset (InferenceRouterCreatePreset):
        candidates (list[InferenceRouterCandidate]):
        display_name (str | Unset):
        fallback_policy (InferenceRouterCreateFallbackPolicy | Unset):  Default:
            InferenceRouterCreateFallbackPolicy.FAIL_CLOSED.
    """

    name: str
    preset: InferenceRouterCreatePreset
    candidates: list[InferenceRouterCandidate]
    display_name: str | Unset = UNSET
    fallback_policy: InferenceRouterCreateFallbackPolicy | Unset = (
        InferenceRouterCreateFallbackPolicy.FAIL_CLOSED
    )

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        preset = self.preset.value

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        display_name = self.display_name

        fallback_policy: str | Unset = UNSET
        if not isinstance(self.fallback_policy, Unset):
            fallback_policy = self.fallback_policy.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "preset": preset,
                "candidates": candidates,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if fallback_policy is not UNSET:
            field_dict["fallback_policy"] = fallback_policy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_candidate import (
            InferenceRouterCandidate,
        )

        d = dict(src_dict)
        name = d.pop("name")

        preset = InferenceRouterCreatePreset(d.pop("preset"))

        candidates = []
        _candidates = d.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = InferenceRouterCandidate.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        display_name = d.pop("display_name", UNSET)

        _fallback_policy = d.pop("fallback_policy", UNSET)
        fallback_policy: InferenceRouterCreateFallbackPolicy | Unset
        if isinstance(_fallback_policy, Unset):
            fallback_policy = UNSET
        else:
            fallback_policy = InferenceRouterCreateFallbackPolicy(_fallback_policy)

        inference_router_create = cls(
            name=name,
            preset=preset,
            candidates=candidates,
            display_name=display_name,
            fallback_policy=fallback_policy,
        )

        return inference_router_create
