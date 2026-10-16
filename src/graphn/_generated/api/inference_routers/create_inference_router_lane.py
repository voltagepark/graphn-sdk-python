from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.inference_router_lane import InferenceRouterLane
from ...models.inference_router_lane_create import InferenceRouterLaneCreate
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    *,
    body: InferenceRouterLaneCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/inference-router-lanes".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InferenceRouterLane | None:
    if response.status_code == 201:
        response_201 = InferenceRouterLane.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | InferenceRouterLane]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InferenceRouterLaneCreate,
) -> Response[Error | InferenceRouterLane]:
    """Create a workspace custom router lane

     A custom lane is a list of literal phrases, matched case-insensitively on word boundaries.
    Candidates in this workspace's routers reference it as `custom:<id>`. Lanes are visible only inside
    their own workspace.

    Args:
        workspace_id (str):
        body (InferenceRouterLaneCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouterLane]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InferenceRouterLaneCreate,
) -> Error | InferenceRouterLane | None:
    """Create a workspace custom router lane

     A custom lane is a list of literal phrases, matched case-insensitively on word boundaries.
    Candidates in this workspace's routers reference it as `custom:<id>`. Lanes are visible only inside
    their own workspace.

    Args:
        workspace_id (str):
        body (InferenceRouterLaneCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouterLane
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InferenceRouterLaneCreate,
) -> Response[Error | InferenceRouterLane]:
    """Create a workspace custom router lane

     A custom lane is a list of literal phrases, matched case-insensitively on word boundaries.
    Candidates in this workspace's routers reference it as `custom:<id>`. Lanes are visible only inside
    their own workspace.

    Args:
        workspace_id (str):
        body (InferenceRouterLaneCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouterLane]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InferenceRouterLaneCreate,
) -> Error | InferenceRouterLane | None:
    """Create a workspace custom router lane

     A custom lane is a list of literal phrases, matched case-insensitively on word boundaries.
    Candidates in this workspace's routers reference it as `custom:<id>`. Lanes are visible only inside
    their own workspace.

    Args:
        workspace_id (str):
        body (InferenceRouterLaneCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouterLane
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
