from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomModelUpdate")


@_attrs_define
class CustomModelUpdate:
    """Partial-update payload for `PATCH /v1/{workspaceId}/custom-models/{modelId}`.
    All fields are independently optional; omitted fields are left
    unchanged. At least one field MUST be supplied.

    Only a small, vetted set of fields are mutable post-create.
    Immutable fields (`huggingface_model_id`, `weight_source`,
    GPU topology, …) are not exposed here — change them by
    deleting and re-creating the model.

        Attributes:
            name (str | Unset): Display name. Persisted to the model record only.
            min_replicas (int | Unset): New floor for the autoscaler. `0` re-enables scale-to-zero;
                any value `>= 1` keeps the model warm. Applied to the live
                deployment in place — no rolling restart, no downtime.
            max_replicas (int | Unset): New ceiling for the autoscaler. KServe propagates the value
                to the underlying KEDA `ScaledObject`'s `maxReplicaCount` on
                its next reconcile. Applied to the live deployment in place.
            cooldown_seconds (int | Unset): Idle period (in seconds) the controller waits before scaling
                an idle replica back to zero. Persisted to the model record;
                the controller picks it up on the next reconcile.
    """

    name: str | Unset = UNSET
    min_replicas: int | Unset = UNSET
    max_replicas: int | Unset = UNSET
    cooldown_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        min_replicas = self.min_replicas

        max_replicas = self.max_replicas

        cooldown_seconds = self.cooldown_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if min_replicas is not UNSET:
            field_dict["min_replicas"] = min_replicas
        if max_replicas is not UNSET:
            field_dict["max_replicas"] = max_replicas
        if cooldown_seconds is not UNSET:
            field_dict["cooldown_seconds"] = cooldown_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        min_replicas = d.pop("min_replicas", UNSET)

        max_replicas = d.pop("max_replicas", UNSET)

        cooldown_seconds = d.pop("cooldown_seconds", UNSET)

        custom_model_update = cls(
            name=name,
            min_replicas=min_replicas,
            max_replicas=max_replicas,
            cooldown_seconds=cooldown_seconds,
        )

        return custom_model_update
