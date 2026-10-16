from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AgentRunRequest")


@_attrs_define
class AgentRunRequest:
    """
    Attributes:
        input_ (str):
    """

    input_: str

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "input": input_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        input_ = d.pop("input")

        agent_run_request = cls(
            input_=input_,
        )

        return agent_run_request
