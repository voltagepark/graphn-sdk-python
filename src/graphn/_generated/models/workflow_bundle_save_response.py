from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow import Workflow
    from ..models.workflow_bundle_save_response_agents_item import (
        WorkflowBundleSaveResponseAgentsItem,
    )
    from ..models.workflow_bundle_save_response_functions_item import (
        WorkflowBundleSaveResponseFunctionsItem,
    )
    from ..models.workflow_bundle_save_response_mcp_servers_item import (
        WorkflowBundleSaveResponseMcpServersItem,
    )
    from ..models.workflow_bundle_save_response_validation import (
        WorkflowBundleSaveResponseValidation,
    )


T = TypeVar("T", bound="WorkflowBundleSaveResponse")


@_attrs_define
class WorkflowBundleSaveResponse:
    """
    Attributes:
        workflow (Workflow | Unset):
        agents (list[WorkflowBundleSaveResponseAgentsItem] | Unset):
        functions (list[WorkflowBundleSaveResponseFunctionsItem] | Unset):
        mcp_servers (list[WorkflowBundleSaveResponseMcpServersItem] | Unset):
        validation (WorkflowBundleSaveResponseValidation | Unset):
    """

    workflow: Workflow | Unset = UNSET
    agents: list[WorkflowBundleSaveResponseAgentsItem] | Unset = UNSET
    functions: list[WorkflowBundleSaveResponseFunctionsItem] | Unset = UNSET
    mcp_servers: list[WorkflowBundleSaveResponseMcpServersItem] | Unset = UNSET
    validation: WorkflowBundleSaveResponseValidation | Unset = UNSET
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

        validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

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
        if validation is not UNSET:
            field_dict["validation"] = validation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow import Workflow
        from ..models.workflow_bundle_save_response_agents_item import (
            WorkflowBundleSaveResponseAgentsItem,
        )
        from ..models.workflow_bundle_save_response_functions_item import (
            WorkflowBundleSaveResponseFunctionsItem,
        )
        from ..models.workflow_bundle_save_response_mcp_servers_item import (
            WorkflowBundleSaveResponseMcpServersItem,
        )
        from ..models.workflow_bundle_save_response_validation import (
            WorkflowBundleSaveResponseValidation,
        )

        d = dict(src_dict)
        _workflow = d.pop("workflow", UNSET)
        workflow: Workflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        _agents = d.pop("agents", UNSET)
        agents: list[WorkflowBundleSaveResponseAgentsItem] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = WorkflowBundleSaveResponseAgentsItem.from_dict(
                    agents_item_data
                )

                agents.append(agents_item)

        _functions = d.pop("functions", UNSET)
        functions: list[WorkflowBundleSaveResponseFunctionsItem] | Unset = UNSET
        if _functions is not UNSET:
            functions = []
            for functions_item_data in _functions:
                functions_item = WorkflowBundleSaveResponseFunctionsItem.from_dict(
                    functions_item_data
                )

                functions.append(functions_item)

        _mcp_servers = d.pop("mcp_servers", UNSET)
        mcp_servers: list[WorkflowBundleSaveResponseMcpServersItem] | Unset = UNSET
        if _mcp_servers is not UNSET:
            mcp_servers = []
            for mcp_servers_item_data in _mcp_servers:
                mcp_servers_item = WorkflowBundleSaveResponseMcpServersItem.from_dict(
                    mcp_servers_item_data
                )

                mcp_servers.append(mcp_servers_item)

        _validation = d.pop("validation", UNSET)
        validation: WorkflowBundleSaveResponseValidation | Unset
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = WorkflowBundleSaveResponseValidation.from_dict(_validation)

        workflow_bundle_save_response = cls(
            workflow=workflow,
            agents=agents,
            functions=functions,
            mcp_servers=mcp_servers,
            validation=validation,
        )

        workflow_bundle_save_response.additional_properties = d
        return workflow_bundle_save_response

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
