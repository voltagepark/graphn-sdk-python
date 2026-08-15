from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.ingest_job import IngestJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    kb_id: str,
    job_id: str,
    *,
    include_items: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/knowledgebases/{kb_id}/ingest/{job_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            kb_id=quote(str(kb_id), safe=""),
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | IngestJob | None:
    if response.status_code == 200:
        response_200 = IngestJob.from_dict(response.json())

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
) -> Response[Error | IngestJob]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    kb_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_items: bool | Unset = UNSET,
) -> Response[Error | IngestJob]:
    """Get an ingest job

    Args:
        workspace_id (str):
        kb_id (str):
        job_id (str):
        include_items (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IngestJob]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        kb_id=kb_id,
        job_id=job_id,
        include_items=include_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    kb_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_items: bool | Unset = UNSET,
) -> Error | IngestJob | None:
    """Get an ingest job

    Args:
        workspace_id (str):
        kb_id (str):
        job_id (str):
        include_items (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IngestJob
    """

    return sync_detailed(
        workspace_id=workspace_id,
        kb_id=kb_id,
        job_id=job_id,
        client=client,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    kb_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_items: bool | Unset = UNSET,
) -> Response[Error | IngestJob]:
    """Get an ingest job

    Args:
        workspace_id (str):
        kb_id (str):
        job_id (str):
        include_items (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IngestJob]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        kb_id=kb_id,
        job_id=job_id,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    kb_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_items: bool | Unset = UNSET,
) -> Error | IngestJob | None:
    """Get an ingest job

    Args:
        workspace_id (str):
        kb_id (str):
        job_id (str):
        include_items (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IngestJob
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            kb_id=kb_id,
            job_id=job_id,
            client=client,
            include_items=include_items,
        )
    ).parsed
