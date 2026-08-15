from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlueprintSummary")


@_attrs_define
class BlueprintSummary:
    """
    Attributes:
        id (str):
        name (str):
        description (str | Unset):
        category (str | Unset):
        pattern (str | Unset):
        agents (int | Unset):
        functions (int | Unset):
        mcp_servers (int | Unset):
    """

    id: str
    name: str
    description: str | Unset = UNSET
    category: str | Unset = UNSET
    pattern: str | Unset = UNSET
    agents: int | Unset = UNSET
    functions: int | Unset = UNSET
    mcp_servers: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        category = self.category

        pattern = self.pattern

        agents = self.agents

        functions = self.functions

        mcp_servers = self.mcp_servers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if agents is not UNSET:
            field_dict["agents"] = agents
        if functions is not UNSET:
            field_dict["functions"] = functions
        if mcp_servers is not UNSET:
            field_dict["mcp_servers"] = mcp_servers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        category = d.pop("category", UNSET)

        pattern = d.pop("pattern", UNSET)

        agents = d.pop("agents", UNSET)

        functions = d.pop("functions", UNSET)

        mcp_servers = d.pop("mcp_servers", UNSET)

        blueprint_summary = cls(
            id=id,
            name=name,
            description=description,
            category=category,
            pattern=pattern,
            agents=agents,
            functions=functions,
            mcp_servers=mcp_servers,
        )

        blueprint_summary.additional_properties = d
        return blueprint_summary

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
