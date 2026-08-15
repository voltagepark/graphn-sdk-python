"""Knowledge bases, documents, search, and async ingest."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any, BinaryIO

from pydantic import BaseModel, ConfigDict

from graphn._exceptions import APIError
from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._poll import apoll_until, poll_until
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra, page_params

_INGEST_TERMINAL = frozenset({"succeeded", "failed", "partial", "canceled", "cancelled"})
_INGEST_FAILED = frozenset({"failed"})
_DEFAULT_WAIT_TIMEOUT_SECONDS = 1800.0
_DEFAULT_POLL_INTERVAL_SECONDS = 2.0


class KnowledgeBase(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    name: str
    workspace_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    description: str | None = None
    document_count: int | None = None
    chunk_count: int | None = None
    embedding_model: str | None = None


class KbDocument(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    kb_id: str
    filename: str
    content_type: str
    chunk_count: int
    created_at: datetime
    document_type: str | None = None
    image_url: str | None = None


class SearchResult(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    text: str
    score: float
    document_id: str
    source: str
    metadata: dict[str, Any] | None = None


class SearchResponse(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    results: list[SearchResult]
    query: str
    total: int


class IngestJobSummary(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    total: int
    pending: int
    running: int
    succeeded: int
    failed: int
    skipped: int


class IngestJob(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    kb_id: str
    status: str
    summary: IngestJobSummary
    created_at: datetime
    updated_at: datetime | None = None


def _raise_if_ingest_failed(job: IngestJob) -> IngestJob:
    if job.status in _INGEST_FAILED:
        raise APIError(
            f"ingest job {job.id} failed",
            status_code=0,
            code="ingest_failed",
            details={"job_id": job.id, "status": job.status},
        )
    return job


class KnowledgeBases:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        description: str | None = None,
        embedding_model: str | None = None,
        extra: Mapping[str, Any] | None = None,
        **fields: Any,
    ) -> KnowledgeBase:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases"),
            json=merge_extra(
                compact(
                    {
                        "name": name,
                        "description": description,
                        "embedding_model": embedding_model,
                        **fields,
                    }
                ),
                extra,
            ),
        )
        return KnowledgeBase.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> SyncPage[KnowledgeBase]:
        def fetch(token: str | None) -> RawPage[KnowledgeBase]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("knowledgebases"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, KnowledgeBase.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, kb_id: str) -> KnowledgeBase:
        data = self._transport.request("GET", self._transport.cp_path("knowledgebases", kb_id))
        return KnowledgeBase.model_validate(data)

    def update(self, kb_id: str, **fields: Any) -> KnowledgeBase:
        extra = fields.pop("extra", None)
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("knowledgebases", kb_id),
            json=merge_extra(compact(fields), extra),
        )
        return KnowledgeBase.model_validate(data)

    def delete(self, kb_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("knowledgebases", kb_id))

    def stats(self, kb_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET", self._transport.cp_path("knowledgebases", kb_id, "stats")
            )
            or {}
        )

    def documents(self, kb_id: str) -> list[KbDocument]:
        data = self._transport.request(
            "GET", self._transport.cp_path("knowledgebases", kb_id, "documents")
        )
        return [KbDocument.model_validate(item) for item in (data or [])]

    def ingest_url(self, kb_id: str, *, url: str, **fields: Any) -> KbDocument:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "documents"),
            json=compact({"url": url, **fields}),
        )
        return KbDocument.model_validate(data)

    def upload(
        self,
        kb_id: str,
        *,
        file: bytes | BinaryIO,
        filename: str = "document",
        content_type: str = "application/octet-stream",
    ) -> KbDocument:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "documents"),
            files={"file": (filename, file, content_type)},
        )
        return KbDocument.model_validate(data)

    def search(self, kb_id: str, *, query: str, **fields: Any) -> SearchResponse:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "search"),
            json=compact({"query": query, **fields}),
        )
        return SearchResponse.model_validate(data)

    def submit_ingest(self, kb_id: str, *, items: list[Mapping[str, Any]]) -> IngestJob:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "ingest"),
            json={"items": list(items)},
        )
        return IngestJob.model_validate(data)

    def get_ingest(self, kb_id: str, job_id: str) -> IngestJob:
        data = self._transport.request(
            "GET", self._transport.cp_path("knowledgebases", kb_id, "ingest", job_id)
        )
        return IngestJob.model_validate(data)

    def wait_ingest(
        self,
        kb_id: str,
        job_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> IngestJob:
        job = poll_until(
            lambda: self.get_ingest(kb_id, job_id),
            done=lambda item: item.status in _INGEST_TERMINAL,
            timeout=timeout,
            interval=poll_interval,
            timeout_message=lambda item: (
                f"ingest job {job_id} did not finish within {timeout:.0f}s "
                f"(last status: {item.status!r})"
            ),
        )
        return _raise_if_ingest_failed(job)


class AsyncKnowledgeBases:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        description: str | None = None,
        embedding_model: str | None = None,
        extra: Mapping[str, Any] | None = None,
        **fields: Any,
    ) -> KnowledgeBase:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases"),
            json=merge_extra(
                compact(
                    {
                        "name": name,
                        "description": description,
                        "embedding_model": embedding_model,
                        **fields,
                    }
                ),
                extra,
            ),
        )
        return KnowledgeBase.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> AsyncPage[KnowledgeBase]:
        async def fetch(token: str | None) -> RawPage[KnowledgeBase]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("knowledgebases"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, KnowledgeBase.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, kb_id: str) -> KnowledgeBase:
        data = await self._transport.request(
            "GET", self._transport.cp_path("knowledgebases", kb_id)
        )
        return KnowledgeBase.model_validate(data)

    async def update(self, kb_id: str, **fields: Any) -> KnowledgeBase:
        extra = fields.pop("extra", None)
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("knowledgebases", kb_id),
            json=merge_extra(compact(fields), extra),
        )
        return KnowledgeBase.model_validate(data)

    async def delete(self, kb_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("knowledgebases", kb_id))

    async def stats(self, kb_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET", self._transport.cp_path("knowledgebases", kb_id, "stats")
            )
            or {}
        )

    async def documents(self, kb_id: str) -> list[KbDocument]:
        data = await self._transport.request(
            "GET", self._transport.cp_path("knowledgebases", kb_id, "documents")
        )
        return [KbDocument.model_validate(item) for item in (data or [])]

    async def ingest_url(self, kb_id: str, *, url: str, **fields: Any) -> KbDocument:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "documents"),
            json=compact({"url": url, **fields}),
        )
        return KbDocument.model_validate(data)

    async def upload(
        self,
        kb_id: str,
        *,
        file: bytes | BinaryIO,
        filename: str = "document",
        content_type: str = "application/octet-stream",
    ) -> KbDocument:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "documents"),
            files={"file": (filename, file, content_type)},
        )
        return KbDocument.model_validate(data)

    async def search(self, kb_id: str, *, query: str, **fields: Any) -> SearchResponse:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "search"),
            json=compact({"query": query, **fields}),
        )
        return SearchResponse.model_validate(data)

    async def submit_ingest(self, kb_id: str, *, items: list[Mapping[str, Any]]) -> IngestJob:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("knowledgebases", kb_id, "ingest"),
            json={"items": list(items)},
        )
        return IngestJob.model_validate(data)

    async def get_ingest(self, kb_id: str, job_id: str) -> IngestJob:
        data = await self._transport.request(
            "GET", self._transport.cp_path("knowledgebases", kb_id, "ingest", job_id)
        )
        return IngestJob.model_validate(data)

    async def wait_ingest(
        self,
        kb_id: str,
        job_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> IngestJob:
        async def fetch() -> IngestJob:
            return await self.get_ingest(kb_id, job_id)

        job = await apoll_until(
            fetch,
            done=lambda item: item.status in _INGEST_TERMINAL,
            timeout=timeout,
            interval=poll_interval,
            timeout_message=lambda item: (
                f"ingest job {job_id} did not finish within {timeout:.0f}s "
                f"(last status: {item.status!r})"
            ),
        )
        return _raise_if_ingest_failed(job)
