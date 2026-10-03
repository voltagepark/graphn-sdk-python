from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.inference_router_scope import InferenceRouterScope
from ..models.inference_router_status import InferenceRouterStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inference_router_revision import InferenceRouterRevision


T = TypeVar("T", bound="InferenceRouter")


@_attrs_define
class InferenceRouter:
    """
    Attributes:
        id (str): `ir_...` for workspace routers; `auto` for the immutable platform adapter.
        name (str):
        display_name (str):
        scope (InferenceRouterScope):
        status (InferenceRouterStatus):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        workspace_id (str | Unset):
        owner_id (str | Unset):
        draft_revision (InferenceRouterRevision | None | Unset):
        pending_revision (InferenceRouterRevision | None | Unset):
        active_revision (InferenceRouterRevision | None | Unset):
    """

    id: str
    name: str
    display_name: str
    scope: InferenceRouterScope
    status: InferenceRouterStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    workspace_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    draft_revision: InferenceRouterRevision | None | Unset = UNSET
    pending_revision: InferenceRouterRevision | None | Unset = UNSET
    active_revision: InferenceRouterRevision | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inference_router_revision import (
            InferenceRouterRevision,
        )

        id = self.id

        name = self.name

        display_name = self.display_name

        scope = self.scope.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        workspace_id = self.workspace_id

        owner_id = self.owner_id

        draft_revision: dict[str, Any] | None | Unset
        if isinstance(self.draft_revision, Unset):
            draft_revision = UNSET
        elif isinstance(self.draft_revision, InferenceRouterRevision):
            draft_revision = self.draft_revision.to_dict()
        else:
            draft_revision = self.draft_revision

        pending_revision: dict[str, Any] | None | Unset
        if isinstance(self.pending_revision, Unset):
            pending_revision = UNSET
        elif isinstance(self.pending_revision, InferenceRouterRevision):
            pending_revision = self.pending_revision.to_dict()
        else:
            pending_revision = self.pending_revision

        active_revision: dict[str, Any] | None | Unset
        if isinstance(self.active_revision, Unset):
            active_revision = UNSET
        elif isinstance(self.active_revision, InferenceRouterRevision):
            active_revision = self.active_revision.to_dict()
        else:
            active_revision = self.active_revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "scope": scope,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if draft_revision is not UNSET:
            field_dict["draft_revision"] = draft_revision
        if pending_revision is not UNSET:
            field_dict["pending_revision"] = pending_revision
        if active_revision is not UNSET:
            field_dict["active_revision"] = active_revision

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_revision import (
            InferenceRouterRevision,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("display_name")

        scope = InferenceRouterScope(d.pop("scope"))

        status = InferenceRouterStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        workspace_id = d.pop("workspace_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        def _parse_draft_revision(
            data: object,
        ) -> InferenceRouterRevision | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                draft_revision_type_1 = InferenceRouterRevision.from_dict(data)

                return draft_revision_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InferenceRouterRevision | None | Unset, data)

        draft_revision = _parse_draft_revision(d.pop("draft_revision", UNSET))

        def _parse_pending_revision(
            data: object,
        ) -> InferenceRouterRevision | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pending_revision_type_1 = InferenceRouterRevision.from_dict(data)

                return pending_revision_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InferenceRouterRevision | None | Unset, data)

        pending_revision = _parse_pending_revision(d.pop("pending_revision", UNSET))

        def _parse_active_revision(
            data: object,
        ) -> InferenceRouterRevision | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                active_revision_type_1 = InferenceRouterRevision.from_dict(data)

                return active_revision_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InferenceRouterRevision | None | Unset, data)

        active_revision = _parse_active_revision(d.pop("active_revision", UNSET))

        inference_router = cls(
            id=id,
            name=name,
            display_name=display_name,
            scope=scope,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            workspace_id=workspace_id,
            owner_id=owner_id,
            draft_revision=draft_revision,
            pending_revision=pending_revision,
            active_revision=active_revision,
        )

        inference_router.additional_properties = d
        return inference_router

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
