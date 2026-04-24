"""Public types for custom models.

These will be replaced by re-exports from ``graphn._generated`` after
the ``sdk-generate`` task runs ``openapi-python-client``. Until then we
expose simple ``Literal``s and a Pydantic model so the rest of the SDK
can be wired up against stable names.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

WeightSource = Literal["huggingface"]
"""Where the model weights come from. Currently HuggingFace only."""

Capability = Literal[
    "chat",
    "completion",
    "embedding",
    "tool_use",
    "vision",
    "speech_to_text",
    "text_to_speech",
]

CustomModelStatus = Literal[
    "pending",
    "deploying",
    "ready",
    "failed",
    "deleting",
]


class CustomModel(BaseModel):
    """Stub custom-model representation.

    Replaced by the generated equivalent once ``scripts/regenerate.sh``
    runs (``sdk-generate`` task). Field names mirror the OpenAPI
    ``CustomModel`` schema.
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str
    workspace_id: str = Field(alias="workspace_id")
    weight_source: WeightSource
    huggingface_model_id: str | None = None
    status: CustomModelStatus
    capabilities: list[Capability] = Field(default_factory=list)
    min_replicas: int = 0
    max_replicas: int = 1
    cooldown_seconds: int = 600
    created_at: datetime | None = None
    updated_at: datetime | None = None
