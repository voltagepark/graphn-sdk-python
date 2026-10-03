from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_submit_request_input import AsyncSubmitRequestInput
    from ..models.async_submit_request_metadata import AsyncSubmitRequestMetadata
    from ..models.async_submit_request_parameters import AsyncSubmitRequestParameters


T = TypeVar("T", bound="AsyncSubmitRequest")


@_attrs_define
class AsyncSubmitRequest:
    """
    Attributes:
        input_ (AsyncSubmitRequestInput):
        parameters (AsyncSubmitRequestParameters | Unset):
        metadata (AsyncSubmitRequestMetadata | Unset):
    """

    input_: AsyncSubmitRequestInput
    parameters: AsyncSubmitRequestParameters | Unset = UNSET
    metadata: AsyncSubmitRequestMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_.to_dict()

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.async_submit_request_input import (
            AsyncSubmitRequestInput,
        )
        from ..models.async_submit_request_metadata import (
            AsyncSubmitRequestMetadata,
        )
        from ..models.async_submit_request_parameters import (
            AsyncSubmitRequestParameters,
        )

        d = dict(src_dict)
        input_ = AsyncSubmitRequestInput.from_dict(d.pop("input"))

        _parameters = d.pop("parameters", UNSET)
        parameters: AsyncSubmitRequestParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = AsyncSubmitRequestParameters.from_dict(_parameters)

        _metadata = d.pop("metadata", UNSET)
        metadata: AsyncSubmitRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AsyncSubmitRequestMetadata.from_dict(_metadata)

        async_submit_request = cls(
            input_=input_,
            parameters=parameters,
            metadata=metadata,
        )

        async_submit_request.additional_properties = d
        return async_submit_request

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
