from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.mpu_complete_request import MpuCompleteRequest
from ...models.post_object_type import PostObjectType
from ...models.storage_post_result import StoragePostResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket: str,
    key: str,
    *,
    body: MpuCompleteRequest,
    uploads: str | Unset = UNSET,
    uploadId: str | Unset = UNSET,
    type_: PostObjectType | Unset = UNSET,
    expires: int | Unset = UNSET,
    max_size: int | Unset = UNSET,
    content_type: str | Unset = UNSET,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["uploads"] = uploads

    params["uploadId"] = uploadId

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["expires"] = expires

    params["max-size"] = max_size

    params["content-type"] = content_type

    params["upload_id"] = upload_id

    params["part_number"] = part_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{bucket}/{key}".format(
            bucket=quote(str(bucket), safe=""),
            key=quote(str(key), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | StoragePostResult | None:
    if response.status_code == 200:
        response_200 = StoragePostResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | StoragePostResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: MpuCompleteRequest,
    uploads: str | Unset = UNSET,
    uploadId: str | Unset = UNSET,
    type_: PostObjectType | Unset = UNSET,
    expires: int | Unset = UNSET,
    max_size: int | Unset = UNSET,
    content_type: str | Unset = UNSET,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Response[Error | StoragePostResult]:
    """MPU init/complete or mint a presigned URL

     Query-string dispatch:

    - `?uploads` — initiate multipart upload.
    - `?uploadId=` — complete MPU. Body `{ "parts":[{"part_number":N,"etag":"..."}] }`.
    - `?type=download&expires=SEC` — presigned GET.
    - `?type=upload&expires=&max-size=&content-type=` — presigned PUT.
    - `?type=upload_part&upload_id=&part_number=` — presigned MPU part.

    Args:
        bucket (str):
        key (str):
        uploads (str | Unset):
        uploadId (str | Unset):
        type_ (PostObjectType | Unset):
        expires (int | Unset):
        max_size (int | Unset):
        content_type (str | Unset):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (MpuCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StoragePostResult]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        key=key,
        body=body,
        uploads=uploads,
        uploadId=uploadId,
        type_=type_,
        expires=expires,
        max_size=max_size,
        content_type=content_type,
        upload_id=upload_id,
        part_number=part_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: MpuCompleteRequest,
    uploads: str | Unset = UNSET,
    uploadId: str | Unset = UNSET,
    type_: PostObjectType | Unset = UNSET,
    expires: int | Unset = UNSET,
    max_size: int | Unset = UNSET,
    content_type: str | Unset = UNSET,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Error | StoragePostResult | None:
    """MPU init/complete or mint a presigned URL

     Query-string dispatch:

    - `?uploads` — initiate multipart upload.
    - `?uploadId=` — complete MPU. Body `{ "parts":[{"part_number":N,"etag":"..."}] }`.
    - `?type=download&expires=SEC` — presigned GET.
    - `?type=upload&expires=&max-size=&content-type=` — presigned PUT.
    - `?type=upload_part&upload_id=&part_number=` — presigned MPU part.

    Args:
        bucket (str):
        key (str):
        uploads (str | Unset):
        uploadId (str | Unset):
        type_ (PostObjectType | Unset):
        expires (int | Unset):
        max_size (int | Unset):
        content_type (str | Unset):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (MpuCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StoragePostResult
    """

    return sync_detailed(
        bucket=bucket,
        key=key,
        client=client,
        body=body,
        uploads=uploads,
        uploadId=uploadId,
        type_=type_,
        expires=expires,
        max_size=max_size,
        content_type=content_type,
        upload_id=upload_id,
        part_number=part_number,
    ).parsed


async def asyncio_detailed(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: MpuCompleteRequest,
    uploads: str | Unset = UNSET,
    uploadId: str | Unset = UNSET,
    type_: PostObjectType | Unset = UNSET,
    expires: int | Unset = UNSET,
    max_size: int | Unset = UNSET,
    content_type: str | Unset = UNSET,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Response[Error | StoragePostResult]:
    """MPU init/complete or mint a presigned URL

     Query-string dispatch:

    - `?uploads` — initiate multipart upload.
    - `?uploadId=` — complete MPU. Body `{ "parts":[{"part_number":N,"etag":"..."}] }`.
    - `?type=download&expires=SEC` — presigned GET.
    - `?type=upload&expires=&max-size=&content-type=` — presigned PUT.
    - `?type=upload_part&upload_id=&part_number=` — presigned MPU part.

    Args:
        bucket (str):
        key (str):
        uploads (str | Unset):
        uploadId (str | Unset):
        type_ (PostObjectType | Unset):
        expires (int | Unset):
        max_size (int | Unset):
        content_type (str | Unset):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (MpuCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StoragePostResult]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        key=key,
        body=body,
        uploads=uploads,
        uploadId=uploadId,
        type_=type_,
        expires=expires,
        max_size=max_size,
        content_type=content_type,
        upload_id=upload_id,
        part_number=part_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: MpuCompleteRequest,
    uploads: str | Unset = UNSET,
    uploadId: str | Unset = UNSET,
    type_: PostObjectType | Unset = UNSET,
    expires: int | Unset = UNSET,
    max_size: int | Unset = UNSET,
    content_type: str | Unset = UNSET,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Error | StoragePostResult | None:
    """MPU init/complete or mint a presigned URL

     Query-string dispatch:

    - `?uploads` — initiate multipart upload.
    - `?uploadId=` — complete MPU. Body `{ "parts":[{"part_number":N,"etag":"..."}] }`.
    - `?type=download&expires=SEC` — presigned GET.
    - `?type=upload&expires=&max-size=&content-type=` — presigned PUT.
    - `?type=upload_part&upload_id=&part_number=` — presigned MPU part.

    Args:
        bucket (str):
        key (str):
        uploads (str | Unset):
        uploadId (str | Unset):
        type_ (PostObjectType | Unset):
        expires (int | Unset):
        max_size (int | Unset):
        content_type (str | Unset):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (MpuCompleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StoragePostResult
    """

    return (
        await asyncio_detailed(
            bucket=bucket,
            key=key,
            client=client,
            body=body,
            uploads=uploads,
            uploadId=uploadId,
            type_=type_,
            expires=expires,
            max_size=max_size,
            content_type=content_type,
            upload_id=upload_id,
            part_number=part_number,
        )
    ).parsed
