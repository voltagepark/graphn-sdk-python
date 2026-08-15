from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelSettings")


@_attrs_define
class ModelSettings:
    """
    Attributes:
        temperature (float | Unset):
        top_p (float | Unset):
        enable_thinking (bool | Unset):
        reasoning_effort (str | Unset):
    """

    temperature: float | Unset = UNSET
    top_p: float | Unset = UNSET
    enable_thinking: bool | Unset = UNSET
    reasoning_effort: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        temperature = self.temperature

        top_p = self.top_p

        enable_thinking = self.enable_thinking

        reasoning_effort = self.reasoning_effort

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if enable_thinking is not UNSET:
            field_dict["enable_thinking"] = enable_thinking
        if reasoning_effort is not UNSET:
            field_dict["reasoning_effort"] = reasoning_effort

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        temperature = d.pop("temperature", UNSET)

        top_p = d.pop("top_p", UNSET)

        enable_thinking = d.pop("enable_thinking", UNSET)

        reasoning_effort = d.pop("reasoning_effort", UNSET)

        model_settings = cls(
            temperature=temperature,
            top_p=top_p,
            enable_thinking=enable_thinking,
            reasoning_effort=reasoning_effort,
        )

        return model_settings
