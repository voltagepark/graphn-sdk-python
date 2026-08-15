from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.storage_upload import StorageUpload
from ...models.upload_storage_file_body import UploadStorageFileBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    store_name: str,
    *,
    body: UploadStorageFileBody,
    path: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/storages/{store_name}/files".format(
            workspace_id=quote(str(workspace_id), safe=""),
            store_name=quote(str(store_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | StorageUpload | None:
    if response.status_code == 201:
        response_201 = StorageUpload.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | StorageUpload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadStorageFileBody,
    path: str | Unset = UNSET,
) -> Response[Error | StorageUpload]:
    """Upload a file

    Args:
        workspace_id (str):
        store_name (str):
        path (str | Unset):
        body (UploadStorageFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StorageUpload]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        body=body,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadStorageFileBody,
    path: str | Unset = UNSET,
) -> Error | StorageUpload | None:
    """Upload a file

    Args:
        workspace_id (str):
        store_name (str):
        path (str | Unset):
        body (UploadStorageFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StorageUpload
    """

    return sync_detailed(
        workspace_id=workspace_id,
        store_name=store_name,
        client=client,
        body=body,
        path=path,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadStorageFileBody,
    path: str | Unset = UNSET,
) -> Response[Error | StorageUpload]:
    """Upload a file

    Args:
        workspace_id (str):
        store_name (str):
        path (str | Unset):
        body (UploadStorageFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StorageUpload]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        body=body,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadStorageFileBody,
    path: str | Unset = UNSET,
) -> Error | StorageUpload | None:
    """Upload a file

    Args:
        workspace_id (str):
        store_name (str):
        path (str | Unset):
        body (UploadStorageFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StorageUpload
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            store_name=store_name,
            client=client,
            body=body,
            path=path,
        )
    ).parsed
