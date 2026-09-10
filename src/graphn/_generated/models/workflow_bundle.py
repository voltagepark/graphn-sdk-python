from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow import Workflow
    from ..models.workflow_bundle_agents_item import WorkflowBundleAgentsItem
    from ..models.workflow_bundle_functions_item import WorkflowBundleFunctionsItem
    from ..models.workflow_bundle_mcp_servers_item import WorkflowBundleMcpServersItem


T = TypeVar("T", bound="WorkflowBundle")


@_attrs_define
class WorkflowBundle:
    """
    Attributes:
        workflow (Workflow | Unset):
        agents (list[WorkflowBundleAgentsItem] | Unset):
        functions (list[WorkflowBundleFunctionsItem] | Unset):
        mcp_servers (list[WorkflowBundleMcpServersItem] | Unset):
    """

    workflow: Workflow | Unset = UNSET
    agents: list[WorkflowBundleAgentsItem] | Unset = UNSET
    functions: list[WorkflowBundleFunctionsItem] | Unset = UNSET
    mcp_servers: list[WorkflowBundleMcpServersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

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
        field_dict.update({})
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if agents is not UNSET:
            field_dict["agents"] = agents
        if functions is not UNSET:
            field_dict["functions"] = functions
        if mcp_servers is not UNSET:
            field_dict["mcp_servers"] = mcp_servers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow import Workflow
        from ..models.workflow_bundle_agents_item import (
            WorkflowBundleAgentsItem,
        )
        from ..models.workflow_bundle_functions_item import (
            WorkflowBundleFunctionsItem,
        )
        from ..models.workflow_bundle_mcp_servers_item import (
            WorkflowBundleMcpServersItem,
        )

        d = dict(src_dict)
        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        _agents = d.pop("agents", UNSET)
        agents: list[WorkflowBundleAgentsItem] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = WorkflowBundleAgentsItem.from_dict(agents_item_data)

                agents.append(agents_item)

        _functions = d.pop("functions", UNSET)
        functions: list[WorkflowBundleFunctionsItem] | Unset = UNSET
        if _functions is not UNSET:
            functions = []
            for functions_item_data in _functions:
                functions_item = WorkflowBundleFunctionsItem.from_dict(
                    functions_item_data
                )

                functions.append(functions_item)

        _mcp_servers = d.pop("mcp_servers", UNSET)
        mcp_servers: list[WorkflowBundleMcpServersItem] | Unset = UNSET
        if _mcp_servers is not UNSET:
            mcp_servers = []
            for mcp_servers_item_data in _mcp_servers:
                mcp_servers_item = WorkflowBundleMcpServersItem.from_dict(
                    mcp_servers_item_data
                )

                mcp_servers.append(mcp_servers_item)

        workflow_bundle = cls(
            workflow=workflow,
            agents=agents,
            functions=functions,
            mcp_servers=mcp_servers,
        )

        workflow_bundle.additional_properties = d
        return workflow_bundle

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
