from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kb_document_metadata import KbDocumentMetadata


T = TypeVar("T", bound="KbDocument")


@_attrs_define
class KbDocument:
    """
    Attributes:
        id (str):
        kb_id (str):
        filename (str):
        content_type (str):
        chunk_count (int):
        created_at (datetime.datetime):
        document_type (str | Unset):
        image_url (str | Unset):
        video_url (str | Unset):
        expires_at (datetime.datetime | Unset):
        expires_in (int | Unset):
        media_href (str | Unset):
        segment_seconds (int | Unset):
        metadata (KbDocumentMetadata | Unset):
    """

    id: str
    kb_id: str
    filename: str
    content_type: str
    chunk_count: int
    created_at: datetime.datetime
    document_type: str | Unset = UNSET
    image_url: str | Unset = UNSET
    video_url: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    expires_in: int | Unset = UNSET
    media_href: str | Unset = UNSET
    segment_seconds: int | Unset = UNSET
    metadata: KbDocumentMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kb_id = self.kb_id

        filename = self.filename

        content_type = self.content_type

        chunk_count = self.chunk_count

        created_at = self.created_at.isoformat()

        document_type = self.document_type

        image_url = self.image_url

        video_url = self.video_url

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        expires_in = self.expires_in

        media_href = self.media_href

        segment_seconds = self.segment_seconds

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kb_id": kb_id,
                "filename": filename,
                "content_type": content_type,
                "chunk_count": chunk_count,
                "created_at": created_at,
            }
        )
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if media_href is not UNSET:
            field_dict["media_href"] = media_href
        if segment_seconds is not UNSET:
            field_dict["segment_seconds"] = segment_seconds
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kb_document_metadata import KbDocumentMetadata

        d = dict(src_dict)
        id = d.pop("id")

        kb_id = d.pop("kb_id")

        filename = d.pop("filename")

        content_type = d.pop("content_type")

        chunk_count = d.pop("chunk_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        document_type = d.pop("document_type", UNSET)

        image_url = d.pop("image_url", UNSET)

        video_url = d.pop("video_url", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        expires_in = d.pop("expires_in", UNSET)

        media_href = d.pop("media_href", UNSET)

        segment_seconds = d.pop("segment_seconds", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: KbDocumentMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = KbDocumentMetadata.from_dict(_metadata)

        kb_document = cls(
            id=id,
            kb_id=kb_id,
            filename=filename,
            content_type=content_type,
            chunk_count=chunk_count,
            created_at=created_at,
            document_type=document_type,
            image_url=image_url,
            video_url=video_url,
            expires_at=expires_at,
            expires_in=expires_in,
            media_href=media_href,
            segment_seconds=segment_seconds,
            metadata=metadata,
        )

        kb_document.additional_properties = d
        return kb_document

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
