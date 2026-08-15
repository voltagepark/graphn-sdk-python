from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.kb_document import KbDocument
from ...models.upload_document_from_url_request import UploadDocumentFromURLRequest
from ...models.upload_knowledgebase_document_files_body import (
    UploadKnowledgebaseDocumentFilesBody,
)
from ...types import UNSET, Response


def _get_kwargs(
    workspace_id: str,
    kb_id: str,
    *,
    body: UploadDocumentFromURLRequest
    | UploadKnowledgebaseDocumentFilesBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/knowledgebases/{kb_id}/documents".format(
            workspace_id=quote(str(workspace_id), safe=""),
            kb_id=quote(str(kb_id), safe=""),
        ),
    }

    if isinstance(body, UploadDocumentFromURLRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UploadKnowledgebaseDocumentFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | KbDocument | None:
    if response.status_code == 201:
        response_201 = KbDocument.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | KbDocument]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    kb_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadDocumentFromURLRequest
    | UploadKnowledgebaseDocumentFilesBody
    | Unset = UNSET,
) -> Response[Error | KbDocument]:
    """Upload or URL-ingest a document

     `multipart/form-data` uploads text bytes (max 100 MiB). `application/json` with `url` fetches the
    document server-side (text, image, or video).

    Args:
        workspace_id (str):
        kb_id (str):
        body (UploadDocumentFromURLRequest):
        body (UploadKnowledgebaseDocumentFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | KbDocument]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        kb_id=kb_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    kb_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadDocumentFromURLRequest
    | UploadKnowledgebaseDocumentFilesBody
    | Unset = UNSET,
) -> Error | KbDocument | None:
    """Upload or URL-ingest a document

     `multipart/form-data` uploads text bytes (max 100 MiB). `application/json` with `url` fetches the
    document server-side (text, image, or video).

    Args:
        workspace_id (str):
        kb_id (str):
        body (UploadDocumentFromURLRequest):
        body (UploadKnowledgebaseDocumentFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | KbDocument
    """

    return sync_detailed(
        workspace_id=workspace_id,
        kb_id=kb_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    kb_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadDocumentFromURLRequest
    | UploadKnowledgebaseDocumentFilesBody
    | Unset = UNSET,
) -> Response[Error | KbDocument]:
    """Upload or URL-ingest a document

     `multipart/form-data` uploads text bytes (max 100 MiB). `application/json` with `url` fetches the
    document server-side (text, image, or video).

    Args:
        workspace_id (str):
        kb_id (str):
        body (UploadDocumentFromURLRequest):
        body (UploadKnowledgebaseDocumentFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | KbDocument]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        kb_id=kb_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    kb_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadDocumentFromURLRequest
    | UploadKnowledgebaseDocumentFilesBody
    | Unset = UNSET,
) -> Error | KbDocument | None:
    """Upload or URL-ingest a document

     `multipart/form-data` uploads text bytes (max 100 MiB). `application/json` with `url` fetches the
    document server-side (text, image, or video).

    Args:
        workspace_id (str):
        kb_id (str):
        body (UploadDocumentFromURLRequest):
        body (UploadKnowledgebaseDocumentFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | KbDocument
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            kb_id=kb_id,
            client=client,
            body=body,
        )
    ).parsed
