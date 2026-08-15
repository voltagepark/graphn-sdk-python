from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.workflow import Workflow
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    workflow_id: str,
    version_number: int,
    *,
    restore_resources: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["restore_resources"] = restore_resources

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/workflows/{workflow_id}/restore/{version_number}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            workflow_id=quote(str(workflow_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Workflow | None:
    if response.status_code == 200:
        response_200 = Workflow.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Workflow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    workflow_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    restore_resources: str | Unset = UNSET,
) -> Response[Error | Workflow]:
    """Restore a workflow version into draft

    Args:
        workspace_id (str):
        workflow_id (str):
        version_number (int):
        restore_resources (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Workflow]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        version_number=version_number,
        restore_resources=restore_resources,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    workflow_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    restore_resources: str | Unset = UNSET,
) -> Error | Workflow | None:
    """Restore a workflow version into draft

    Args:
        workspace_id (str):
        workflow_id (str):
        version_number (int):
        restore_resources (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Workflow
    """

    return sync_detailed(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        version_number=version_number,
        client=client,
        restore_resources=restore_resources,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    workflow_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    restore_resources: str | Unset = UNSET,
) -> Response[Error | Workflow]:
    """Restore a workflow version into draft

    Args:
        workspace_id (str):
        workflow_id (str):
        version_number (int):
        restore_resources (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Workflow]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        version_number=version_number,
        restore_resources=restore_resources,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    workflow_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    restore_resources: str | Unset = UNSET,
) -> Error | Workflow | None:
    """Restore a workflow version into draft

    Args:
        workspace_id (str):
        workflow_id (str):
        version_number (int):
        restore_resources (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Workflow
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            workflow_id=workflow_id,
            version_number=version_number,
            client=client,
            restore_resources=restore_resources,
        )
    ).parsed
