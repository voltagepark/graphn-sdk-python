from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestConnectionRequest")


@_attrs_define
class TestConnectionRequest:
    """
    Attributes:
        endpoint (str):
        model_id (str): Upstream model identifier to test against.
        api_key_secret_id (str | Unset): Workspace secret with the upstream API key. Optional for unauthenticated
            endpoints.
        message (str | Unset): Test prompt. Defaults to `"Hello, respond in one sentence."`.
    """

    endpoint: str
    model_id: str
    api_key_secret_id: str | Unset = UNSET
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        model_id = self.model_id

        api_key_secret_id = self.api_key_secret_id

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
                "model_id": model_id,
            }
        )
        if api_key_secret_id is not UNSET:
            field_dict["api_key_secret_id"] = api_key_secret_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        model_id = d.pop("model_id")

        api_key_secret_id = d.pop("api_key_secret_id", UNSET)

        message = d.pop("message", UNSET)

        test_connection_request = cls(
            endpoint=endpoint,
            model_id=model_id,
            api_key_secret_id=api_key_secret_id,
            message=message,
        )

        return test_connection_request
