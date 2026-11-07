from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.agent_computer_coordinate_space import AgentComputerCoordinateSpace
from ..models.agent_computer_scope import AgentComputerScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_computer_display import AgentComputerDisplay


T = TypeVar("T", bound="AgentComputer")


@_attrs_define
class AgentComputer:
    """Computer-use capability. When enabled the agent step runs on a sandboxed desktop with Chromium (one Lambda MicroVM
    per sandbox) and acts from screenshots; the agent's model must accept image input.

        Attributes:
            enabled (bool | Unset):
            scope (AgentComputerScope | Unset): step (default): one sandbox per agent step; execution: shared across the
                workflow execution
            max_actions (int | Unset): cap on actions per step, 1-500; 0 or omitted means the default of 50
            display (AgentComputerDisplay | Unset):
            coordinate_space (AgentComputerCoordinateSpace | Unset): Grid the grounding model answers in; default
                relative_1000 (Qwen 0..1000 grid, what qwen3-vl emits)
            planner_model (str | Unset): agentic text model that plans and calls tools; empty = the agent's model
            grounding_model (str | Unset): vision model that grounds described targets to screen coordinates; empty =
                platform default
            planner_sees_screenshots (bool | Unset): also attach the latest screenshots to the planner (multimodal planners
                only)
    """

    enabled: bool | Unset = UNSET
    scope: AgentComputerScope | Unset = UNSET
    max_actions: int | Unset = UNSET
    display: AgentComputerDisplay | Unset = UNSET
    coordinate_space: AgentComputerCoordinateSpace | Unset = UNSET
    planner_model: str | Unset = UNSET
    grounding_model: str | Unset = UNSET
    planner_sees_screenshots: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        max_actions = self.max_actions

        display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.to_dict()

        coordinate_space: str | Unset = UNSET
        if not isinstance(self.coordinate_space, Unset):
            coordinate_space = self.coordinate_space.value

        planner_model = self.planner_model

        grounding_model = self.grounding_model

        planner_sees_screenshots = self.planner_sees_screenshots

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if scope is not UNSET:
            field_dict["scope"] = scope
        if max_actions is not UNSET:
            field_dict["max_actions"] = max_actions
        if display is not UNSET:
            field_dict["display"] = display
        if coordinate_space is not UNSET:
            field_dict["coordinate_space"] = coordinate_space
        if planner_model is not UNSET:
            field_dict["planner_model"] = planner_model
        if grounding_model is not UNSET:
            field_dict["grounding_model"] = grounding_model
        if planner_sees_screenshots is not UNSET:
            field_dict["planner_sees_screenshots"] = planner_sees_screenshots

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.agent_computer_display import AgentComputerDisplay

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: AgentComputerScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = AgentComputerScope(_scope)

        max_actions = d.pop("max_actions", UNSET)

        _display = d.pop("display", UNSET)
        display: AgentComputerDisplay | Unset
        if isinstance(_display, Unset):
            display = UNSET
        else:
            display = AgentComputerDisplay.from_dict(_display)

        _coordinate_space = d.pop("coordinate_space", UNSET)
        coordinate_space: AgentComputerCoordinateSpace | Unset
        if isinstance(_coordinate_space, Unset):
            coordinate_space = UNSET
        else:
            coordinate_space = AgentComputerCoordinateSpace(_coordinate_space)

        planner_model = d.pop("planner_model", UNSET)

        grounding_model = d.pop("grounding_model", UNSET)

        planner_sees_screenshots = d.pop("planner_sees_screenshots", UNSET)

        agent_computer = cls(
            enabled=enabled,
            scope=scope,
            max_actions=max_actions,
            display=display,
            coordinate_space=coordinate_space,
            planner_model=planner_model,
            grounding_model=grounding_model,
            planner_sees_screenshots=planner_sees_screenshots,
        )

        return agent_computer
