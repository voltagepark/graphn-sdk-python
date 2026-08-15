from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.presigned_url import PresignedURL
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    store_name: str,
    file_key: str,
    *,
    expires_in: int | Unset = UNSET,
    upload: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["expires_in"] = expires_in

    params["upload"] = upload

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/storages/{store_name}/files/{file_key}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            store_name=quote(str(store_name), safe=""),
            file_key=quote(str(file_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PresignedURL | None:
    if response.status_code == 200:
        response_200 = PresignedURL.from_dict(response.json())

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PresignedURL]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    store_name: str,
    file_key: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
    upload: bool | Unset = UNSET,
) -> Response[Error | PresignedURL]:
    """Mint a presigned URL for a file

     The path must end with `/presign` in the live API (`.../files/{key}/presign`). Documented here as
    POST on the file with `presign` semantics.

    Args:
        workspace_id (str):
        store_name (str):
        file_key (str):
        expires_in (int | Unset):
        upload (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PresignedURL]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        file_key=file_key,
        expires_in=expires_in,
        upload=upload,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    store_name: str,
    file_key: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
    upload: bool | Unset = UNSET,
) -> Error | PresignedURL | None:
    """Mint a presigned URL for a file

     The path must end with `/presign` in the live API (`.../files/{key}/presign`). Documented here as
    POST on the file with `presign` semantics.

    Args:
        workspace_id (str):
        store_name (str):
        file_key (str):
        expires_in (int | Unset):
        upload (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PresignedURL
    """

    return sync_detailed(
        workspace_id=workspace_id,
        store_name=store_name,
        file_key=file_key,
        client=client,
        expires_in=expires_in,
        upload=upload,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    store_name: str,
    file_key: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
    upload: bool | Unset = UNSET,
) -> Response[Error | PresignedURL]:
    """Mint a presigned URL for a file

     The path must end with `/presign` in the live API (`.../files/{key}/presign`). Documented here as
    POST on the file with `presign` semantics.

    Args:
        workspace_id (str):
        store_name (str):
        file_key (str):
        expires_in (int | Unset):
        upload (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PresignedURL]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        file_key=file_key,
        expires_in=expires_in,
        upload=upload,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    store_name: str,
    file_key: str,
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
    upload: bool | Unset = UNSET,
) -> Error | PresignedURL | None:
    """Mint a presigned URL for a file

     The path must end with `/presign` in the live API (`.../files/{key}/presign`). Documented here as
    POST on the file with `presign` semantics.

    Args:
        workspace_id (str):
        store_name (str):
        file_key (str):
        expires_in (int | Unset):
        upload (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PresignedURL
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            store_name=store_name,
            file_key=file_key,
            client=client,
            expires_in=expires_in,
            upload=upload,
        )
    ).parsed
