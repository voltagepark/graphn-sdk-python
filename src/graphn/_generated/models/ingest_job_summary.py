from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="IngestJobSummary")


@_attrs_define
class IngestJobSummary:
    """
    Attributes:
        total (int):
        pending (int):
        running (int):
        succeeded (int):
        failed (int):
        skipped (int):
    """

    total: int
    pending: int
    running: int
    succeeded: int
    failed: int
    skipped: int

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        running = self.running

        succeeded = self.succeeded

        failed = self.failed

        skipped = self.skipped

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "pending": pending,
                "running": running,
                "succeeded": succeeded,
                "failed": failed,
                "skipped": skipped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total")

        pending = d.pop("pending")

        running = d.pop("running")

        succeeded = d.pop("succeeded")

        failed = d.pop("failed")

        skipped = d.pop("skipped")

        ingest_job_summary = cls(
            total=total,
            pending=pending,
            running=running,
            succeeded=succeeded,
            failed=failed,
            skipped=skipped,
        )

        return ingest_job_summary
