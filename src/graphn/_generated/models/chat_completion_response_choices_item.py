from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message import ChatMessage


T = TypeVar("T", bound="ChatCompletionResponseChoicesItem")


@_attrs_define
class ChatCompletionResponseChoicesItem:
    """
    Attributes:
        index (int):
        message (ChatMessage): OpenAI chat message. `content` may be a string, an array of
            content parts (text + image / audio / video), or null when
            `tool_calls` is set. See the OpenAI Chat Completions reference
            for the canonical shape; we forward the entire object unchanged.
        finish_reason (None | str | Unset):
    """

    index: int
    message: ChatMessage
    finish_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        message = self.message.to_dict()

        finish_reason: None | str | Unset
        if isinstance(self.finish_reason, Unset):
            finish_reason = UNSET
        else:
            finish_reason = self.finish_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "message": message,
            }
        )
        if finish_reason is not UNSET:
            field_dict["finish_reason"] = finish_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message import ChatMessage

        d = dict(src_dict)
        index = d.pop("index")

        message = ChatMessage.from_dict(d.pop("message"))

        def _parse_finish_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finish_reason = _parse_finish_reason(d.pop("finish_reason", UNSET))

        chat_completion_response_choices_item = cls(
            index=index,
            message=message,
            finish_reason=finish_reason,
        )

        chat_completion_response_choices_item.additional_properties = d
        return chat_completion_response_choices_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
