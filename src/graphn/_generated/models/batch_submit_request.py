from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_file_ref import BatchFileRef
    from ..models.batch_input_item import BatchInputItem
    from ..models.batch_submit_request_metadata import BatchSubmitRequestMetadata
    from ..models.batch_submit_request_parameters import BatchSubmitRequestParameters


T = TypeVar("T", bound="BatchSubmitRequest")


@_attrs_define
class BatchSubmitRequest:
    """
    Attributes:
        inputs (list[BatchInputItem] | Unset):
        input_file (BatchFileRef | Unset):
        parameters (BatchSubmitRequestParameters | Unset):
        metadata (BatchSubmitRequestMetadata | Unset):
    """

    inputs: list[BatchInputItem] | Unset = UNSET
    input_file: BatchFileRef | Unset = UNSET
    parameters: BatchSubmitRequestParameters | Unset = UNSET
    metadata: BatchSubmitRequestMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)

        input_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_file, Unset):
            input_file = self.input_file.to_dict()

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if input_file is not UNSET:
            field_dict["input_file"] = input_file
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_file_ref import BatchFileRef
        from ..models.batch_input_item import BatchInputItem
        from ..models.batch_submit_request_metadata import (
            BatchSubmitRequestMetadata,
        )
        from ..models.batch_submit_request_parameters import (
            BatchSubmitRequestParameters,
        )

        d = dict(src_dict)
        _inputs = d.pop("inputs", UNSET)
        inputs: list[BatchInputItem] | Unset = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:
                inputs_item = BatchInputItem.from_dict(inputs_item_data)

                inputs.append(inputs_item)

        _input_file = d.pop("input_file", UNSET)
        input_file: BatchFileRef | Unset
        if isinstance(_input_file, Unset):
            input_file = UNSET
        else:
            input_file = BatchFileRef.from_dict(_input_file)

        _parameters = d.pop("parameters", UNSET)
        parameters: BatchSubmitRequestParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = BatchSubmitRequestParameters.from_dict(_parameters)

        _metadata = d.pop("metadata", UNSET)
        metadata: BatchSubmitRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BatchSubmitRequestMetadata.from_dict(_metadata)

        batch_submit_request = cls(
            inputs=inputs,
            input_file=input_file,
            parameters=parameters,
            metadata=metadata,
        )

        return batch_submit_request
