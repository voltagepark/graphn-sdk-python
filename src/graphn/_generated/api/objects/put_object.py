from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    bucket: str,
    key: str,
    *,
    body: File,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["uploadId"] = upload_id

    params["partNumber"] = part_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/{bucket}/{key}".format(
            bucket=quote(str(bucket), safe=""),
            key=quote(str(key), safe=""),
        ),
        "params": params,
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Response[Any | Error]:
    """Upload an object (single-shot)

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        key=key,
        body=body,
        upload_id=upload_id,
        part_number=part_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Any | Error | None:
    """Upload an object (single-shot)

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        bucket=bucket,
        key=key,
        client=client,
        body=body,
        upload_id=upload_id,
        part_number=part_number,
    ).parsed


async def asyncio_detailed(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Response[Any | Error]:
    """Upload an object (single-shot)

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        key=key,
        body=body,
        upload_id=upload_id,
        part_number=part_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,
    upload_id: str | Unset = UNSET,
    part_number: int | Unset = UNSET,
) -> Any | Error | None:
    """Upload an object (single-shot)

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):
        part_number (int | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            bucket=bucket,
            key=key,
            client=client,
            body=body,
            upload_id=upload_id,
            part_number=part_number,
        )
    ).parsed
