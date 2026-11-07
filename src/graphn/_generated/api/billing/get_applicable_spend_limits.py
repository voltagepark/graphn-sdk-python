from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.applicable_spend_limits_response import ApplicableSpendLimitsResponse
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: str,
    *,
    workspace_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{org_id}/billing/spend-limits/applicable".format(
            org_id=quote(str(org_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApplicableSpendLimitsResponse | Error | None:
    if response.status_code == 200:
        response_200 = ApplicableSpendLimitsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApplicableSpendLimitsResponse | Error]:
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
    workspace_id: str | Unset = UNSET,
) -> Response[ApplicableSpendLimitsResponse | Error]:
    """Get spend limits applicable to the authenticated user

     Returns the caller's user limit status and, when workspaceId is provided and authorized, that
    workspace's limit status.

    Args:
        org_id (str):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicableSpendLimitsResponse | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    workspace_id: str | Unset = UNSET,
) -> ApplicableSpendLimitsResponse | Error | None:
    """Get spend limits applicable to the authenticated user

     Returns the caller's user limit status and, when workspaceId is provided and authorized, that
    workspace's limit status.

    Args:
        org_id (str):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicableSpendLimitsResponse | Error
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    workspace_id: str | Unset = UNSET,
) -> Response[ApplicableSpendLimitsResponse | Error]:
    """Get spend limits applicable to the authenticated user

     Returns the caller's user limit status and, when workspaceId is provided and authorized, that
    workspace's limit status.

    Args:
        org_id (str):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicableSpendLimitsResponse | Error]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient | Client,
    workspace_id: str | Unset = UNSET,
) -> ApplicableSpendLimitsResponse | Error | None:
    """Get spend limits applicable to the authenticated user

     Returns the caller's user limit status and, when workspaceId is provided and authorized, that
    workspace's limit status.

    Args:
        org_id (str):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicableSpendLimitsResponse | Error
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
