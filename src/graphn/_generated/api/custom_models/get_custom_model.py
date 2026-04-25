from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_model import CustomModel
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    model_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/custom-models/{model_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            model_id=quote(str(model_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomModel | Error | None:
    if response.status_code == 200:
        response_200 = CustomModel.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomModel | Error]:
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
) -> Response[CustomModel | Error]:
    """Get a custom model

     Returns the latest known state of the custom model, enriched with
    live deployment status (replica counts, endpoint readiness).

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModel | Error]
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
) -> CustomModel | Error | None:
    """Get a custom model

     Returns the latest known state of the custom model, enriched with
    live deployment status (replica counts, endpoint readiness).

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModel | Error
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
) -> Response[CustomModel | Error]:
    """Get a custom model

     Returns the latest known state of the custom model, enriched with
    live deployment status (replica counts, endpoint readiness).

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModel | Error]
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
) -> CustomModel | Error | None:
    """Get a custom model

     Returns the latest known state of the custom model, enriched with
    live deployment status (replica counts, endpoint readiness).

    Args:
        workspace_id (str):
        model_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModel | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            model_id=model_id,
            client=client,
        )
    ).parsed
