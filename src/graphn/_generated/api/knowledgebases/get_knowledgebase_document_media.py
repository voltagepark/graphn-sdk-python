from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_media import DocumentMedia
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    kb_id: str,
    doc_id: str,
    *,
    index: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["index"] = index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/knowledgebases/{kb_id}/documents/{doc_id}/media".format(
            workspace_id=quote(str(workspace_id), safe=""),
            kb_id=quote(str(kb_id), safe=""),
            doc_id=quote(str(doc_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocumentMedia | Error | None:
    if response.status_code == 200:
        response_200 = DocumentMedia.from_dict(response.json())

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
) -> Response[DocumentMedia | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    kb_id: str,
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    index: int | Unset = 0,
) -> Response[DocumentMedia | Error]:
    """Mint a fresh playable URL for document media

    Args:
        workspace_id (str):
        kb_id (str):
        doc_id (str):
        index (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentMedia | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        kb_id=kb_id,
        doc_id=doc_id,
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    kb_id: str,
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    index: int | Unset = 0,
) -> DocumentMedia | Error | None:
    """Mint a fresh playable URL for document media

    Args:
        workspace_id (str):
        kb_id (str):
        doc_id (str):
        index (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentMedia | Error
    """

    return sync_detailed(
        workspace_id=workspace_id,
        kb_id=kb_id,
        doc_id=doc_id,
        client=client,
        index=index,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    kb_id: str,
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    index: int | Unset = 0,
) -> Response[DocumentMedia | Error]:
    """Mint a fresh playable URL for document media

    Args:
        workspace_id (str):
        kb_id (str):
        doc_id (str):
        index (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentMedia | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        kb_id=kb_id,
        doc_id=doc_id,
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    kb_id: str,
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    index: int | Unset = 0,
) -> DocumentMedia | Error | None:
    """Mint a fresh playable URL for document media

    Args:
        workspace_id (str):
        kb_id (str):
        doc_id (str):
        index (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentMedia | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            kb_id=kb_id,
            doc_id=doc_id,
            client=client,
            index=index,
        )
    ).parsed
