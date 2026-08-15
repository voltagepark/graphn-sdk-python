from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch import Batch
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    workflow_id: str,
    batch_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/{workflow_id}/batch/{batch_id}/cancel".format(
            workspace_id=quote(str(workspace_id), safe=""),
            workflow_id=quote(str(workflow_id), safe=""),
            batch_id=quote(str(batch_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Batch | Error | None:
    if response.status_code == 200:
        response_200 = Batch.from_dict(response.json())

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
) -> Response[Batch | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    workflow_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Batch | Error]:
    """Cancel a batch

    Args:
        workspace_id (str):
        workflow_id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Batch | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        batch_id=batch_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    workflow_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Batch | Error | None:
    """Cancel a batch

    Args:
        workspace_id (str):
        workflow_id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Batch | Error
    """

    return sync_detailed(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        batch_id=batch_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    workflow_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Batch | Error]:
    """Cancel a batch

    Args:
        workspace_id (str):
        workflow_id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Batch | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        workflow_id=workflow_id,
        batch_id=batch_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    workflow_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Batch | Error | None:
    """Cancel a batch

    Args:
        workspace_id (str):
        workflow_id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Batch | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            workflow_id=workflow_id,
            batch_id=batch_id,
            client=client,
        )
    ).parsed
