from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_grant_result import BillingGrantResult
from ...models.billing_top_up_request import BillingTopUpRequest
from ...types import Response


def _get_kwargs(
    org_id: str,
    *,
    body: BillingTopUpRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{org_id}/billing/topups".format(
            org_id=quote(str(org_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BillingGrantResult | None:
    if response.status_code == 200:
        response_200 = BillingGrantResult.from_dict(response.json())

        return response_200

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 428:
        response_428 = cast(Any, None)
        return response_428

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BillingGrantResult]:
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
    body: BillingTopUpRequest,
) -> Response[Any | BillingGrantResult]:
    """Charge the saved payment method and add credits

    Args:
        org_id (str):
        body (BillingTopUpRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingGrantResult]
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
    body: BillingTopUpRequest,
) -> Any | BillingGrantResult | None:
    """Charge the saved payment method and add credits

    Args:
        org_id (str):
        body (BillingTopUpRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingGrantResult
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
    body: BillingTopUpRequest,
) -> Response[Any | BillingGrantResult]:
    """Charge the saved payment method and add credits

    Args:
        org_id (str):
        body (BillingTopUpRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingGrantResult]
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
    body: BillingTopUpRequest,
) -> Any | BillingGrantResult | None:
    """Charge the saved payment method and add credits

    Args:
        org_id (str):
        body (BillingTopUpRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingGrantResult
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            body=body,
        )
    ).parsed
