"""Public types for workspace secrets.

Mirrors the OpenAPI ``Secret`` schema. The plaintext value is never
returned by the API — list / get responses include only
``value_preview`` (the first few characters), so the SDK type stays in
sync.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Secret(BaseModel):
    """Workspace secret record."""

    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    workspace_id: str
    name: str
    value_preview: str
    created_at: datetime
    updated_at: datetime
    provider_id: str | None = None
    field_name: str | None = None
