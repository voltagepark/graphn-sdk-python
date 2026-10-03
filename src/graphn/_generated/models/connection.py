from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.connection_kind import ConnectionKind
from ..models.connection_status import ConnectionStatus
from ..models.connection_watch_status import ConnectionWatchStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_account_metadata import ConnectionAccountMetadata


T = TypeVar("T", bound="Connection")


@_attrs_define
class Connection:
    """Workspace-owned authorization metadata. OAuth client secrets, access
    tokens, refresh tokens, PKCE data, and account hashes are never returned.

        Attributes:
            id (str):
            workspace_id (str):
            name (str):
            kind (ConnectionKind):
            provider_id (str):
            status (ConnectionStatus):
            granted_capabilities (list[str]):
            granted_scopes (list[str]):
            watch_status (ConnectionWatchStatus):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            resource_id (str | Unset):
            account_label (str | Unset):
            account_metadata (ConnectionAccountMetadata | Unset):
            credential_expires_at (datetime.datetime | Unset):
            last_validated_at (datetime.datetime | Unset):
            last_error_code (str | Unset):
            last_error_message (str | Unset):
            watch_expires_at (datetime.datetime | Unset):
            last_event_at (datetime.datetime | Unset):
    """

    id: str
    workspace_id: str
    name: str
    kind: ConnectionKind
    provider_id: str
    status: ConnectionStatus
    granted_capabilities: list[str]
    granted_scopes: list[str]
    watch_status: ConnectionWatchStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    resource_id: str | Unset = UNSET
    account_label: str | Unset = UNSET
    account_metadata: ConnectionAccountMetadata | Unset = UNSET
    credential_expires_at: datetime.datetime | Unset = UNSET
    last_validated_at: datetime.datetime | Unset = UNSET
    last_error_code: str | Unset = UNSET
    last_error_message: str | Unset = UNSET
    watch_expires_at: datetime.datetime | Unset = UNSET
    last_event_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        name = self.name

        kind = self.kind.value

        provider_id = self.provider_id

        status = self.status.value

        granted_capabilities = self.granted_capabilities

        granted_scopes = self.granted_scopes

        watch_status = self.watch_status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        resource_id = self.resource_id

        account_label = self.account_label

        account_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_metadata, Unset):
            account_metadata = self.account_metadata.to_dict()

        credential_expires_at: str | Unset = UNSET
        if not isinstance(self.credential_expires_at, Unset):
            credential_expires_at = self.credential_expires_at.isoformat()

        last_validated_at: str | Unset = UNSET
        if not isinstance(self.last_validated_at, Unset):
            last_validated_at = self.last_validated_at.isoformat()

        last_error_code = self.last_error_code

        last_error_message = self.last_error_message

        watch_expires_at: str | Unset = UNSET
        if not isinstance(self.watch_expires_at, Unset):
            watch_expires_at = self.watch_expires_at.isoformat()

        last_event_at: str | Unset = UNSET
        if not isinstance(self.last_event_at, Unset):
            last_event_at = self.last_event_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "name": name,
                "kind": kind,
                "provider_id": provider_id,
                "status": status,
                "granted_capabilities": granted_capabilities,
                "granted_scopes": granted_scopes,
                "watch_status": watch_status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if account_label is not UNSET:
            field_dict["account_label"] = account_label
        if account_metadata is not UNSET:
            field_dict["account_metadata"] = account_metadata
        if credential_expires_at is not UNSET:
            field_dict["credential_expires_at"] = credential_expires_at
        if last_validated_at is not UNSET:
            field_dict["last_validated_at"] = last_validated_at
        if last_error_code is not UNSET:
            field_dict["last_error_code"] = last_error_code
        if last_error_message is not UNSET:
            field_dict["last_error_message"] = last_error_message
        if watch_expires_at is not UNSET:
            field_dict["watch_expires_at"] = watch_expires_at
        if last_event_at is not UNSET:
            field_dict["last_event_at"] = last_event_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.connection_account_metadata import (
            ConnectionAccountMetadata,
        )

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        name = d.pop("name")

        kind = ConnectionKind(d.pop("kind"))

        provider_id = d.pop("provider_id")

        status = ConnectionStatus(d.pop("status"))

        granted_capabilities = cast(list[str], d.pop("granted_capabilities"))

        granted_scopes = cast(list[str], d.pop("granted_scopes"))

        watch_status = ConnectionWatchStatus(d.pop("watch_status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        resource_id = d.pop("resource_id", UNSET)

        account_label = d.pop("account_label", UNSET)

        _account_metadata = d.pop("account_metadata", UNSET)
        account_metadata: ConnectionAccountMetadata | Unset
        if isinstance(_account_metadata, Unset):
            account_metadata = UNSET
        else:
            account_metadata = ConnectionAccountMetadata.from_dict(_account_metadata)

        _credential_expires_at = d.pop("credential_expires_at", UNSET)
        credential_expires_at: datetime.datetime | Unset
        if isinstance(_credential_expires_at, Unset):
            credential_expires_at = UNSET
        else:
            credential_expires_at = datetime.datetime.fromisoformat(
                _credential_expires_at
            )

        _last_validated_at = d.pop("last_validated_at", UNSET)
        last_validated_at: datetime.datetime | Unset
        if isinstance(_last_validated_at, Unset):
            last_validated_at = UNSET
        else:
            last_validated_at = datetime.datetime.fromisoformat(_last_validated_at)

        last_error_code = d.pop("last_error_code", UNSET)

        last_error_message = d.pop("last_error_message", UNSET)

        _watch_expires_at = d.pop("watch_expires_at", UNSET)
        watch_expires_at: datetime.datetime | Unset
        if isinstance(_watch_expires_at, Unset):
            watch_expires_at = UNSET
        else:
            watch_expires_at = datetime.datetime.fromisoformat(_watch_expires_at)

        _last_event_at = d.pop("last_event_at", UNSET)
        last_event_at: datetime.datetime | Unset
        if isinstance(_last_event_at, Unset):
            last_event_at = UNSET
        else:
            last_event_at = datetime.datetime.fromisoformat(_last_event_at)

        connection = cls(
            id=id,
            workspace_id=workspace_id,
            name=name,
            kind=kind,
            provider_id=provider_id,
            status=status,
            granted_capabilities=granted_capabilities,
            granted_scopes=granted_scopes,
            watch_status=watch_status,
            created_at=created_at,
            updated_at=updated_at,
            resource_id=resource_id,
            account_label=account_label,
            account_metadata=account_metadata,
            credential_expires_at=credential_expires_at,
            last_validated_at=last_validated_at,
            last_error_code=last_error_code,
            last_error_message=last_error_message,
            watch_expires_at=watch_expires_at,
            last_event_at=last_event_at,
        )

        return connection
