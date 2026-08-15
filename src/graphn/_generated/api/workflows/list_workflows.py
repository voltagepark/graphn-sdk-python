from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.workflow_list import WorkflowList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    limit: int | Unset = 50,
    continue_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["continue_token"] = continue_token

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/workflows".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WorkflowList | None:
    if response.status_code == 200:
        response_200 = WorkflowList.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | WorkflowList]:
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
    limit: int | Unset = 50,
    continue_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Response[Error | WorkflowList]:
    """List workflows

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        continue_token (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkflowList]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        limit=limit,
        continue_token=continue_token,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    continue_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Error | WorkflowList | None:
    """List workflows

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        continue_token (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkflowList
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        limit=limit,
        continue_token=continue_token,
        status=status,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    continue_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Response[Error | WorkflowList]:
    """List workflows

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        continue_token (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WorkflowList]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        limit=limit,
        continue_token=continue_token,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    continue_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
) -> Error | WorkflowList | None:
    """List workflows

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        continue_token (str | Unset):
        status (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WorkflowList
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            limit=limit,
            continue_token=continue_token,
            status=status,
        )
    ).parsed
