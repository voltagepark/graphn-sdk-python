from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.capability import Capability
from ..models.custom_model_create_quantization import CustomModelCreateQuantization
from ..models.weight_source import WeightSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomModelCreate")


@_attrs_define
class CustomModelCreate:
    """
    Attributes:
        name (str): URL-safe model name; use this when calling `chat.completions`
            once the model is `ready`. Must be unique within the workspace.
        huggingface_model_id (str): Canonical model identifier (`org/model-name`). **Required
            for every `weight_source`**: this is the name the inference
            endpoint advertises and the value clients pass in `model`
            for chat completions, so without it the deployed model has
            no stable name to address via inference. For `huggingface`
            it also drives the download; for the S3 sources it mirrors
            the "Model ID" field in the web UI's S3 import flow.
             Example: meta-llama/Llama-3-8B-Instruct.
        display_name (str | Unset): Human-friendly name for UI display. Defaults to `name`.
        weight_source (WeightSource | Unset): Source of the model weights:
            - `huggingface`: download from HuggingFace using `huggingface_model_id`
            - `s3_presigned`: download from a presigned S3 URL
            - `s3_assume_role`: download from S3 using an assumed IAM role
        s3_url (str | Unset): Required when `weight_source` is `s3_presigned` or
            `s3_assume_role`. Conditional requirement is enforced by
            the server (returns 422); not encoded as a JSON Schema
            keyword for OAS-3.0-tooling compatibility.
        s3_role_arn (str | Unset): Required when `weight_source` is `s3_assume_role`. The role
            name (the segment after `:role/`) must start with
            `graphn-byom-`; GraphN's platform IAM policy is scoped to
            that prefix as a defense-in-depth boundary, and the
            customer-facing CloudFormation template enforces the same
            constraint at stack-create time. Conditional requirement
            (s3_assume_role only) is enforced by the server (returns
            422); the format itself is checked against this pattern.
        hf_token_secret_id (str | Unset): ID of a workspace secret holding a HuggingFace access token.
            Required for gated HuggingFace models.
        gpu_count (int | Unset):  Default: 1.
        max_model_len (int | Unset):
        gpu_memory_utilization (float | Unset):  Default: 0.9.
        quantization (CustomModelCreateQuantization | Unset):
        capabilities (list[Capability] | Unset):
        min_replicas (int | Unset):  Default: 0.
        max_replicas (int | Unset):  Default: 1.
        cooldown_seconds (int | Unset):  Default: 600.
        base_model_id (str | Unset): Override / hint for LoRA imports. Must be one of the
            platform's allowlisted base models (see
            `GET /v1/{workspaceId}/custom-models/supported-architectures`).

            * **`weight_source=s3_*`**: this is the **only** way to
              classify the bundle as a LoRA adapter at create-time --
              omitting it routes the import through the base path,
              and a bundle that later turns out to be a LoRA adapter
              will deploy to `failed` with an actionable error
              ("re-create with `base_model_id` set").
            * **`weight_source=huggingface`**: the field **overrides**
              `adapter_config.json::base_model_name_or_path` from the
              adapter repo. Useful for adapters trained against a
              local filesystem path (e.g. `C:/users/.../base`) whose
              recorded base id isn't a valid HF id. When the override
              disagrees with the adapter's declared base the caller's
              value wins; the disagreement is logged server-side for
              debuggability.

            Ignored when the resolved artifact type is `base`.
             Example: Qwen/Qwen3.5-4B.
    """

    name: str
    huggingface_model_id: str
    display_name: str | Unset = UNSET
    weight_source: WeightSource | Unset = UNSET
    s3_url: str | Unset = UNSET
    s3_role_arn: str | Unset = UNSET
    hf_token_secret_id: str | Unset = UNSET
    gpu_count: int | Unset = 1
    max_model_len: int | Unset = UNSET
    gpu_memory_utilization: float | Unset = 0.9
    quantization: CustomModelCreateQuantization | Unset = UNSET
    capabilities: list[Capability] | Unset = UNSET
    min_replicas: int | Unset = 0
    max_replicas: int | Unset = 1
    cooldown_seconds: int | Unset = 600
    base_model_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        huggingface_model_id = self.huggingface_model_id

        display_name = self.display_name

        weight_source: str | Unset = UNSET
        if not isinstance(self.weight_source, Unset):
            weight_source = self.weight_source.value

        s3_url = self.s3_url

        s3_role_arn = self.s3_role_arn

        hf_token_secret_id = self.hf_token_secret_id

        gpu_count = self.gpu_count

        max_model_len = self.max_model_len

        gpu_memory_utilization = self.gpu_memory_utilization

        quantization: str | Unset = UNSET
        if not isinstance(self.quantization, Unset):
            quantization = self.quantization.value

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = []
            for capabilities_item_data in self.capabilities:
                capabilities_item = capabilities_item_data.value
                capabilities.append(capabilities_item)

        min_replicas = self.min_replicas

        max_replicas = self.max_replicas

        cooldown_seconds = self.cooldown_seconds

        base_model_id = self.base_model_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "huggingface_model_id": huggingface_model_id,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if weight_source is not UNSET:
            field_dict["weight_source"] = weight_source
        if s3_url is not UNSET:
            field_dict["s3_url"] = s3_url
        if s3_role_arn is not UNSET:
            field_dict["s3_role_arn"] = s3_role_arn
        if hf_token_secret_id is not UNSET:
            field_dict["hf_token_secret_id"] = hf_token_secret_id
        if gpu_count is not UNSET:
            field_dict["gpu_count"] = gpu_count
        if max_model_len is not UNSET:
            field_dict["max_model_len"] = max_model_len
        if gpu_memory_utilization is not UNSET:
            field_dict["gpu_memory_utilization"] = gpu_memory_utilization
        if quantization is not UNSET:
            field_dict["quantization"] = quantization
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if min_replicas is not UNSET:
            field_dict["min_replicas"] = min_replicas
        if max_replicas is not UNSET:
            field_dict["max_replicas"] = max_replicas
        if cooldown_seconds is not UNSET:
            field_dict["cooldown_seconds"] = cooldown_seconds
        if base_model_id is not UNSET:
            field_dict["base_model_id"] = base_model_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        huggingface_model_id = d.pop("huggingface_model_id")

        display_name = d.pop("display_name", UNSET)

        _weight_source = d.pop("weight_source", UNSET)
        weight_source: WeightSource | Unset
        if isinstance(_weight_source, Unset):
            weight_source = UNSET
        else:
            weight_source = WeightSource(_weight_source)

        s3_url = d.pop("s3_url", UNSET)

        s3_role_arn = d.pop("s3_role_arn", UNSET)

        hf_token_secret_id = d.pop("hf_token_secret_id", UNSET)

        gpu_count = d.pop("gpu_count", UNSET)

        max_model_len = d.pop("max_model_len", UNSET)

        gpu_memory_utilization = d.pop("gpu_memory_utilization", UNSET)

        _quantization = d.pop("quantization", UNSET)
        quantization: CustomModelCreateQuantization | Unset
        if isinstance(_quantization, Unset):
            quantization = UNSET
        else:
            quantization = CustomModelCreateQuantization(_quantization)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: list[Capability] | Unset = UNSET
        if _capabilities is not UNSET:
            capabilities = []
            for capabilities_item_data in _capabilities:
                capabilities_item = Capability(capabilities_item_data)

                capabilities.append(capabilities_item)

        min_replicas = d.pop("min_replicas", UNSET)

        max_replicas = d.pop("max_replicas", UNSET)

        cooldown_seconds = d.pop("cooldown_seconds", UNSET)

        base_model_id = d.pop("base_model_id", UNSET)

        custom_model_create = cls(
            name=name,
            huggingface_model_id=huggingface_model_id,
            display_name=display_name,
            weight_source=weight_source,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            hf_token_secret_id=hf_token_secret_id,
            gpu_count=gpu_count,
            max_model_len=max_model_len,
            gpu_memory_utilization=gpu_memory_utilization,
            quantization=quantization,
            capabilities=capabilities,
            min_replicas=min_replicas,
            max_replicas=max_replicas,
            cooldown_seconds=cooldown_seconds,
            base_model_id=base_model_id,
        )

        return custom_model_create
