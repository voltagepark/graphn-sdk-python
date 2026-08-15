from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_request_metadata_filter import SearchRequestMetadataFilter


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        query (str):
        top_k (int | Unset):
        rerank (bool | Unset):
        reranker_model (str | Unset):
        score_threshold (float | Unset):
        metadata_filter (SearchRequestMetadataFilter | Unset):
    """

    query: str
    top_k: int | Unset = UNSET
    rerank: bool | Unset = UNSET
    reranker_model: str | Unset = UNSET
    score_threshold: float | Unset = UNSET
    metadata_filter: SearchRequestMetadataFilter | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        top_k = self.top_k

        rerank = self.rerank

        reranker_model = self.reranker_model

        score_threshold = self.score_threshold

        metadata_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_filter, Unset):
            metadata_filter = self.metadata_filter.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "query": query,
            }
        )
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if rerank is not UNSET:
            field_dict["rerank"] = rerank
        if reranker_model is not UNSET:
            field_dict["reranker_model"] = reranker_model
        if score_threshold is not UNSET:
            field_dict["score_threshold"] = score_threshold
        if metadata_filter is not UNSET:
            field_dict["metadata_filter"] = metadata_filter

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_request_metadata_filter import SearchRequestMetadataFilter

        d = dict(src_dict)
        query = d.pop("query")

        top_k = d.pop("top_k", UNSET)

        rerank = d.pop("rerank", UNSET)

        reranker_model = d.pop("reranker_model", UNSET)

        score_threshold = d.pop("score_threshold", UNSET)

        _metadata_filter = d.pop("metadata_filter", UNSET)
        metadata_filter: SearchRequestMetadataFilter | Unset
        if isinstance(_metadata_filter, Unset):
            metadata_filter = UNSET
        else:
            metadata_filter = SearchRequestMetadataFilter.from_dict(_metadata_filter)

        search_request = cls(
            query=query,
            top_k=top_k,
            rerank=rerank,
            reranker_model=reranker_model,
            score_threshold=score_threshold,
            metadata_filter=metadata_filter,
        )

        return search_request
