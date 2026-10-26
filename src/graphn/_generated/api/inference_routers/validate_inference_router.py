from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.inference_router_validation import InferenceRouterValidation
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    router_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/inference-routers/{router_id}/validate".format(
            workspace_id=quote(str(workspace_id), safe=""),
            router_id=quote(str(router_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InferenceRouterValidation | None:
    if response.status_code == 200:
        response_200 = InferenceRouterValidation.from_dict(response.json())

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
) -> Response[Error | InferenceRouterValidation]:
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
) -> Response[Error | InferenceRouterValidation]:
    """Validate the current draft and derive its target manifest

    Args:
        workspace_id (str):
        router_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouterValidation]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        router_id=router_id,
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
) -> Error | InferenceRouterValidation | None:
    """Validate the current draft and derive its target manifest

    Args:
        workspace_id (str):
        router_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouterValidation
    """

    return sync_detailed(
        workspace_id=workspace_id,
        router_id=router_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | InferenceRouterValidation]:
    """Validate the current draft and derive its target manifest

    Args:
        workspace_id (str):
        router_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouterValidation]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        router_id=router_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | InferenceRouterValidation | None:
    """Validate the current draft and derive its target manifest

    Args:
        workspace_id (str):
        router_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouterValidation
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            router_id=router_id,
            client=client,
        )
    ).parsed
