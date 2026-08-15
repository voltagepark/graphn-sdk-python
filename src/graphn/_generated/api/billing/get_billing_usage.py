from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_usage import BillingUsage
from ...models.get_billing_usage_filter import GetBillingUsageFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: str,
    *,
    filter_: GetBillingUsageFilter | Unset = GetBillingUsageFilter.THIRTY_DAY,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{org_id}/billing/usage".format(
            org_id=quote(str(org_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BillingUsage | None:
    if response.status_code == 200:
        response_200 = BillingUsage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BillingUsage]:
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
    filter_: GetBillingUsageFilter | Unset = GetBillingUsageFilter.THIRTY_DAY,
) -> Response[BillingUsage]:
    """Get dollar-denominated usage over time

    Args:
        org_id (str):
        filter_ (GetBillingUsageFilter | Unset):  Default: GetBillingUsageFilter.THIRTY_DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingUsage]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: GetBillingUsageFilter | Unset = GetBillingUsageFilter.THIRTY_DAY,
) -> BillingUsage | None:
    """Get dollar-denominated usage over time

    Args:
        org_id (str):
        filter_ (GetBillingUsageFilter | Unset):  Default: GetBillingUsageFilter.THIRTY_DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingUsage
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: GetBillingUsageFilter | Unset = GetBillingUsageFilter.THIRTY_DAY,
) -> Response[BillingUsage]:
    """Get dollar-denominated usage over time

    Args:
        org_id (str):
        filter_ (GetBillingUsageFilter | Unset):  Default: GetBillingUsageFilter.THIRTY_DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingUsage]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: GetBillingUsageFilter | Unset = GetBillingUsageFilter.THIRTY_DAY,
) -> BillingUsage | None:
    """Get dollar-denominated usage over time

    Args:
        org_id (str):
        filter_ (GetBillingUsageFilter | Unset):  Default: GetBillingUsageFilter.THIRTY_DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingUsage
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            filter_=filter_,
        )
    ).parsed
