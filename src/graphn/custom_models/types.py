"""Public types for custom models.

Mirrors the schemas in the public OpenAPI spec
(``CustomModel``, ``CustomModelCreate``, etc.). When
``scripts/regenerate.sh`` runs, the generated transport ships richer
attrs-based dataclasses under ``graphn._generated.models``; the
ergonomic resource layer wraps those internally and returns the
Pydantic types defined here so customer code always sees a stable,
hand-curated surface.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

WeightSource = Literal["huggingface", "s3_presigned", "s3_assume_role"]
"""Where the model weights come from."""

Capability = Literal["tool_calling", "vision", "embedding", "reasoning"]

CustomModelStatus = Literal[
    "pending",
    "deploying",
    "ready",
    "failed",
    "deleting",
]

Quantization = Literal["awq", "gptq", "fp8", "squeezellm", "marlin", "gguf"]

ArtifactType = Literal["base", "lora"]
"""Whether a custom-model import is a full base checkpoint or a LoRA adapter."""


class CustomModel(BaseModel):
    """Public custom-model record.

    Mirrors the OpenAPI ``CustomModel`` schema (the ``additionalProperties:
    true`` flag in the spec means future internal fields appear as
    extras under ``model_extra``).
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True, frozen=True)

    id: str
    name: str
    workspace_id: str
    status: CustomModelStatus
    weight_source: WeightSource
    gpu_count: int
    capabilities: list[Capability] = Field(default_factory=list)
    min_replicas: int
    max_replicas: int
    cooldown_seconds: int
    gpu_memory_utilization: float
    created_at: datetime
    updated_at: datetime

    display_name: str | None = None
    huggingface_model_id: str | None = None
    s3_url: str | None = None
    s3_role_arn: str | None = None
    max_model_len: int | None = None
    quantization: Quantization | None = None
    replicas_available: int | None = None
    endpoint: str | None = None
    error_message: str | None = None
    num_params: int | None = None
    estimated_memory_gb: float | None = None
    architectures: list[str] | None = None

    artifact_type: ArtifactType | None = None
    """``"base"`` for full checkpoints, ``"lora"`` for adapter imports.

    Set eagerly at create-time. HuggingFace imports are classified by
    probing ``adapter_config.json`` on the upstream repo; S3 imports are
    classified as ``"lora"`` iff ``base_model_id`` is supplied on
    :meth:`CustomModels.create`. Older control planes that predate the
    LoRA work leave this field unset on existing records — treat
    ``None`` as ``"base"`` for compatibility.
    """
    base_model_id: str | None = None
    """Base model id this adapter loads on top of (populated when
    ``artifact_type == "lora"``)."""
    lora_adapter_name: str | None = None
    """vLLM routing name the adapter is served under. Clients address
    the adapter via ``model=<lora_adapter_name>`` in chat completions."""
    lora_rank: int | None = None
    """``r`` value from the adapter's ``adapter_config.json``."""


class CustomModelAccess(BaseModel):
    """Workspace allowlist check result."""

    model_config = ConfigDict(extra="allow", frozen=True)

    allowed: bool


class GpuHoursResponse(BaseModel):
    """Cumulative GPU-hours billed for a custom model."""

    model_config = ConfigDict(extra="allow", frozen=True)

    gpu_hours: float


class ValidateModelResponse(BaseModel):
    """Result of ``validateCustomModel``."""

    model_config = ConfigDict(extra="allow", frozen=True)

    valid: bool
    error: str | None = None
    architectures: list[str] | None = None
    supports_mtp: bool | None = None
    num_params: int | None = None
    estimated_memory_gb: float | None = None
    max_context_length: int | None = None

    artifact_type: ArtifactType | None = None
    """``"lora"`` when AF detected an ``adapter_config.json`` in the
    HuggingFace repo, ``"base"`` otherwise. Defaults to ``"base"`` on
    fresh responses; older control planes may omit the field entirely,
    in which case the bundle should be treated as a base checkpoint.

    When ``artifact_type == "lora"``, ``architectures``, ``num_params``,
    ``estimated_memory_gb``, and ``max_context_length`` describe the
    *base* model resolved from ``adapter_config.json`` — not the
    adapter itself.
    """
    detected_base_model_id: str | None = None
    """Base model id read from ``adapter_config.json::base_model_name_or_path``.
    Populated only when ``artifact_type == "lora"``."""
    lora_rank: int | None = None
    """``r`` value from the adapter's ``adapter_config.json``.
    Populated only when ``artifact_type == "lora"``."""


class ArchitectureInfo(BaseModel):
    """A HuggingFace architecture the platform can serve.

    Returned as elements of :class:`SupportedArchitectures.architectures`.
    """

    model_config = ConfigDict(extra="allow", frozen=True)

    name: str
    """HuggingFace ``architectures[0]`` value (e.g. ``"LlamaForCausalLM"``,
    ``"Qwen3VLMoeForConditionalGeneration"``)."""
    capabilities: list[str] = Field(default_factory=list)
    """Capability tags this architecture exposes — ``"tool_calling"``,
    ``"vision"``, ``"image_input"``, ``"video_input"``, ``"streaming"``,
    ``"json_mode"``."""


class SupportedArchitectures(BaseModel):
    """Catalog of model architectures supported for custom-model import.

    Returned by :meth:`CustomModels.supported_architectures`. The list
    is updated alongside platform runtime upgrades; clients should not
    cache it across build cycles.
    """

    model_config = ConfigDict(extra="allow", frozen=True)

    architectures: list[ArchitectureInfo] = Field(default_factory=list)
