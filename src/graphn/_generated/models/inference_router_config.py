from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.inference_router_config_fallback_policy import (
    InferenceRouterConfigFallbackPolicy,
)
from ..models.inference_router_config_preset import InferenceRouterConfigPreset
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inference_router_candidate import InferenceRouterCandidate


T = TypeVar("T", bound="InferenceRouterConfig")


@_attrs_define
class InferenceRouterConfig:
    """
    Attributes:
        preset (InferenceRouterConfigPreset):
        candidates (list[InferenceRouterCandidate]):
        fallback_policy (InferenceRouterConfigFallbackPolicy | Unset): What callers get when no shard can classify the
            request. `degraded_general` serves the highest-weight general candidate without classification, trading routing
            quality for availability. Default: InferenceRouterConfigFallbackPolicy.FAIL_CLOSED.
    """

    preset: InferenceRouterConfigPreset
    candidates: list[InferenceRouterCandidate]
    fallback_policy: InferenceRouterConfigFallbackPolicy | Unset = (
        InferenceRouterConfigFallbackPolicy.FAIL_CLOSED
    )

    def to_dict(self) -> dict[str, Any]:
        preset = self.preset.value

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        fallback_policy: str | Unset = UNSET
        if not isinstance(self.fallback_policy, Unset):
            fallback_policy = self.fallback_policy.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "preset": preset,
                "candidates": candidates,
            }
        )
        if fallback_policy is not UNSET:
            field_dict["fallback_policy"] = fallback_policy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_candidate import (
            InferenceRouterCandidate,
        )

        d = dict(src_dict)
        preset = InferenceRouterConfigPreset(d.pop("preset"))

        candidates = []
        _candidates = d.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = InferenceRouterCandidate.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        _fallback_policy = d.pop("fallback_policy", UNSET)
        fallback_policy: InferenceRouterConfigFallbackPolicy | Unset
        if isinstance(_fallback_policy, Unset):
            fallback_policy = UNSET
        else:
            fallback_policy = InferenceRouterConfigFallbackPolicy(_fallback_policy)

        inference_router_config = cls(
            preset=preset,
            candidates=candidates,
            fallback_policy=fallback_policy,
        )

        return inference_router_config
