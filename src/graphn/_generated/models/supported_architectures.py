from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.architecture_info import ArchitectureInfo


T = TypeVar("T", bound="SupportedArchitectures")


@_attrs_define
class SupportedArchitectures:
    """
    Attributes:
        architectures (list[ArchitectureInfo]): Sorted (by `name`) list of architectures the platform's serving
            runtimes can deploy.
    """

    architectures: list[ArchitectureInfo]

    def to_dict(self) -> dict[str, Any]:
        architectures = []
        for architectures_item_data in self.architectures:
            architectures_item = architectures_item_data.to_dict()
            architectures.append(architectures_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "architectures": architectures,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.architecture_info import ArchitectureInfo

        d = dict(src_dict)
        architectures = []
        _architectures = d.pop("architectures")
        for architectures_item_data in _architectures:
            architectures_item = ArchitectureInfo.from_dict(architectures_item_data)

            architectures.append(architectures_item)

        supported_architectures = cls(
            architectures=architectures,
        )

        return supported_architectures
