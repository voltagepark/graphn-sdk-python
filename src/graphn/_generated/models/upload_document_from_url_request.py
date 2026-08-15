from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_document_from_url_request_metadata import (
        UploadDocumentFromURLRequestMetadata,
    )


T = TypeVar("T", bound="UploadDocumentFromURLRequest")


@_attrs_define
class UploadDocumentFromURLRequest:
    """
    Attributes:
        url (str):
        filename (str | Unset):
        content_type (str | Unset):
        segment_seconds (int | Unset):
        metadata (UploadDocumentFromURLRequestMetadata | Unset):
    """

    url: str
    filename: str | Unset = UNSET
    content_type: str | Unset = UNSET
    segment_seconds: int | Unset = UNSET
    metadata: UploadDocumentFromURLRequestMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        filename = self.filename

        content_type = self.content_type

        segment_seconds = self.segment_seconds

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if segment_seconds is not UNSET:
            field_dict["segment_seconds"] = segment_seconds
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.upload_document_from_url_request_metadata import (
            UploadDocumentFromURLRequestMetadata,
        )

        d = dict(src_dict)
        url = d.pop("url")

        filename = d.pop("filename", UNSET)

        content_type = d.pop("content_type", UNSET)

        segment_seconds = d.pop("segment_seconds", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UploadDocumentFromURLRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UploadDocumentFromURLRequestMetadata.from_dict(_metadata)

        upload_document_from_url_request = cls(
            url=url,
            filename=filename,
            content_type=content_type,
            segment_seconds=segment_seconds,
            metadata=metadata,
        )

        return upload_document_from_url_request
