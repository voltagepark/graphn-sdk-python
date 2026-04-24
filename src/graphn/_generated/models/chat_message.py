from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_message_role import ChatMessageRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message_tool_calls_item import ChatMessageToolCallsItem


T = TypeVar("T", bound="ChatMessage")


@_attrs_define
class ChatMessage:
    """OpenAI chat message. `content` may be a string, an array of
    content parts (text + image / audio / video), or null when
    `tool_calls` is set. See the OpenAI Chat Completions reference
    for the canonical shape; we forward the entire object unchanged.

        Attributes:
            role (ChatMessageRole):
            name (str | Unset):
            tool_call_id (str | Unset):
            tool_calls (list[ChatMessageToolCallsItem] | Unset):
    """

    role: ChatMessageRole
    name: str | Unset = UNSET
    tool_call_id: str | Unset = UNSET
    tool_calls: list[ChatMessageToolCallsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        name = self.name

        tool_call_id = self.tool_call_id

        tool_calls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = []
            for tool_calls_item_data in self.tool_calls:
                tool_calls_item = tool_calls_item_data.to_dict()
                tool_calls.append(tool_calls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if tool_call_id is not UNSET:
            field_dict["tool_call_id"] = tool_call_id
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message_tool_calls_item import ChatMessageToolCallsItem

        d = dict(src_dict)
        role = ChatMessageRole(d.pop("role"))

        name = d.pop("name", UNSET)

        tool_call_id = d.pop("tool_call_id", UNSET)

        _tool_calls = d.pop("tool_calls", UNSET)
        tool_calls: list[ChatMessageToolCallsItem] | Unset = UNSET
        if _tool_calls is not UNSET:
            tool_calls = []
            for tool_calls_item_data in _tool_calls:
                tool_calls_item = ChatMessageToolCallsItem.from_dict(
                    tool_calls_item_data
                )

                tool_calls.append(tool_calls_item)

        chat_message = cls(
            role=role,
            name=name,
            tool_call_id=tool_call_id,
            tool_calls=tool_calls,
        )

        chat_message.additional_properties = d
        return chat_message

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
