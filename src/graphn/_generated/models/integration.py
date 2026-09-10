from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.integration_auth_mode import IntegrationAuthMode
from ..models.integration_kind import IntegrationKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.integration_capability import IntegrationCapability
    from ..models.integration_event import IntegrationEvent


T = TypeVar("T", bound="Integration")


@_attrs_define
class Integration:
    """
    Attributes:
        id (str):
        display_name (str):
        kind (IntegrationKind):
        auth_mode (IntegrationAuthMode):
        capabilities (list[IntegrationCapability]):
        events (list[IntegrationEvent]):
        description (str | Unset):
    """

    id: str
    display_name: str
    kind: IntegrationKind
    auth_mode: IntegrationAuthMode
    capabilities: list[IntegrationCapability]
    events: list[IntegrationEvent]
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        kind = self.kind.value

        auth_mode = self.auth_mode.value

        capabilities = []
        for capabilities_item_data in self.capabilities:
            capabilities_item = capabilities_item_data.to_dict()
            capabilities.append(capabilities_item)

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "kind": kind,
                "auth_mode": auth_mode,
                "capabilities": capabilities,
                "events": events,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.integration_capability import (
            IntegrationCapability,
        )
        from ..models.integration_event import IntegrationEvent

        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        kind = IntegrationKind(d.pop("kind"))

        auth_mode = IntegrationAuthMode(d.pop("auth_mode"))

        capabilities = []
        _capabilities = d.pop("capabilities")
        for capabilities_item_data in _capabilities:
            capabilities_item = IntegrationCapability.from_dict(capabilities_item_data)

            capabilities.append(capabilities_item)

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = IntegrationEvent.from_dict(events_item_data)

            events.append(events_item)

        description = d.pop("description", UNSET)

        integration = cls(
            id=id,
            display_name=display_name,
            kind=kind,
            auth_mode=auth_mode,
            capabilities=capabilities,
            events=events,
            description=description,
        )

        return integration
