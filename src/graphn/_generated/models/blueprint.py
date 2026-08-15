from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blueprint_agents_item import BlueprintAgentsItem
    from ..models.blueprint_functions_item import BlueprintFunctionsItem
    from ..models.blueprint_mcp_servers_item import BlueprintMcpServersItem


T = TypeVar("T", bound="Blueprint")


@_attrs_define
class Blueprint:
    """
    Attributes:
        id (str):
        name (str):
        dsl (str):
        description (str | Unset):
        category (str | Unset):
        pattern (str | Unset):
        agents (list[BlueprintAgentsItem] | Unset):
        functions (list[BlueprintFunctionsItem] | Unset):
        mcp_servers (list[BlueprintMcpServersItem] | Unset):
    """

    id: str
    name: str
    dsl: str
    description: str | Unset = UNSET
    category: str | Unset = UNSET
    pattern: str | Unset = UNSET
    agents: list[BlueprintAgentsItem] | Unset = UNSET
    functions: list[BlueprintFunctionsItem] | Unset = UNSET
    mcp_servers: list[BlueprintMcpServersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        dsl = self.dsl

        description = self.description

        category = self.category

        pattern = self.pattern

        agents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()
                agents.append(agents_item)

        functions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.functions, Unset):
            functions = []
            for functions_item_data in self.functions:
                functions_item = functions_item_data.to_dict()
                functions.append(functions_item)

        mcp_servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mcp_servers, Unset):
            mcp_servers = []
            for mcp_servers_item_data in self.mcp_servers:
                mcp_servers_item = mcp_servers_item_data.to_dict()
                mcp_servers.append(mcp_servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "dsl": dsl,
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
        from ..models.blueprint_agents_item import BlueprintAgentsItem
        from ..models.blueprint_functions_item import BlueprintFunctionsItem
        from ..models.blueprint_mcp_servers_item import BlueprintMcpServersItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        dsl = d.pop("dsl")

        description = d.pop("description", UNSET)

        category = d.pop("category", UNSET)

        pattern = d.pop("pattern", UNSET)

        _agents = d.pop("agents", UNSET)
        agents: list[BlueprintAgentsItem] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = BlueprintAgentsItem.from_dict(agents_item_data)

                agents.append(agents_item)

        _functions = d.pop("functions", UNSET)
        functions: list[BlueprintFunctionsItem] | Unset = UNSET
        if _functions is not UNSET:
            functions = []
            for functions_item_data in _functions:
                functions_item = BlueprintFunctionsItem.from_dict(functions_item_data)

                functions.append(functions_item)

        _mcp_servers = d.pop("mcp_servers", UNSET)
        mcp_servers: list[BlueprintMcpServersItem] | Unset = UNSET
        if _mcp_servers is not UNSET:
            mcp_servers = []
            for mcp_servers_item_data in _mcp_servers:
                mcp_servers_item = BlueprintMcpServersItem.from_dict(
                    mcp_servers_item_data
                )

                mcp_servers.append(mcp_servers_item)

        blueprint = cls(
            id=id,
            name=name,
            dsl=dsl,
            description=description,
            category=category,
            pattern=pattern,
            agents=agents,
            functions=functions,
            mcp_servers=mcp_servers,
        )

        blueprint.additional_properties = d
        return blueprint

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
