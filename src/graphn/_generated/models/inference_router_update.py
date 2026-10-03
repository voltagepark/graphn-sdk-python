from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.inference_router_update_fallback_policy import (
    InferenceRouterUpdateFallbackPolicy,
)
from ..models.inference_router_update_preset import InferenceRouterUpdatePreset
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inference_router_candidate import InferenceRouterCandidate


T = TypeVar("T", bound="InferenceRouterUpdate")


@_attrs_define
class InferenceRouterUpdate:
    """
    Attributes:
        expected_revision (int):
        display_name (str | Unset):
        preset (InferenceRouterUpdatePreset | Unset):
        candidates (list[InferenceRouterCandidate] | Unset):
        fallback_policy (InferenceRouterUpdateFallbackPolicy | Unset):
    """

    expected_revision: int
    display_name: str | Unset = UNSET
    preset: InferenceRouterUpdatePreset | Unset = UNSET
    candidates: list[InferenceRouterCandidate] | Unset = UNSET
    fallback_policy: InferenceRouterUpdateFallbackPolicy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expected_revision = self.expected_revision

        display_name = self.display_name

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset.value

        candidates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.candidates, Unset):
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
                "expected_revision": expected_revision,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if preset is not UNSET:
            field_dict["preset"] = preset
        if candidates is not UNSET:
            field_dict["candidates"] = candidates
        if fallback_policy is not UNSET:
            field_dict["fallback_policy"] = fallback_policy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_candidate import (
            InferenceRouterCandidate,
        )

        d = dict(src_dict)
        expected_revision = d.pop("expected_revision")

        display_name = d.pop("display_name", UNSET)

        _preset = d.pop("preset", UNSET)
        preset: InferenceRouterUpdatePreset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = InferenceRouterUpdatePreset(_preset)

        _candidates = d.pop("candidates", UNSET)
        candidates: list[InferenceRouterCandidate] | Unset = UNSET
        if _candidates is not UNSET:
            candidates = []
            for candidates_item_data in _candidates:
                candidates_item = InferenceRouterCandidate.from_dict(
                    candidates_item_data
                )

                candidates.append(candidates_item)

        _fallback_policy = d.pop("fallback_policy", UNSET)
        fallback_policy: InferenceRouterUpdateFallbackPolicy | Unset
        if isinstance(_fallback_policy, Unset):
            fallback_policy = UNSET
        else:
            fallback_policy = InferenceRouterUpdateFallbackPolicy(_fallback_policy)

        inference_router_update = cls(
            expected_revision=expected_revision,
            display_name=display_name,
            preset=preset,
            candidates=candidates,
            fallback_policy=fallback_policy,
        )

        return inference_router_update
