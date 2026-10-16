import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_inference_router_analytics_interval import (
    GetInferenceRouterAnalyticsInterval,
)
from ...models.inference_router_analytics import InferenceRouterAnalytics
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    router_id: str,
    *,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    interval: GetInferenceRouterAnalyticsInterval
    | Unset = GetInferenceRouterAnalyticsInterval.DAY,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_time = start_time.isoformat()
    params["start_time"] = json_start_time

    json_end_time = end_time.isoformat()
    params["end_time"] = json_end_time

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value

    params["interval"] = json_interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/inference-routers/{router_id}/analytics".format(
            workspace_id=quote(str(workspace_id), safe=""),
            router_id=quote(str(router_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InferenceRouterAnalytics | None:
    if response.status_code == 200:
        response_200 = InferenceRouterAnalytics.from_dict(response.json())

        return response_200

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
) -> Response[Error | InferenceRouterAnalytics]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    interval: GetInferenceRouterAnalyticsInterval
    | Unset = GetInferenceRouterAnalyticsInterval.DAY,
) -> Response[Error | InferenceRouterAnalytics]:
    """Get router usage analytics

     Available only when inference-router analytics is enabled for the deployment.

    Args:
        workspace_id (str):
        router_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        interval (GetInferenceRouterAnalyticsInterval | Unset):  Default:
            GetInferenceRouterAnalyticsInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouterAnalytics]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        router_id=router_id,
        start_time=start_time,
        end_time=end_time,
        interval=interval,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    interval: GetInferenceRouterAnalyticsInterval
    | Unset = GetInferenceRouterAnalyticsInterval.DAY,
) -> Error | InferenceRouterAnalytics | None:
    """Get router usage analytics

     Available only when inference-router analytics is enabled for the deployment.

    Args:
        workspace_id (str):
        router_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        interval (GetInferenceRouterAnalyticsInterval | Unset):  Default:
            GetInferenceRouterAnalyticsInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouterAnalytics
    """

    return sync_detailed(
        workspace_id=workspace_id,
        router_id=router_id,
        client=client,
        start_time=start_time,
        end_time=end_time,
        interval=interval,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    interval: GetInferenceRouterAnalyticsInterval
    | Unset = GetInferenceRouterAnalyticsInterval.DAY,
) -> Response[Error | InferenceRouterAnalytics]:
    """Get router usage analytics

     Available only when inference-router analytics is enabled for the deployment.

    Args:
        workspace_id (str):
        router_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        interval (GetInferenceRouterAnalyticsInterval | Unset):  Default:
            GetInferenceRouterAnalyticsInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouterAnalytics]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        router_id=router_id,
        start_time=start_time,
        end_time=end_time,
        interval=interval,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    interval: GetInferenceRouterAnalyticsInterval
    | Unset = GetInferenceRouterAnalyticsInterval.DAY,
) -> Error | InferenceRouterAnalytics | None:
    """Get router usage analytics

     Available only when inference-router analytics is enabled for the deployment.

    Args:
        workspace_id (str):
        router_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        interval (GetInferenceRouterAnalyticsInterval | Unset):  Default:
            GetInferenceRouterAnalyticsInterval.DAY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouterAnalytics
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            router_id=router_id,
            client=client,
            start_time=start_time,
            end_time=end_time,
            interval=interval,
        )
    ).parsed
