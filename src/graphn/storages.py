"""REST overlay for workspace object stores, plus the S3-style host."""

from __future__ import annotations

from typing import Any, BinaryIO

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact


class Storage(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    name: str
    status: str
    display_name: str | None = None
    description: str | None = None
    object_count: int | None = None
    total_size_bytes: int | None = None


class StorageFile(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    key: str
    size: int
    last_modified: str | None = None
    etag: str | None = None


class StorageUpload(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    key: str
    size: int
    store_name: str
    etag: str | None = None


class Storages:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(self, *, name: str, description: str | None = None) -> Storage:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("storages"),
            json=compact({"name": name, "description": description}),
        )
        return Storage.model_validate(data)

    def list(self) -> SyncPage[Storage]:
        def fetch(_token: str | None) -> RawPage[Storage]:
            data = self._transport.request("GET", self._transport.cp_path("storages"))
            return RawPage.from_response(data or {}, Storage.model_validate)

        return SyncPage(first=fetch(None), fetch_next=fetch)

    def get(self, store_name: str) -> Storage:
        data = self._transport.request("GET", self._transport.cp_path("storages", store_name))
        return Storage.model_validate(data)

    def delete(self, store_name: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("storages", store_name))

    def files(self, store_name: str, **params: Any) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET",
                self._transport.cp_path("storages", store_name, "files"),
                params=compact(params),
            )
            or {}
        )

    def upload(
        self,
        store_name: str,
        *,
        file: bytes | BinaryIO,
        filename: str,
        path: str | None = None,
        content_type: str = "application/octet-stream",
    ) -> StorageUpload:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("storages", store_name, "files"),
            files={"file": (filename, file, content_type)},
            params=compact({"path": path}),
        )
        return StorageUpload.model_validate(data)

    def put_object(
        self, bucket: str, key: str, data: bytes, *, content_type: str | None = None
    ) -> Any:
        headers = compact({"Content-Type": content_type})
        return self._transport.request(
            "PUT",
            self._transport.storage_object_url(bucket, key),
            content=data,
            headers=headers or None,
        )

    def get_object(self, bucket: str, key: str) -> bytes:
        body = self._transport.request("GET", self._transport.storage_object_url(bucket, key))
        if isinstance(body, bytes):
            return body
        return b"" if body is None else str(body).encode()

    def delete_object(self, bucket: str, key: str) -> None:
        self._transport.request("DELETE", self._transport.storage_object_url(bucket, key))


class AsyncStorages:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(self, *, name: str, description: str | None = None) -> Storage:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("storages"),
            json=compact({"name": name, "description": description}),
        )
        return Storage.model_validate(data)

    async def list(self) -> AsyncPage[Storage]:
        async def fetch(_token: str | None) -> RawPage[Storage]:
            data = await self._transport.request("GET", self._transport.cp_path("storages"))
            return RawPage.from_response(data or {}, Storage.model_validate)

        return AsyncPage(first=await fetch(None), fetch_next=fetch)

    async def get(self, store_name: str) -> Storage:
        data = await self._transport.request("GET", self._transport.cp_path("storages", store_name))
        return Storage.model_validate(data)

    async def delete(self, store_name: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("storages", store_name))

    async def files(self, store_name: str, **params: Any) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET",
                self._transport.cp_path("storages", store_name, "files"),
                params=compact(params),
            )
            or {}
        )

    async def upload(
        self,
        store_name: str,
        *,
        file: bytes | BinaryIO,
        filename: str,
        path: str | None = None,
        content_type: str = "application/octet-stream",
    ) -> StorageUpload:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("storages", store_name, "files"),
            files={"file": (filename, file, content_type)},
            params=compact({"path": path}),
        )
        return StorageUpload.model_validate(data)

    async def put_object(
        self, bucket: str, key: str, data: bytes, *, content_type: str | None = None
    ) -> Any:
        headers = compact({"Content-Type": content_type})
        return await self._transport.request(
            "PUT",
            self._transport.storage_object_url(bucket, key),
            content=data,
            headers=headers or None,
        )

    async def get_object(self, bucket: str, key: str) -> bytes:
        body = await self._transport.request("GET", self._transport.storage_object_url(bucket, key))
        if isinstance(body, bytes):
            return body
        return b"" if body is None else str(body).encode()

    async def delete_object(self, bucket: str, key: str) -> None:
        await self._transport.request("DELETE", self._transport.storage_object_url(bucket, key))
