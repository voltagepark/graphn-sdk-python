from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbedRequest")


@_attrs_define
class EmbedRequest:
    """
    Attributes:
        texts (list[str]):
        normalize (bool | Unset):
        model (str | Unset):
    """

    texts: list[str]
    normalize: bool | Unset = UNSET
    model: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        texts = self.texts

        normalize = self.normalize

        model = self.model

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "texts": texts,
            }
        )
        if normalize is not UNSET:
            field_dict["normalize"] = normalize
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        texts = cast(list[str], d.pop("texts"))

        normalize = d.pop("normalize", UNSET)

        model = d.pop("model", UNSET)

        embed_request = cls(
            texts=texts,
            normalize=normalize,
            model=model,
        )

        return embed_request
