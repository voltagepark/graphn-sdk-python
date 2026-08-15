from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.storage_file_list import StorageFileList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    store_name: str,
    *,
    prefix: str | Unset = UNSET,
    delimiter: str | Unset = UNSET,
    max_keys: int | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["prefix"] = prefix

    params["delimiter"] = delimiter

    params["max_keys"] = max_keys

    params["continuation_token"] = continuation_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/storages/{store_name}/files".format(
            workspace_id=quote(str(workspace_id), safe=""),
            store_name=quote(str(store_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | StorageFileList | None:
    if response.status_code == 200:
        response_200 = StorageFileList.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | StorageFileList]:
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
    prefix: str | Unset = UNSET,
    delimiter: str | Unset = UNSET,
    max_keys: int | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
) -> Response[Error | StorageFileList]:
    """List files in an object store

    Args:
        workspace_id (str):
        store_name (str):
        prefix (str | Unset):
        delimiter (str | Unset):
        max_keys (int | Unset):
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StorageFileList]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        prefix=prefix,
        delimiter=delimiter,
        max_keys=max_keys,
        continuation_token=continuation_token,
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
    prefix: str | Unset = UNSET,
    delimiter: str | Unset = UNSET,
    max_keys: int | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
) -> Error | StorageFileList | None:
    """List files in an object store

    Args:
        workspace_id (str):
        store_name (str):
        prefix (str | Unset):
        delimiter (str | Unset):
        max_keys (int | Unset):
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StorageFileList
    """

    return sync_detailed(
        workspace_id=workspace_id,
        store_name=store_name,
        client=client,
        prefix=prefix,
        delimiter=delimiter,
        max_keys=max_keys,
        continuation_token=continuation_token,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    prefix: str | Unset = UNSET,
    delimiter: str | Unset = UNSET,
    max_keys: int | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
) -> Response[Error | StorageFileList]:
    """List files in an object store

    Args:
        workspace_id (str):
        store_name (str):
        prefix (str | Unset):
        delimiter (str | Unset):
        max_keys (int | Unset):
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StorageFileList]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        prefix=prefix,
        delimiter=delimiter,
        max_keys=max_keys,
        continuation_token=continuation_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    prefix: str | Unset = UNSET,
    delimiter: str | Unset = UNSET,
    max_keys: int | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
) -> Error | StorageFileList | None:
    """List files in an object store

    Args:
        workspace_id (str):
        store_name (str):
        prefix (str | Unset):
        delimiter (str | Unset):
        max_keys (int | Unset):
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StorageFileList
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            store_name=store_name,
            client=client,
            prefix=prefix,
            delimiter=delimiter,
            max_keys=max_keys,
            continuation_token=continuation_token,
        )
    ).parsed
