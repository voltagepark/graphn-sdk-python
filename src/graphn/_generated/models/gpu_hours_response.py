from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GpuHoursResponse")


@_attrs_define
class GpuHoursResponse:
    """
    Attributes:
        gpu_hours (float): Cumulative GPU-hours consumed by this model. For an adapter, the
            base's: an adapter bills no GPU time of its own.
        shared (bool | Unset): Preview. `true` when `gpu_hours` is an adapter's base's.
        parent_model_id (str | Unset): Preview. With `shared`, the base the hours belong to.
    """

    gpu_hours: float
    shared: bool | Unset = UNSET
    parent_model_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gpu_hours = self.gpu_hours

        shared = self.shared

        parent_model_id = self.parent_model_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gpu_hours": gpu_hours,
            }
        )
        if shared is not UNSET:
            field_dict["shared"] = shared
        if parent_model_id is not UNSET:
            field_dict["parent_model_id"] = parent_model_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gpu_hours = d.pop("gpu_hours")

        shared = d.pop("shared", UNSET)

        parent_model_id = d.pop("parent_model_id", UNSET)

        gpu_hours_response = cls(
            gpu_hours=gpu_hours,
            shared=shared,
            parent_model_id=parent_model_id,
        )

        return gpu_hours_response
