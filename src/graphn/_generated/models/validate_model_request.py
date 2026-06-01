from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.validate_model_request_quantization import (
    ValidateModelRequestQuantization,
)
from ..models.validate_model_request_weight_source import (
    ValidateModelRequestWeightSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateModelRequest")


@_attrs_define
class ValidateModelRequest:
    """
    Attributes:
        huggingface_model_id (str): Required when `weight_source` is `huggingface`. Carried
            through on the `s3_assume_role` path as the canonical
            model identifier (used for naming + LoRA classification
            hints), but architecture detection comes from `config.json`
            in the customer's bucket, not the HF Hub.
        weight_source (ValidateModelRequestWeightSource | Unset): Which validation path to run. `huggingface` (default)
            queries
            the HuggingFace Hub API. `s3_assume_role` chains the same
            two-hop AssumeRole the smart-loader uses (bootstrap user
            → platform role → customer role with ExternalId) and
            probes `<s3_url>config.json` directly, so an unsupported
            architecture surfaces before AF provisions a download Job.
            `s3_presigned` is intentionally not accepted: presigned
            URLs deliver a single archive object and architecture
            detection requires the full extract.
             Default: ValidateModelRequestWeightSource.HUGGINGFACE.
        s3_url (None | str | Unset): S3 prefix (must end with `/`). Required when
            `weight_source` is `s3_assume_role`. Points at the
            directory containing `config.json` + safetensors in
            HuggingFace layout; the smart-loader uses `aws s3 sync`
            on this path so a single archive object is rejected at
            the API boundary.
        s3_role_arn (None | str | Unset): Customer IAM role ARN. Required when `weight_source` is
            `s3_assume_role`. Role name must start with `graphn-byom-`
            (the platform IAM is scoped to that prefix as
            defense-in-depth).
        s3_external_id (None | str | Unset): ExternalId from the customer's IAM trust policy. Required
            when `weight_source` is `s3_assume_role`.
        hf_token_secret_id (None | str | Unset): ID of a workspace secret holding a HuggingFace token.
        quantization (ValidateModelRequestQuantization | Unset):
        gpu_memory_utilization (float | Unset):  Default: 0.9.
        model_size_gb (int | None | Unset): Optional caller-supplied estimate of the on-disk weights size,
            in GiB. When provided, the platform sizes the model-weights PVC
            from this hint instead of waiting for a HuggingFace head-bytes
            probe; useful for very large models where the probe would
            otherwise stall the validate response.
        base_model_id (None | str | Unset): LoRA base override / hint, mirroring
            `CustomModelCreate.base_model_id`. When the validator
            detects a LoRA adapter and this field is set, the
            override **wins** over
            `adapter_config.json::base_model_name_or_path` -- so the
            allowlist check and the base-model sizing probe both run
            against the override. Useful for adapters whose adapter
            config records a local filesystem path
            (e.g. `C:/users/.../base`) that isn't a valid HF id.
            Silently ignored when the validator resolves the repo as
            a full model (`artifact_type=base`).
    """

    huggingface_model_id: str
    weight_source: ValidateModelRequestWeightSource | Unset = (
        ValidateModelRequestWeightSource.HUGGINGFACE
    )
    s3_url: None | str | Unset = UNSET
    s3_role_arn: None | str | Unset = UNSET
    s3_external_id: None | str | Unset = UNSET
    hf_token_secret_id: None | str | Unset = UNSET
    quantization: ValidateModelRequestQuantization | Unset = UNSET
    gpu_memory_utilization: float | Unset = 0.9
    model_size_gb: int | None | Unset = UNSET
    base_model_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        huggingface_model_id = self.huggingface_model_id

        weight_source: str | Unset = UNSET
        if not isinstance(self.weight_source, Unset):
            weight_source = self.weight_source.value

        s3_url: None | str | Unset
        if isinstance(self.s3_url, Unset):
            s3_url = UNSET
        else:
            s3_url = self.s3_url

        s3_role_arn: None | str | Unset
        if isinstance(self.s3_role_arn, Unset):
            s3_role_arn = UNSET
        else:
            s3_role_arn = self.s3_role_arn

        s3_external_id: None | str | Unset
        if isinstance(self.s3_external_id, Unset):
            s3_external_id = UNSET
        else:
            s3_external_id = self.s3_external_id

        hf_token_secret_id: None | str | Unset
        if isinstance(self.hf_token_secret_id, Unset):
            hf_token_secret_id = UNSET
        else:
            hf_token_secret_id = self.hf_token_secret_id

        quantization: str | Unset = UNSET
        if not isinstance(self.quantization, Unset):
            quantization = self.quantization.value

        gpu_memory_utilization = self.gpu_memory_utilization

        model_size_gb: int | None | Unset
        if isinstance(self.model_size_gb, Unset):
            model_size_gb = UNSET
        else:
            model_size_gb = self.model_size_gb

        base_model_id: None | str | Unset
        if isinstance(self.base_model_id, Unset):
            base_model_id = UNSET
        else:
            base_model_id = self.base_model_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "huggingface_model_id": huggingface_model_id,
            }
        )
        if weight_source is not UNSET:
            field_dict["weight_source"] = weight_source
        if s3_url is not UNSET:
            field_dict["s3_url"] = s3_url
        if s3_role_arn is not UNSET:
            field_dict["s3_role_arn"] = s3_role_arn
        if s3_external_id is not UNSET:
            field_dict["s3_external_id"] = s3_external_id
        if hf_token_secret_id is not UNSET:
            field_dict["hf_token_secret_id"] = hf_token_secret_id
        if quantization is not UNSET:
            field_dict["quantization"] = quantization
        if gpu_memory_utilization is not UNSET:
            field_dict["gpu_memory_utilization"] = gpu_memory_utilization
        if model_size_gb is not UNSET:
            field_dict["model_size_gb"] = model_size_gb
        if base_model_id is not UNSET:
            field_dict["base_model_id"] = base_model_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        huggingface_model_id = d.pop("huggingface_model_id")

        _weight_source = d.pop("weight_source", UNSET)
        weight_source: ValidateModelRequestWeightSource | Unset
        if isinstance(_weight_source, Unset):
            weight_source = UNSET
        else:
            weight_source = ValidateModelRequestWeightSource(_weight_source)

        def _parse_s3_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3_url = _parse_s3_url(d.pop("s3_url", UNSET))

        def _parse_s3_role_arn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3_role_arn = _parse_s3_role_arn(d.pop("s3_role_arn", UNSET))

        def _parse_s3_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3_external_id = _parse_s3_external_id(d.pop("s3_external_id", UNSET))

        def _parse_hf_token_secret_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hf_token_secret_id = _parse_hf_token_secret_id(
            d.pop("hf_token_secret_id", UNSET)
        )

        _quantization = d.pop("quantization", UNSET)
        quantization: ValidateModelRequestQuantization | Unset
        if isinstance(_quantization, Unset):
            quantization = UNSET
        else:
            quantization = ValidateModelRequestQuantization(_quantization)

        gpu_memory_utilization = d.pop("gpu_memory_utilization", UNSET)

        def _parse_model_size_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        model_size_gb = _parse_model_size_gb(d.pop("model_size_gb", UNSET))

        def _parse_base_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_model_id = _parse_base_model_id(d.pop("base_model_id", UNSET))

        validate_model_request = cls(
            huggingface_model_id=huggingface_model_id,
            weight_source=weight_source,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            s3_external_id=s3_external_id,
            hf_token_secret_id=hf_token_secret_id,
            quantization=quantization,
            gpu_memory_utilization=gpu_memory_utilization,
            model_size_gb=model_size_gb,
            base_model_id=base_model_id,
        )

        return validate_model_request
