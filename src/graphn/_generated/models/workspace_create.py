from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="WorkspaceCreate")


@_attrs_define
class WorkspaceCreate:
    """
    Attributes:
        name (str):
    """

    name: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        workspace_create = cls(
            name=name,
        )

        return workspace_create
