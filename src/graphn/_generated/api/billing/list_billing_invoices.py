from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_billing_invoices_response_200 import ListBillingInvoicesResponse200
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
        "url": "/v1/{org_id}/billing/invoices".format(
            org_id=quote(str(org_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListBillingInvoicesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListBillingInvoicesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListBillingInvoicesResponse200]:
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
) -> Response[ListBillingInvoicesResponse200]:
    """List billing statements

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListBillingInvoicesResponse200]
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
) -> ListBillingInvoicesResponse200 | None:
    """List billing statements

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListBillingInvoicesResponse200
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
) -> Response[ListBillingInvoicesResponse200]:
    """List billing statements

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListBillingInvoicesResponse200]
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
) -> ListBillingInvoicesResponse200 | None:
    """List billing statements

    Args:
        org_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListBillingInvoicesResponse200
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            limit=limit,
        )
    ).parsed
