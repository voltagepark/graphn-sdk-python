from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_invoices_response import AdminInvoicesResponse
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: str,
    *,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/orgs/{org_id}/invoices".format(
            org_id=quote(str(org_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminInvoicesResponse | Any | Error | None:
    if response.status_code == 200:
        response_200 = AdminInvoicesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdminInvoicesResponse | Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> Response[AdminInvoicesResponse | Any | Error]:
    """List immutable billing statements for an organization

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminInvoicesResponse | Any | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> AdminInvoicesResponse | Any | Error | None:
    """List immutable billing statements for an organization

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminInvoicesResponse | Any | Error
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> Response[AdminInvoicesResponse | Any | Error]:
    """List immutable billing statements for an organization

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminInvoicesResponse | Any | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> AdminInvoicesResponse | Any | Error | None:
    """List immutable billing statements for an organization

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminInvoicesResponse | Any | Error
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            limit=limit,
        )
    ).parsed
