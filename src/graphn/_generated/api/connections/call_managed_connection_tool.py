from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.managed_connection_tool_call import ManagedConnectionToolCall
from ...models.managed_connection_tool_result import ManagedConnectionToolResult
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    connection_id: str,
    tool_name: str,
    *,
    body: ManagedConnectionToolCall,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/internal/workspaces/{workspace_id}/connections/{connection_id}/tools/{tool_name}/call".format(
            workspace_id=quote(str(workspace_id), safe=""),
            connection_id=quote(str(connection_id), safe=""),
            tool_name=quote(str(tool_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ManagedConnectionToolResult | None:
    if response.status_code == 200:
        response_200 = ManagedConnectionToolResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ManagedConnectionToolResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    connection_id: str,
    tool_name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedConnectionToolCall,
) -> Response[Error | ManagedConnectionToolResult]:
    """Invoke a GraphN-managed MCP tool

     Internal service-to-service endpoint used by Agent Foundry.

    Args:
        workspace_id (str):
        connection_id (str):
        tool_name (str):
        body (ManagedConnectionToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ManagedConnectionToolResult]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        connection_id=connection_id,
        tool_name=tool_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    connection_id: str,
    tool_name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedConnectionToolCall,
) -> Error | ManagedConnectionToolResult | None:
    """Invoke a GraphN-managed MCP tool

     Internal service-to-service endpoint used by Agent Foundry.

    Args:
        workspace_id (str):
        connection_id (str):
        tool_name (str):
        body (ManagedConnectionToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ManagedConnectionToolResult
    """

    return sync_detailed(
        workspace_id=workspace_id,
        connection_id=connection_id,
        tool_name=tool_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    connection_id: str,
    tool_name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedConnectionToolCall,
) -> Response[Error | ManagedConnectionToolResult]:
    """Invoke a GraphN-managed MCP tool

     Internal service-to-service endpoint used by Agent Foundry.

    Args:
        workspace_id (str):
        connection_id (str):
        tool_name (str):
        body (ManagedConnectionToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ManagedConnectionToolResult]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        connection_id=connection_id,
        tool_name=tool_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    connection_id: str,
    tool_name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedConnectionToolCall,
) -> Error | ManagedConnectionToolResult | None:
    """Invoke a GraphN-managed MCP tool

     Internal service-to-service endpoint used by Agent Foundry.

    Args:
        workspace_id (str):
        connection_id (str):
        tool_name (str):
        body (ManagedConnectionToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ManagedConnectionToolResult
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            connection_id=connection_id,
            tool_name=tool_name,
            client=client,
            body=body,
        )
    ).parsed
