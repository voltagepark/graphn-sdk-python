from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_result_metadata import SearchResultMetadata


T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """
    Attributes:
        id (str):
        text (str):
        score (float):
        document_id (str):
        source (str):
        document_type (str | Unset):
        image_url (str | Unset):
        video_url (str | Unset):
        segment_start_sec (float | Unset):
        segment_end_sec (float | Unset):
        metadata (SearchResultMetadata | Unset):
    """

    id: str
    text: str
    score: float
    document_id: str
    source: str
    document_type: str | Unset = UNSET
    image_url: str | Unset = UNSET
    video_url: str | Unset = UNSET
    segment_start_sec: float | Unset = UNSET
    segment_end_sec: float | Unset = UNSET
    metadata: SearchResultMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        score = self.score

        document_id = self.document_id

        source = self.source

        document_type = self.document_type

        image_url = self.image_url

        video_url = self.video_url

        segment_start_sec = self.segment_start_sec

        segment_end_sec = self.segment_end_sec

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "score": score,
                "document_id": document_id,
                "source": source,
            }
        )
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if segment_start_sec is not UNSET:
            field_dict["segment_start_sec"] = segment_start_sec
        if segment_end_sec is not UNSET:
            field_dict["segment_end_sec"] = segment_end_sec
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_result_metadata import SearchResultMetadata

        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        score = d.pop("score")

        document_id = d.pop("document_id")

        source = d.pop("source")

        document_type = d.pop("document_type", UNSET)

        image_url = d.pop("image_url", UNSET)

        video_url = d.pop("video_url", UNSET)

        segment_start_sec = d.pop("segment_start_sec", UNSET)

        segment_end_sec = d.pop("segment_end_sec", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SearchResultMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SearchResultMetadata.from_dict(_metadata)

        search_result = cls(
            id=id,
            text=text,
            score=score,
            document_id=document_id,
            source=source,
            document_type=document_type,
            image_url=image_url,
            video_url=video_url,
            segment_start_sec=segment_start_sec,
            segment_end_sec=segment_end_sec,
            metadata=metadata,
        )

        search_result.additional_properties = d
        return search_result

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
