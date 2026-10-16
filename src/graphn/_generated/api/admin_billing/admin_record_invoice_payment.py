from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_invoice_record_payment_request import (
    AdminInvoiceRecordPaymentRequest,
)
from ...models.admin_invoice_record_payment_response import (
    AdminInvoiceRecordPaymentResponse,
)
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    org_id: str,
    invoice_id: str,
    *,
    body: AdminInvoiceRecordPaymentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/admin/orgs/{org_id}/invoices/{invoice_id}/record-payment".format(
            org_id=quote(str(org_id), safe=""),
            invoice_id=quote(str(invoice_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminInvoiceRecordPaymentResponse | Any | Error | None:
    if response.status_code == 200:
        response_200 = AdminInvoiceRecordPaymentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

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
) -> Response[AdminInvoiceRecordPaymentResponse | Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminInvoiceRecordPaymentRequest,
) -> Response[AdminInvoiceRecordPaymentResponse | Any | Error]:
    """Append a paid-invoice journal payment record

    Args:
        org_id (str):
        invoice_id (str):
        body (AdminInvoiceRecordPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminInvoiceRecordPaymentResponse | Any | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        invoice_id=invoice_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminInvoiceRecordPaymentRequest,
) -> AdminInvoiceRecordPaymentResponse | Any | Error | None:
    """Append a paid-invoice journal payment record

    Args:
        org_id (str):
        invoice_id (str):
        body (AdminInvoiceRecordPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminInvoiceRecordPaymentResponse | Any | Error
    """

    return sync_detailed(
        org_id=org_id,
        invoice_id=invoice_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminInvoiceRecordPaymentRequest,
) -> Response[AdminInvoiceRecordPaymentResponse | Any | Error]:
    """Append a paid-invoice journal payment record

    Args:
        org_id (str):
        invoice_id (str):
        body (AdminInvoiceRecordPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminInvoiceRecordPaymentResponse | Any | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        invoice_id=invoice_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminInvoiceRecordPaymentRequest,
) -> AdminInvoiceRecordPaymentResponse | Any | Error | None:
    """Append a paid-invoice journal payment record

    Args:
        org_id (str):
        invoice_id (str):
        body (AdminInvoiceRecordPaymentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminInvoiceRecordPaymentResponse | Any | Error
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
