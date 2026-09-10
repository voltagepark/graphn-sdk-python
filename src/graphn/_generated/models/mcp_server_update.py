from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server_spec import McpServerSpec
    from ..models.mcp_server_update_files import McpServerUpdateFiles
    from ..models.mcp_server_update_secrets import McpServerUpdateSecrets


T = TypeVar("T", bound="McpServerUpdate")


@_attrs_define
class McpServerUpdate:
    """
    Attributes:
        name (str | Unset):
        files (McpServerUpdateFiles | Unset):
        endpoint_url (str | Unset):
        workflow_id (str | Unset):
        secrets (McpServerUpdateSecrets | Unset):
        spec (McpServerSpec | Unset):
    """

    name: str | Unset = UNSET
    files: McpServerUpdateFiles | Unset = UNSET
    endpoint_url: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    secrets: McpServerUpdateSecrets | Unset = UNSET
    spec: McpServerSpec | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.mcp_server_spec import McpServerSpec
        from ..models.mcp_server_update_files import (
            McpServerUpdateFiles,
        )
        from ..models.mcp_server_update_secrets import (
            McpServerUpdateSecrets,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _files = d.pop("files", UNSET)
        files: McpServerUpdateFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = McpServerUpdateFiles.from_dict(_files)

        endpoint_url = d.pop("endpoint_url", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: McpServerUpdateSecrets | Unset
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = McpServerUpdateSecrets.from_dict(_secrets)

        _spec = d.pop("spec", UNSET)
        spec: McpServerSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = McpServerSpec.from_dict(_spec)

        mcp_server_update = cls(
            name=name,
            files=files,
            endpoint_url=endpoint_url,
            workflow_id=workflow_id,
            secrets=secrets,
            spec=spec,
        )

        return mcp_server_update
