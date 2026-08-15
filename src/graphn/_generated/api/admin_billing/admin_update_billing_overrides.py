from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_billing_overrides import AdminBillingOverrides
from ...models.admin_billing_state import AdminBillingState
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    org_id: str,
    *,
    body: AdminBillingOverrides,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/admin/orgs/{org_id}/billing/overrides".format(
            org_id=quote(str(org_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminBillingState | Any | Error | None:
    if response.status_code == 200:
        response_200 = AdminBillingState.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdminBillingState | Any | Error]:
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
    body: AdminBillingOverrides,
) -> Response[AdminBillingState | Any | Error]:
    """Update administrative billing overrides

    Args:
        org_id (str):
        body (AdminBillingOverrides):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminBillingState | Any | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminBillingOverrides,
) -> AdminBillingState | Any | Error | None:
    """Update administrative billing overrides

    Args:
        org_id (str):
        body (AdminBillingOverrides):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminBillingState | Any | Error
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminBillingOverrides,
) -> Response[AdminBillingState | Any | Error]:
    """Update administrative billing overrides

    Args:
        org_id (str):
        body (AdminBillingOverrides):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminBillingState | Any | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminBillingOverrides,
) -> AdminBillingState | Any | Error | None:
    """Update administrative billing overrides

    Args:
        org_id (str):
        body (AdminBillingOverrides):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminBillingState | Any | Error
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            body=body,
        )
    ).parsed
