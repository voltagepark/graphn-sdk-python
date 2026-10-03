from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_spec_output_schema import AgentSpecOutputSchema
    from ..models.model_settings import ModelSettings
    from ..models.tool_reference import ToolReference


T = TypeVar("T", bound="AgentSpec")


@_attrs_define
class AgentSpec:
    """
    Attributes:
        instructions (str | Unset):
        model (str | Unset):
        mcp_tools (list[ToolReference] | Unset):
        knowledge_base_id (str | Unset):
        output_schema (AgentSpecOutputSchema | Unset):
        timeout_seconds (int | Unset):
        max_llm_calls (int | Unset):
        model_settings (ModelSettings | Unset):
    """

    instructions: str | Unset = UNSET
    model: str | Unset = UNSET
    mcp_tools: list[ToolReference] | Unset = UNSET
    knowledge_base_id: str | Unset = UNSET
    output_schema: AgentSpecOutputSchema | Unset = UNSET
    timeout_seconds: int | Unset = UNSET
    max_llm_calls: int | Unset = UNSET
    model_settings: ModelSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instructions = self.instructions

        model = self.model

        mcp_tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mcp_tools, Unset):
            mcp_tools = []
            for mcp_tools_item_data in self.mcp_tools:
                mcp_tools_item = mcp_tools_item_data.to_dict()
                mcp_tools.append(mcp_tools_item)

        knowledge_base_id = self.knowledge_base_id

        output_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_schema, Unset):
            output_schema = self.output_schema.to_dict()

        timeout_seconds = self.timeout_seconds

        max_llm_calls = self.max_llm_calls

        model_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_settings, Unset):
            model_settings = self.model_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if model is not UNSET:
            field_dict["model"] = model
        if mcp_tools is not UNSET:
            field_dict["mcp_tools"] = mcp_tools
        if knowledge_base_id is not UNSET:
            field_dict["knowledge_base_id"] = knowledge_base_id
        if output_schema is not UNSET:
            field_dict["output_schema"] = output_schema
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds
        if max_llm_calls is not UNSET:
            field_dict["max_llm_calls"] = max_llm_calls
        if model_settings is not UNSET:
            field_dict["model_settings"] = model_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.agent_spec_output_schema import (
            AgentSpecOutputSchema,
        )
        from ..models.model_settings import ModelSettings
        from ..models.tool_reference import ToolReference

        d = dict(src_dict)
        instructions = d.pop("instructions", UNSET)

        model = d.pop("model", UNSET)

        _mcp_tools = d.pop("mcp_tools", UNSET)
        mcp_tools: list[ToolReference] | Unset = UNSET
        if _mcp_tools is not UNSET:
            mcp_tools = []
            for mcp_tools_item_data in _mcp_tools:
                mcp_tools_item = ToolReference.from_dict(mcp_tools_item_data)

                mcp_tools.append(mcp_tools_item)

        knowledge_base_id = d.pop("knowledge_base_id", UNSET)

        _output_schema = d.pop("output_schema", UNSET)
        output_schema: AgentSpecOutputSchema | Unset
        if isinstance(_output_schema, Unset):
            output_schema = UNSET
        else:
            output_schema = AgentSpecOutputSchema.from_dict(_output_schema)

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        max_llm_calls = d.pop("max_llm_calls", UNSET)

        _model_settings = d.pop("model_settings", UNSET)
        model_settings: ModelSettings | Unset
        if isinstance(_model_settings, Unset):
            model_settings = UNSET
        else:
            model_settings = ModelSettings.from_dict(_model_settings)

        agent_spec = cls(
            instructions=instructions,
            model=model,
            mcp_tools=mcp_tools,
            knowledge_base_id=knowledge_base_id,
            output_schema=output_schema,
            timeout_seconds=timeout_seconds,
            max_llm_calls=max_llm_calls,
            model_settings=model_settings,
        )

        agent_spec.additional_properties = d
        return agent_spec

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
