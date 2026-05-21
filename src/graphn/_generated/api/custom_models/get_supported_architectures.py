from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.supported_architectures import SupportedArchitectures
from ...types import Response


def _get_kwargs(
    workspace_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/custom-models/supported-architectures".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SupportedArchitectures | None:
    if response.status_code == 200:
        response_200 = SupportedArchitectures.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SupportedArchitectures]:
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
) -> Response[Error | SupportedArchitectures]:
    """List model architectures supported for custom-model import

     Returns the static list of HuggingFace model architectures the
    platform's serving runtimes can deploy, alongside the capability
    tags (`tool_calling`, `vision`, etc.) each architecture exposes.
    Use this to drive the UI's architecture/capability filters before
    calling `validateCustomModel`.

    The list is updated alongside platform runtime upgrades; clients
    should not cache it for more than a build cycle.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SupportedArchitectures]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | SupportedArchitectures | None:
    """List model architectures supported for custom-model import

     Returns the static list of HuggingFace model architectures the
    platform's serving runtimes can deploy, alongside the capability
    tags (`tool_calling`, `vision`, etc.) each architecture exposes.
    Use this to drive the UI's architecture/capability filters before
    calling `validateCustomModel`.

    The list is updated alongside platform runtime upgrades; clients
    should not cache it for more than a build cycle.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SupportedArchitectures
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | SupportedArchitectures]:
    """List model architectures supported for custom-model import

     Returns the static list of HuggingFace model architectures the
    platform's serving runtimes can deploy, alongside the capability
    tags (`tool_calling`, `vision`, etc.) each architecture exposes.
    Use this to drive the UI's architecture/capability filters before
    calling `validateCustomModel`.

    The list is updated alongside platform runtime upgrades; clients
    should not cache it for more than a build cycle.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SupportedArchitectures]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | SupportedArchitectures | None:
    """List model architectures supported for custom-model import

     Returns the static list of HuggingFace model architectures the
    platform's serving runtimes can deploy, alongside the capability
    tags (`tool_calling`, `vision`, etc.) each architecture exposes.
    Use this to drive the UI's architecture/capability filters before
    calling `validateCustomModel`.

    The list is updated alongside platform runtime upgrades; clients
    should not cache it for more than a build cycle.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SupportedArchitectures
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
        )
    ).parsed
