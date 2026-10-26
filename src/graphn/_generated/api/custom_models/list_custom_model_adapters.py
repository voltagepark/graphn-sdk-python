from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_model_list import CustomModelList
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    model_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/custom-models/{model_id}/adapters".format(
            workspace_id=quote(str(workspace_id), safe=""),
            model_id=quote(str(model_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomModelList | Error | None:
    if response.status_code == 200:
        response_200 = CustomModelList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomModelList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CustomModelList | Error]:
    """List the adapters attached to a shared base

     Preview. Every adapter on the base, oldest first, including those
    that failed or are being deleted. Each reports the base's GPU and
    replica fields.

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModelList | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        model_id=model_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CustomModelList | Error | None:
    """List the adapters attached to a shared base

     Preview. Every adapter on the base, oldest first, including those
    that failed or are being deleted. Each reports the base's GPU and
    replica fields.

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModelList | Error
    """

    return sync_detailed(
        workspace_id=workspace_id,
        model_id=model_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CustomModelList | Error]:
    """List the adapters attached to a shared base

     Preview. Every adapter on the base, oldest first, including those
    that failed or are being deleted. Each reports the base's GPU and
    replica fields.

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModelList | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        model_id=model_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CustomModelList | Error | None:
    """List the adapters attached to a shared base

     Preview. Every adapter on the base, oldest first, including those
    that failed or are being deleted. Each reports the base's GPU and
    replica fields.

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModelList | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            model_id=model_id,
            client=client,
        )
    ).parsed
