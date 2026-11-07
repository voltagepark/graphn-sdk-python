from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_grant_result import BillingGrantResult
from ...models.billing_top_up_charge_request import BillingTopUpChargeRequest
from ...models.billing_top_up_probe_request import BillingTopUpProbeRequest
from ...models.billing_top_up_probe_result import BillingTopUpProbeResult
from ...types import Response


def _get_kwargs(
    org_id: str,
    *,
    body: BillingTopUpChargeRequest | BillingTopUpProbeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{org_id}/billing/topups".format(
            org_id=quote(str(org_id), safe=""),
        ),
    }

    if isinstance(body, BillingTopUpChargeRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BillingGrantResult | BillingTopUpProbeResult | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> BillingGrantResult | BillingTopUpProbeResult:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = BillingGrantResult.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = BillingTopUpProbeResult.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402

    if response.status_code == 412:
        response_412 = cast(Any, None)
        return response_412

    if response.status_code == 428:
        response_428 = cast(Any, None)
        return response_428

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BillingGrantResult | BillingTopUpProbeResult]:
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
    body: BillingTopUpChargeRequest | BillingTopUpProbeRequest,
) -> Response[Any | BillingGrantResult | BillingTopUpProbeResult]:
    """Charge the saved payment method or probe that a charge can be made

    Args:
        org_id (str):
        body (BillingTopUpChargeRequest | BillingTopUpProbeRequest): A charge requires amountCents
            and idempotencyKey. A probe sends probeOnly true and does not charge or grant credits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingGrantResult | BillingTopUpProbeResult]
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
    body: BillingTopUpChargeRequest | BillingTopUpProbeRequest,
) -> Any | BillingGrantResult | BillingTopUpProbeResult | None:
    """Charge the saved payment method or probe that a charge can be made

    Args:
        org_id (str):
        body (BillingTopUpChargeRequest | BillingTopUpProbeRequest): A charge requires amountCents
            and idempotencyKey. A probe sends probeOnly true and does not charge or grant credits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingGrantResult | BillingTopUpProbeResult
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
    body: BillingTopUpChargeRequest | BillingTopUpProbeRequest,
) -> Response[Any | BillingGrantResult | BillingTopUpProbeResult]:
    """Charge the saved payment method or probe that a charge can be made

    Args:
        org_id (str):
        body (BillingTopUpChargeRequest | BillingTopUpProbeRequest): A charge requires amountCents
            and idempotencyKey. A probe sends probeOnly true and does not charge or grant credits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BillingGrantResult | BillingTopUpProbeResult]
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
    body: BillingTopUpChargeRequest | BillingTopUpProbeRequest,
) -> Any | BillingGrantResult | BillingTopUpProbeResult | None:
    """Charge the saved payment method or probe that a charge can be made

    Args:
        org_id (str):
        body (BillingTopUpChargeRequest | BillingTopUpProbeRequest): A charge requires amountCents
            and idempotencyKey. A probe sends probeOnly true and does not charge or grant credits.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BillingGrantResult | BillingTopUpProbeResult
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            body=body,
        )
    ).parsed
