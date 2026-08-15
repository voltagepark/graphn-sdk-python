from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.execution import Execution
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    execution_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/executions/{execution_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            execution_id=quote(str(execution_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Execution | None:
    if response.status_code == 200:
        response_200 = Execution.from_dict(response.json())

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Execution]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Execution]:
    """Get an execution

     `exec_` and `test_` ids are served by the control plane. UUID operation ids from async/batch submit
    are served by the gateway. Generated clients that honor per-operation servers can pick either host;
    the official Python SDK routes by id prefix.

    Args:
        workspace_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Execution]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        execution_id=execution_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Execution | None:
    """Get an execution

     `exec_` and `test_` ids are served by the control plane. UUID operation ids from async/batch submit
    are served by the gateway. Generated clients that honor per-operation servers can pick either host;
    the official Python SDK routes by id prefix.

    Args:
        workspace_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Execution
    """

    return sync_detailed(
        workspace_id=workspace_id,
        execution_id=execution_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Execution]:
    """Get an execution

     `exec_` and `test_` ids are served by the control plane. UUID operation ids from async/batch submit
    are served by the gateway. Generated clients that honor per-operation servers can pick either host;
    the official Python SDK routes by id prefix.

    Args:
        workspace_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Execution]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        execution_id=execution_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Execution | None:
    """Get an execution

     `exec_` and `test_` ids are served by the control plane. UUID operation ids from async/batch submit
    are served by the gateway. Generated clients that honor per-operation servers can pick either host;
    the official Python SDK routes by id prefix.

    Args:
        workspace_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Execution
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            execution_id=execution_id,
            client=client,
        )
    ).parsed
