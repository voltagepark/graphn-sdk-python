from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from .. import types
from ..types import File

T = TypeVar("T", bound="UploadStorageFileBody")


@_attrs_define
class UploadStorageFileBody:
    """
    Attributes:
        file (File):
    """

    file: File

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        upload_storage_file_body = cls(
            file=file,
        )

        return upload_storage_file_body
