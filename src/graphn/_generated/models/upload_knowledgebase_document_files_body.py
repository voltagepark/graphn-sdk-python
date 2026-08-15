from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="UploadKnowledgebaseDocumentFilesBody")


@_attrs_define
class UploadKnowledgebaseDocumentFilesBody:
    """
    Attributes:
        file (File):
        metadata (str | Unset): Optional JSON object serialized as a string.
    """

    file: File
    metadata: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file": file,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.metadata, Unset):
            files.append(
                ("metadata", (None, str(self.metadata).encode(), "text/plain"))
            )

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        metadata = d.pop("metadata", UNSET)

        upload_knowledgebase_document_files_body = cls(
            file=file,
            metadata=metadata,
        )

        return upload_knowledgebase_document_files_body
