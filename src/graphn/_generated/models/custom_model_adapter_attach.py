from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.weight_source import WeightSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomModelAdapterAttach")


@_attrs_define
class CustomModelAdapterAttach:
    """Preview. Request body for
    `POST /v1/{workspaceId}/custom-models/{modelId}/adapters`.

        Attributes:
            name (str | Unset): URL-safe adapter name. Must be unique within the workspace.
                Defaults to the last segment of `huggingface_model_id`,
                lowercased. Chat completions take the adapter's ID
                (`custom:<id>`), not its name.
            display_name (str | Unset): Human-friendly name for UI display. Defaults to `name`.
            weight_source (WeightSource | Unset): Source of the model weights:
                - `huggingface`: download from HuggingFace using `huggingface_model_id`
                - `s3_presigned`: download from a presigned S3 URL
                - `s3_assume_role`: download from S3 using an assumed IAM role
            huggingface_model_id (str | Unset): Hugging Face repo id (`org/name`) of the adapter. Required when
                `weight_source` is `huggingface`; enforced by the server.
                 Example: my-org/qwen3-32b-support-lora.
            hf_token_secret_id (str | Unset): ID of a workspace secret holding a HuggingFace access token.
                Required for gated or private adapter repos.
            s3_url (str | Unset): Required when `weight_source` is `s3_presigned` or
                `s3_assume_role`; enforced by the server.
            s3_role_arn (str | Unset): Required when `weight_source` is `s3_assume_role`. The role name
                must start with `graphn-byom-`.
            s3_external_id (str | Unset): ExternalId from the customer's IAM trust policy, for
                `s3_assume_role`. Generated when omitted.
            base_mismatch_acknowledged (bool | Unset): Accept an adapter whose declared base differs from this base's
                Hugging Face ID; staging otherwise refuses it. Recorded on the
                adapter. A base imported from S3 has no ID to compare.
                 Default: False.
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    weight_source: WeightSource | Unset = UNSET
    huggingface_model_id: str | Unset = UNSET
    hf_token_secret_id: str | Unset = UNSET
    s3_url: str | Unset = UNSET
    s3_role_arn: str | Unset = UNSET
    s3_external_id: str | Unset = UNSET
    base_mismatch_acknowledged: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        weight_source: str | Unset = UNSET
        if not isinstance(self.weight_source, Unset):
            weight_source = self.weight_source.value

        huggingface_model_id = self.huggingface_model_id

        hf_token_secret_id = self.hf_token_secret_id

        s3_url = self.s3_url

        s3_role_arn = self.s3_role_arn

        s3_external_id = self.s3_external_id

        base_mismatch_acknowledged = self.base_mismatch_acknowledged

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if weight_source is not UNSET:
            field_dict["weight_source"] = weight_source
        if huggingface_model_id is not UNSET:
            field_dict["huggingface_model_id"] = huggingface_model_id
        if hf_token_secret_id is not UNSET:
            field_dict["hf_token_secret_id"] = hf_token_secret_id
        if s3_url is not UNSET:
            field_dict["s3_url"] = s3_url
        if s3_role_arn is not UNSET:
            field_dict["s3_role_arn"] = s3_role_arn
        if s3_external_id is not UNSET:
            field_dict["s3_external_id"] = s3_external_id
        if base_mismatch_acknowledged is not UNSET:
            field_dict["base_mismatch_acknowledged"] = base_mismatch_acknowledged

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("display_name", UNSET)

        _weight_source = d.pop("weight_source", UNSET)
        weight_source: WeightSource | Unset
        if isinstance(_weight_source, Unset):
            weight_source = UNSET
        else:
            weight_source = WeightSource(_weight_source)

        huggingface_model_id = d.pop("huggingface_model_id", UNSET)

        hf_token_secret_id = d.pop("hf_token_secret_id", UNSET)

        s3_url = d.pop("s3_url", UNSET)

        s3_role_arn = d.pop("s3_role_arn", UNSET)

        s3_external_id = d.pop("s3_external_id", UNSET)

        base_mismatch_acknowledged = d.pop("base_mismatch_acknowledged", UNSET)

        custom_model_adapter_attach = cls(
            name=name,
            display_name=display_name,
            weight_source=weight_source,
            huggingface_model_id=huggingface_model_id,
            hf_token_secret_id=hf_token_secret_id,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            s3_external_id=s3_external_id,
            base_mismatch_acknowledged=base_mismatch_acknowledged,
        )

        return custom_model_adapter_attach
