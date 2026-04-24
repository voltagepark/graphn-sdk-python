"""Public types for workspace secrets.

Replaced by re-exports from ``graphn._generated`` after the
``sdk-generate`` task runs.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Secret(BaseModel):
    """Stub secret representation matching the OpenAPI ``Secret`` schema."""

    model_config = ConfigDict(extra="allow")

    id: str
    name: str
    description: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
