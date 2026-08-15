from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_billing_invoice_response_200 import GetBillingInvoiceResponse200
from ...types import Response


def _get_kwargs(
    org_id: str,
    period_start: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{org_id}/billing/invoices/{period_start}".format(
            org_id=quote(str(org_id), safe=""),
            period_start=quote(str(period_start), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBillingInvoiceResponse200 | None:
    if response.status_code == 200:
        response_200 = GetBillingInvoiceResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBillingInvoiceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    period_start: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBillingInvoiceResponse200]:
    """Get billing statement detail

    Args:
        org_id (str):
        period_start (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingInvoiceResponse200]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        period_start=period_start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    period_start: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetBillingInvoiceResponse200 | None:
    """Get billing statement detail

    Args:
        org_id (str):
        period_start (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingInvoiceResponse200
    """

    return sync_detailed(
        org_id=org_id,
        period_start=period_start,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    period_start: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetBillingInvoiceResponse200]:
    """Get billing statement detail

    Args:
        org_id (str):
        period_start (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingInvoiceResponse200]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        period_start=period_start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    period_start: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetBillingInvoiceResponse200 | None:
    """Get billing statement detail

    Args:
        org_id (str):
        period_start (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingInvoiceResponse200
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            period_start=period_start,
            client=client,
        )
    ).parsed
