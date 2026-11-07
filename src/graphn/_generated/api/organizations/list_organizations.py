from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.organization_list import OrganizationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    continue_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["continue_token"] = continue_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | OrganizationList | None:
    if response.status_code == 200:
        response_200 = OrganizationList.from_dict(response.json())

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
) -> Response[Error | OrganizationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    continue_token: str | Unset = UNSET,
) -> Response[Error | OrganizationList]:
    """List organizations for the caller

     Returns the caller's organizations ordered by ID. When
    `continue_token` is present in the response, pass it back to fetch
    the next page.

    Args:
        limit (int | Unset):  Default: 100.
        continue_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OrganizationList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        continue_token=continue_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    continue_token: str | Unset = UNSET,
) -> Error | OrganizationList | None:
    """List organizations for the caller

     Returns the caller's organizations ordered by ID. When
    `continue_token` is present in the response, pass it back to fetch
    the next page.

    Args:
        limit (int | Unset):  Default: 100.
        continue_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OrganizationList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        continue_token=continue_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    continue_token: str | Unset = UNSET,
) -> Response[Error | OrganizationList]:
    """List organizations for the caller

     Returns the caller's organizations ordered by ID. When
    `continue_token` is present in the response, pass it back to fetch
    the next page.

    Args:
        limit (int | Unset):  Default: 100.
        continue_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OrganizationList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        continue_token=continue_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    continue_token: str | Unset = UNSET,
) -> Error | OrganizationList | None:
    """List organizations for the caller

     Returns the caller's organizations ordered by ID. When
    `continue_token` is present in the response, pass it back to fetch
    the next page.

    Args:
        limit (int | Unset):  Default: 100.
        continue_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OrganizationList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            continue_token=continue_token,
        )
    ).parsed
