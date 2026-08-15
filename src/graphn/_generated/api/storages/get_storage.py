from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.storage import Storage
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    store_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/storages/{store_name}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            store_name=quote(str(store_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Storage | None:
    if response.status_code == 200:
        response_200 = Storage.from_dict(response.json())

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
) -> Response[Error | Storage]:
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
) -> Response[Error | Storage]:
    """Get an object store

    Args:
        workspace_id (str):
        store_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Storage]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
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
) -> Error | Storage | None:
    """Get an object store

    Args:
        workspace_id (str):
        store_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Storage
    """

    return sync_detailed(
        workspace_id=workspace_id,
        store_name=store_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Storage]:
    """Get an object store

    Args:
        workspace_id (str):
        store_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Storage]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Storage | None:
    """Get an object store

    Args:
        workspace_id (str):
        store_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Storage
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            store_name=store_name,
            client=client,
        )
    ).parsed
