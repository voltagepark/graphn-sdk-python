from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_connection_response_usage import TestConnectionResponseUsage


T = TypeVar("T", bound="TestConnectionResponse")


@_attrs_define
class TestConnectionResponse:
    """
    Attributes:
        response (str): Text content of the upstream response.
        model (str): Model id echoed back by the upstream.
        usage (TestConnectionResponseUsage | Unset): Optional token usage stats from the upstream.
    """

    response: str
    model: str
    usage: TestConnectionResponseUsage | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        response = self.response

        model = self.model

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "response": response,
                "model": model,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_connection_response_usage import TestConnectionResponseUsage

        d = dict(src_dict)
        response = d.pop("response")

        model = d.pop("model")

        _usage = d.pop("usage", UNSET)
        usage: TestConnectionResponseUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = TestConnectionResponseUsage.from_dict(_usage)

        test_connection_response = cls(
            response=response,
            model=model,
            usage=usage,
        )

        return test_connection_response
