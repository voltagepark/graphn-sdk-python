from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.gpu_hours_response import GpuHoursResponse
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    model_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/custom-models/{model_id}/gpu-hours".format(
            workspace_id=quote(str(workspace_id), safe=""),
            model_id=quote(str(model_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GpuHoursResponse | None:
    if response.status_code == 200:
        response_200 = GpuHoursResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GpuHoursResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GpuHoursResponse]:
    """Get cumulative GPU-hours billed for a custom model

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GpuHoursResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        model_id=model_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | GpuHoursResponse | None:
    """Get cumulative GPU-hours billed for a custom model

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GpuHoursResponse
    """

    return sync_detailed(
        workspace_id=workspace_id,
        model_id=model_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GpuHoursResponse]:
    """Get cumulative GPU-hours billed for a custom model

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GpuHoursResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        model_id=model_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | GpuHoursResponse | None:
    """Get cumulative GPU-hours billed for a custom model

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GpuHoursResponse
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            model_id=model_id,
            client=client,
        )
    ).parsed
