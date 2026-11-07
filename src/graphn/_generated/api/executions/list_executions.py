from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_executions_status import ListExecutionsStatus
from ...models.opaque_object import OpaqueObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    workflow_id: str | Unset = UNSET,
    status: ListExecutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workflow_id"] = workflow_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/executions".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | OpaqueObject | None:
    if response.status_code == 200:
        response_200 = OpaqueObject.from_dict(response.json())

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | OpaqueObject]:
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
    workflow_id: str | Unset = UNSET,
    status: ListExecutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Error | OpaqueObject]:
    """List executions, newest first

     Lists executions in the workspace. `workflow_id` is optional: omit it to
    list every workflow's executions. Results are paginated with `page` and
    `limit` (AF caps page size at 100).

    Args:
        workspace_id (str):
        workflow_id (str | Unset):
        status (ListExecutionsStatus | Unset):
        limit (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OpaqueObject]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        status=status,
        limit=limit,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    status: ListExecutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Error | OpaqueObject | None:
    """List executions, newest first

     Lists executions in the workspace. `workflow_id` is optional: omit it to
    list every workflow's executions. Results are paginated with `page` and
    `limit` (AF caps page size at 100).

    Args:
        workspace_id (str):
        workflow_id (str | Unset):
        status (ListExecutionsStatus | Unset):
        limit (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OpaqueObject
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        workflow_id=workflow_id,
        status=status,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    status: ListExecutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Error | OpaqueObject]:
    """List executions, newest first

     Lists executions in the workspace. `workflow_id` is optional: omit it to
    list every workflow's executions. Results are paginated with `page` and
    `limit` (AF caps page size at 100).

    Args:
        workspace_id (str):
        workflow_id (str | Unset):
        status (ListExecutionsStatus | Unset):
        limit (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OpaqueObject]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        status=status,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    status: ListExecutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Error | OpaqueObject | None:
    """List executions, newest first

     Lists executions in the workspace. `workflow_id` is optional: omit it to
    list every workflow's executions. Results are paginated with `page` and
    `limit` (AF caps page size at 100).

    Args:
        workspace_id (str):
        workflow_id (str | Unset):
        status (ListExecutionsStatus | Unset):
        limit (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OpaqueObject
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            workflow_id=workflow_id,
            status=status,
            limit=limit,
            page=page,
        )
    ).parsed
