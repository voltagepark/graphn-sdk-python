from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GpuHoursResponse")


@_attrs_define
class GpuHoursResponse:
    """
    Attributes:
        gpu_hours (float): Cumulative GPU-hours consumed by this model.
    """

    gpu_hours: float

    def to_dict(self) -> dict[str, Any]:
        gpu_hours = self.gpu_hours

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gpu_hours": gpu_hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gpu_hours = d.pop("gpu_hours")

        gpu_hours_response = cls(
            gpu_hours=gpu_hours,
        )

        return gpu_hours_response
