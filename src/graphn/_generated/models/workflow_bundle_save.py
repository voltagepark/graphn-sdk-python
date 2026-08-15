from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_resource_item import BundleResourceItem
    from ..models.workflow_update import WorkflowUpdate


T = TypeVar("T", bound="WorkflowBundleSave")


@_attrs_define
class WorkflowBundleSave:
    """
    Attributes:
        workflow (WorkflowUpdate | Unset):
        agents (list[BundleResourceItem] | Unset):
        functions (list[BundleResourceItem] | Unset):
        mcp_servers (list[BundleResourceItem] | Unset):
    """

    workflow: WorkflowUpdate | Unset = UNSET
    agents: list[BundleResourceItem] | Unset = UNSET
    functions: list[BundleResourceItem] | Unset = UNSET
    mcp_servers: list[BundleResourceItem] | Unset = UNSET

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
        from ..models.bundle_resource_item import BundleResourceItem
        from ..models.workflow_update import WorkflowUpdate

        d = dict(src_dict)
        _workflow = d.pop("workflow", UNSET)
        workflow: WorkflowUpdate | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WorkflowUpdate.from_dict(_workflow)

        _agents = d.pop("agents", UNSET)
        agents: list[BundleResourceItem] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = BundleResourceItem.from_dict(agents_item_data)

                agents.append(agents_item)

        _functions = d.pop("functions", UNSET)
        functions: list[BundleResourceItem] | Unset = UNSET
        if _functions is not UNSET:
            functions = []
            for functions_item_data in _functions:
                functions_item = BundleResourceItem.from_dict(functions_item_data)

                functions.append(functions_item)

        _mcp_servers = d.pop("mcp_servers", UNSET)
        mcp_servers: list[BundleResourceItem] | Unset = UNSET
        if _mcp_servers is not UNSET:
            mcp_servers = []
            for mcp_servers_item_data in _mcp_servers:
                mcp_servers_item = BundleResourceItem.from_dict(mcp_servers_item_data)

                mcp_servers.append(mcp_servers_item)

        workflow_bundle_save = cls(
            workflow=workflow,
            agents=agents,
            functions=functions,
            mcp_servers=mcp_servers,
        )

        return workflow_bundle_save
