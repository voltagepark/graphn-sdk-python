from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ArchitectureInfo")


@_attrs_define
class ArchitectureInfo:
    """
    Attributes:
        name (str): HuggingFace `architectures[0]` value (e.g. `LlamaForCausalLM`,
            `Qwen3VLMoeForConditionalGeneration`).
        capabilities (list[str]): Capability tags this architecture exposes — `tool_calling`,
            `vision`, `image_input`, `video_input`, `streaming`, `json_mode`.
            Drives the UI capability filters and AF's per-feature gating.
    """

    name: str
    capabilities: list[str]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        capabilities = self.capabilities

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

        capabilities = cast(list[str], d.pop("capabilities"))

        architecture_info = cls(
            name=name,
            capabilities=capabilities,
        )

        return architecture_info
