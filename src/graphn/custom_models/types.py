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


class CustomModelAccess(BaseModel):
    """Workspace allowlist check result."""

    model_config = ConfigDict(extra="allow", frozen=True)

    allowed: bool


class GpuHoursResponse(BaseModel):
    """Cumulative GPU-hours billed for a custom model."""

    model_config = ConfigDict(extra="allow", frozen=True)

    gpu_hours: float


class ArchitectureInfo(BaseModel):
    """Single supported HuggingFace architecture."""

    model_config = ConfigDict(extra="allow", frozen=True)

    name: str
    capabilities: list[Capability]


class SupportedArchitectures(BaseModel):
    """Result of ``listSupportedArchitectures``."""

    model_config = ConfigDict(extra="allow", frozen=True)

    architectures: list[ArchitectureInfo]


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
