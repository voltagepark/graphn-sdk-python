from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    store_name: str,
    *,
    purge: bool | Unset = UNSET,
    hard_delete: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["purge"] = purge

    params["hard_delete"] = hard_delete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/{workspace_id}/storages/{store_name}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            store_name=quote(str(store_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | Error]:
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
    purge: bool | Unset = UNSET,
    hard_delete: bool | Unset = UNSET,
) -> Response[Any | Error]:
    """Delete an object store

    Args:
        workspace_id (str):
        store_name (str):
        purge (bool | Unset):
        hard_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        purge=purge,
        hard_delete=hard_delete,
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
    purge: bool | Unset = UNSET,
    hard_delete: bool | Unset = UNSET,
) -> Any | Error | None:
    """Delete an object store

    Args:
        workspace_id (str):
        store_name (str):
        purge (bool | Unset):
        hard_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace_id=workspace_id,
        store_name=store_name,
        client=client,
        purge=purge,
        hard_delete=hard_delete,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    purge: bool | Unset = UNSET,
    hard_delete: bool | Unset = UNSET,
) -> Response[Any | Error]:
    """Delete an object store

    Args:
        workspace_id (str):
        store_name (str):
        purge (bool | Unset):
        hard_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        store_name=store_name,
        purge=purge,
        hard_delete=hard_delete,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    store_name: str,
    *,
    client: AuthenticatedClient | Client,
    purge: bool | Unset = UNSET,
    hard_delete: bool | Unset = UNSET,
) -> Any | Error | None:
    """Delete an object store

    Args:
        workspace_id (str):
        store_name (str):
        purge (bool | Unset):
        hard_delete (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            store_name=store_name,
            client=client,
            purge=purge,
            hard_delete=hard_delete,
        )
    ).parsed
