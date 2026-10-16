from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_invoice_preview_request import AdminInvoicePreviewRequest
from ...models.admin_invoice_preview_response import AdminInvoicePreviewResponse
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: str,
    *,
    body: AdminInvoicePreviewRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/admin/orgs/{org_id}/invoices/preview".format(
            org_id=quote(str(org_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminInvoicePreviewResponse | Any | Error | None:
    if response.status_code == 200:
        response_200 = AdminInvoicePreviewResponse.from_dict(response.json())

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
) -> Response[AdminInvoicePreviewResponse | Any | Error]:
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
    body: AdminInvoicePreviewRequest | Unset = UNSET,
) -> Response[AdminInvoicePreviewResponse | Any | Error]:
    """Preview invoiceable statement window and immutable manifest

    Args:
        org_id (str):
        body (AdminInvoicePreviewRequest | Unset): from and to must both be set or both omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminInvoicePreviewResponse | Any | Error]
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
    body: AdminInvoicePreviewRequest | Unset = UNSET,
) -> AdminInvoicePreviewResponse | Any | Error | None:
    """Preview invoiceable statement window and immutable manifest

    Args:
        org_id (str):
        body (AdminInvoicePreviewRequest | Unset): from and to must both be set or both omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminInvoicePreviewResponse | Any | Error
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
    body: AdminInvoicePreviewRequest | Unset = UNSET,
) -> Response[AdminInvoicePreviewResponse | Any | Error]:
    """Preview invoiceable statement window and immutable manifest

    Args:
        org_id (str):
        body (AdminInvoicePreviewRequest | Unset): from and to must both be set or both omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminInvoicePreviewResponse | Any | Error]
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
    body: AdminInvoicePreviewRequest | Unset = UNSET,
) -> AdminInvoicePreviewResponse | Any | Error | None:
    """Preview invoiceable statement window and immutable manifest

    Args:
        org_id (str):
        body (AdminInvoicePreviewRequest | Unset): from and to must both be set or both omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminInvoicePreviewResponse | Any | Error
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            body=body,
        )
    ).parsed
