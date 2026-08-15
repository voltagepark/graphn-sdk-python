from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blueprint import Blueprint
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    blueprint_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/blueprints/{blueprint_id}".format(
            blueprint_id=quote(str(blueprint_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Blueprint | Error | None:
    if response.status_code == 200:
        response_200 = Blueprint.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Blueprint | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Blueprint | Error]:
    """Get a blueprint

    Args:
        blueprint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Blueprint | Error]
    """

    kwargs = _get_kwargs(
        blueprint_id=blueprint_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Blueprint | Error | None:
    """Get a blueprint

    Args:
        blueprint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Blueprint | Error
    """

    return sync_detailed(
        blueprint_id=blueprint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Blueprint | Error]:
    """Get a blueprint

    Args:
        blueprint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Blueprint | Error]
    """

    kwargs = _get_kwargs(
        blueprint_id=blueprint_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Blueprint | Error | None:
    """Get a blueprint

    Args:
        blueprint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Blueprint | Error
    """

    return (
        await asyncio_detailed(
            blueprint_id=blueprint_id,
            client=client,
        )
    ).parsed
