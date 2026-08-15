from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="EmbedResponse")


@_attrs_define
class EmbedResponse:
    """
    Attributes:
        embeddings (list[list[float]]):
        dimensions (int):
        count (int):
    """

    embeddings: list[list[float]]
    dimensions: int
    count: int

    def to_dict(self) -> dict[str, Any]:
        embeddings = []
        for embeddings_item_data in self.embeddings:
            embeddings_item = embeddings_item_data

            embeddings.append(embeddings_item)

        dimensions = self.dimensions

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "embeddings": embeddings,
                "dimensions": dimensions,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        embeddings = []
        _embeddings = d.pop("embeddings")
        for embeddings_item_data in _embeddings:
            embeddings_item = cast(list[float], embeddings_item_data)

            embeddings.append(embeddings_item)

        dimensions = d.pop("dimensions")

        count = d.pop("count")

        embed_response = cls(
            embeddings=embeddings,
            dimensions=dimensions,
            count=count,
        )

        return embed_response
