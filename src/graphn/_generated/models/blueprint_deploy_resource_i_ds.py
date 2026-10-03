from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="BlueprintDeployResourceIDs")


@_attrs_define
class BlueprintDeployResourceIDs:
    """
    Attributes:
        agents (list[str]):
        functions (list[str]):
        mcp_servers (list[str]):
    """

    agents: list[str]
    functions: list[str]
    mcp_servers: list[str]

    def to_dict(self) -> dict[str, Any]:
        agents = self.agents

        functions = self.functions

        mcp_servers = self.mcp_servers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agents": agents,
                "functions": functions,
                "mcp_servers": mcp_servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        agents = cast(list[str], d.pop("agents"))

        functions = cast(list[str], d.pop("functions"))

        mcp_servers = cast(list[str], d.pop("mcp_servers"))

        blueprint_deploy_resource_i_ds = cls(
            agents=agents,
            functions=functions,
            mcp_servers=mcp_servers,
        )

        return blueprint_deploy_resource_i_ds
