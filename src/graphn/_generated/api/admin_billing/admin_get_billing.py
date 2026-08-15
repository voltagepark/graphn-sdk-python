from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_billing_state import AdminBillingState
from ...types import Response


def _get_kwargs(
    org_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/orgs/{org_id}/billing".format(
            org_id=quote(str(org_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminBillingState | Any | None:
    if response.status_code == 200:
        response_200 = AdminBillingState.from_dict(response.json())

        return response_200

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdminBillingState | Any]:
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
) -> Response[AdminBillingState | Any]:
    """Get combined admin billing state

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminBillingState | Any]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AdminBillingState | Any | None:
    """Get combined admin billing state

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminBillingState | Any
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AdminBillingState | Any]:
    """Get combined admin billing state

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminBillingState | Any]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AdminBillingState | Any | None:
    """Get combined admin billing state

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminBillingState | Any
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
        )
    ).parsed
