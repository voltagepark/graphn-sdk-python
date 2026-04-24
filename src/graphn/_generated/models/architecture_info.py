from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.capability import Capability

T = TypeVar("T", bound="ArchitectureInfo")


@_attrs_define
class ArchitectureInfo:
    """
    Attributes:
        name (str): HuggingFace architecture identifier (e.g. `LlamaForCausalLM`).
        capabilities (list[Capability]):
    """

    name: str
    capabilities: list[Capability]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        capabilities = []
        for capabilities_item_data in self.capabilities:
            capabilities_item = capabilities_item_data.value
            capabilities.append(capabilities_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "capabilities": capabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        capabilities = []
        _capabilities = d.pop("capabilities")
        for capabilities_item_data in _capabilities:
            capabilities_item = Capability(capabilities_item_data)

            capabilities.append(capabilities_item)

        architecture_info = cls(
            name=name,
            capabilities=capabilities,
        )

        return architecture_info
