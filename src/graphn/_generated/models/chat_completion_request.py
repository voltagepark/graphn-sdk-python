from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_request_response_format import (
        ChatCompletionRequestResponseFormat,
    )
    from ..models.chat_completion_request_tool_choice_type_1 import (
        ChatCompletionRequestToolChoiceType1,
    )
    from ..models.chat_completion_request_tools_item import (
        ChatCompletionRequestToolsItem,
    )
    from ..models.chat_message import ChatMessage


T = TypeVar("T", bound="ChatCompletionRequest")


@_attrs_define
class ChatCompletionRequest:
    """OpenAI-compatible chat completion request. Additional fields not
    listed here are forwarded to the upstream model unchanged. See
    the OpenAI Chat Completions reference for the full set.

        Attributes:
            model (str): Model name (built-in alias or custom model `name`). For
                imported models, use `imported:<id>`; for custom models you
                may use either `<name>` or `custom:<id>`.
            messages (list[ChatMessage]):
            stream (bool | Unset):  Default: False.
            temperature (float | Unset):
            top_p (float | Unset):
            max_tokens (int | Unset):
            max_completion_tokens (int | Unset):
            tools (list[ChatCompletionRequestToolsItem] | Unset):
            tool_choice (ChatCompletionRequestToolChoiceType1 | str | Unset):
            response_format (ChatCompletionRequestResponseFormat | Unset):
            stop (list[str] | str | Unset):
            n (int | Unset):  Default: 1.
            seed (int | Unset):
            user (str | Unset):
    """

    model: str
    messages: list[ChatMessage]
    stream: bool | Unset = False
    temperature: float | Unset = UNSET
    top_p: float | Unset = UNSET
    max_tokens: int | Unset = UNSET
    max_completion_tokens: int | Unset = UNSET
    tools: list[ChatCompletionRequestToolsItem] | Unset = UNSET
    tool_choice: ChatCompletionRequestToolChoiceType1 | str | Unset = UNSET
    response_format: ChatCompletionRequestResponseFormat | Unset = UNSET
    stop: list[str] | str | Unset = UNSET
    n: int | Unset = 1
    seed: int | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_request_tool_choice_type_1 import (
            ChatCompletionRequestToolChoiceType1,
        )

        model = self.model

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        stream = self.stream

        temperature = self.temperature

        top_p = self.top_p

        max_tokens = self.max_tokens

        max_completion_tokens = self.max_completion_tokens

        tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)

        tool_choice: dict[str, Any] | str | Unset
        if isinstance(self.tool_choice, Unset):
            tool_choice = UNSET
        elif isinstance(self.tool_choice, ChatCompletionRequestToolChoiceType1):
            tool_choice = self.tool_choice.to_dict()
        else:
            tool_choice = self.tool_choice

        response_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = self.response_format.to_dict()

        stop: list[str] | str | Unset
        if isinstance(self.stop, Unset):
            stop = UNSET
        elif isinstance(self.stop, list):
            stop = self.stop

        else:
            stop = self.stop

        n = self.n

        seed = self.seed

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "messages": messages,
            }
        )
        if stream is not UNSET:
            field_dict["stream"] = stream
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if max_completion_tokens is not UNSET:
            field_dict["max_completion_tokens"] = max_completion_tokens
        if tools is not UNSET:
            field_dict["tools"] = tools
        if tool_choice is not UNSET:
            field_dict["tool_choice"] = tool_choice
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if stop is not UNSET:
            field_dict["stop"] = stop
        if n is not UNSET:
            field_dict["n"] = n
        if seed is not UNSET:
            field_dict["seed"] = seed
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_request_response_format import (
            ChatCompletionRequestResponseFormat,
        )
        from ..models.chat_completion_request_tool_choice_type_1 import (
            ChatCompletionRequestToolChoiceType1,
        )
        from ..models.chat_completion_request_tools_item import (
            ChatCompletionRequestToolsItem,
        )
        from ..models.chat_message import ChatMessage

        d = dict(src_dict)
        model = d.pop("model")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = ChatMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        stream = d.pop("stream", UNSET)

        temperature = d.pop("temperature", UNSET)

        top_p = d.pop("top_p", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        max_completion_tokens = d.pop("max_completion_tokens", UNSET)

        _tools = d.pop("tools", UNSET)
        tools: list[ChatCompletionRequestToolsItem] | Unset = UNSET
        if _tools is not UNSET:
            tools = []
            for tools_item_data in _tools:
                tools_item = ChatCompletionRequestToolsItem.from_dict(tools_item_data)

                tools.append(tools_item)

        def _parse_tool_choice(
            data: object,
        ) -> ChatCompletionRequestToolChoiceType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_choice_type_1 = ChatCompletionRequestToolChoiceType1.from_dict(
                    data
                )

                return tool_choice_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionRequestToolChoiceType1 | str | Unset, data)

        tool_choice = _parse_tool_choice(d.pop("tool_choice", UNSET))

        _response_format = d.pop("response_format", UNSET)
        response_format: ChatCompletionRequestResponseFormat | Unset
        if isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = ChatCompletionRequestResponseFormat.from_dict(
                _response_format
            )

        def _parse_stop(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stop_type_1 = cast(list[str], data)

                return stop_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        stop = _parse_stop(d.pop("stop", UNSET))

        n = d.pop("n", UNSET)

        seed = d.pop("seed", UNSET)

        user = d.pop("user", UNSET)

        chat_completion_request = cls(
            model=model,
            messages=messages,
            stream=stream,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            max_completion_tokens=max_completion_tokens,
            tools=tools,
            tool_choice=tool_choice,
            response_format=response_format,
            stop=stop,
            n=n,
            seed=seed,
            user=user,
        )

        chat_completion_request.additional_properties = d
        return chat_completion_request

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
