from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.model_list import ModelList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_workspace_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-Id"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/models",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ModelList | None:
    if response.status_code == 200:
        response_200 = ModelList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ModelList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | ModelList]:
    """List models available to the workspace

     Returns built-in models, imported models, and custom models in
    OpenAI `/v1/models` format. Use the returned `id` as the `model`
    field on `createChatCompletion`.

    Args:
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ModelList]
    """

    kwargs = _get_kwargs(
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_workspace_id: str | Unset = UNSET,
) -> Error | ModelList | None:
    """List models available to the workspace

     Returns built-in models, imported models, and custom models in
    OpenAI `/v1/models` format. Use the returned `id` as the `model`
    field on `createChatCompletion`.

    Args:
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ModelList
    """

    return sync_detailed(
        client=client,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | ModelList]:
    """List models available to the workspace

     Returns built-in models, imported models, and custom models in
    OpenAI `/v1/models` format. Use the returned `id` as the `model`
    field on `createChatCompletion`.

    Args:
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ModelList]
    """

    kwargs = _get_kwargs(
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_workspace_id: str | Unset = UNSET,
) -> Error | ModelList | None:
    """List models available to the workspace

     Returns built-in models, imported models, and custom models in
    OpenAI `/v1/models` format. Use the returned `id` as the `model`
    field on `createChatCompletion`.

    Args:
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ModelList
    """

    return (
        await asyncio_detailed(
            client=client,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
