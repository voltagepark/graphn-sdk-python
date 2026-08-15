from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket: str,
    key: str,
    *,
    upload_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["uploadId"] = upload_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{bucket}/{key}".format(
            bucket=quote(str(bucket), safe=""),
            key=quote(str(key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    upload_id: str | Unset = UNSET,
) -> Response[Any | Error]:
    """Delete an object or abort an MPU

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        key=key,
        upload_id=upload_id,
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
    upload_id: str | Unset = UNSET,
) -> Any | Error | None:
    """Delete an object or abort an MPU

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):

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
        upload_id=upload_id,
    ).parsed


async def asyncio_detailed(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
) -> Response[Any | Error]:
    """Delete an object or abort an MPU

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        key=key,
        upload_id=upload_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    upload_id: str | Unset = UNSET,
) -> Any | Error | None:
    """Delete an object or abort an MPU

    Args:
        bucket (str):
        key (str):
        upload_id (str | Unset):

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
            upload_id=upload_id,
        )
    ).parsed
