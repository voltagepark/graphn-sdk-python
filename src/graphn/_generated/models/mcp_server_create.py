from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server_create_files import McpServerCreateFiles
    from ..models.mcp_server_create_secrets import McpServerCreateSecrets
    from ..models.mcp_server_spec import McpServerSpec


T = TypeVar("T", bound="McpServerCreate")


@_attrs_define
class McpServerCreate:
    """
    Attributes:
        name (str):
        type_ (str | Unset):
        files (McpServerCreateFiles | Unset):
        endpoint_url (str | Unset):
        workflow_id (str | Unset):
        secrets (McpServerCreateSecrets | Unset):
        spec (McpServerSpec | Unset):
    """

    name: str
    type_: str | Unset = UNSET
    files: McpServerCreateFiles | Unset = UNSET
    endpoint_url: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    secrets: McpServerCreateSecrets | Unset = UNSET
    spec: McpServerSpec | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        endpoint_url = self.endpoint_url

        workflow_id = self.workflow_id

        secrets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if files is not UNSET:
            field_dict["files"] = files
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_server_create_files import McpServerCreateFiles
        from ..models.mcp_server_create_secrets import McpServerCreateSecrets
        from ..models.mcp_server_spec import McpServerSpec

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type", UNSET)

        _files = d.pop("files", UNSET)
        files: McpServerCreateFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = McpServerCreateFiles.from_dict(_files)

        endpoint_url = d.pop("endpoint_url", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: McpServerCreateSecrets | Unset
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = McpServerCreateSecrets.from_dict(_secrets)

        _spec = d.pop("spec", UNSET)
        spec: McpServerSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = McpServerSpec.from_dict(_spec)

        mcp_server_create = cls(
            name=name,
            type_=type_,
            files=files,
            endpoint_url=endpoint_url,
            workflow_id=workflow_id,
            secrets=secrets,
            spec=spec,
        )

        return mcp_server_create
