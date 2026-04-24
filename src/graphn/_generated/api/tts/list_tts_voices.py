from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.inference_error import InferenceError
from ...models.list_tts_voices_response_200 import ListTtsVoicesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model: str,
    x_workspace_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-Id"] = x_workspace_id

    params: dict[str, Any] = {}

    params["model"] = model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tts/voices",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InferenceError | ListTtsVoicesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListTtsVoicesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InferenceError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | InferenceError | ListTtsVoicesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model: str,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | InferenceError | ListTtsVoicesResponse200]:
    """List TTS voices for a model

    Args:
        model (str):
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceError | ListTtsVoicesResponse200]
    """

    kwargs = _get_kwargs(
        model=model,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    model: str,
    x_workspace_id: str | Unset = UNSET,
) -> Error | InferenceError | ListTtsVoicesResponse200 | None:
    """List TTS voices for a model

    Args:
        model (str):
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceError | ListTtsVoicesResponse200
    """

    return sync_detailed(
        client=client,
        model=model,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model: str,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | InferenceError | ListTtsVoicesResponse200]:
    """List TTS voices for a model

    Args:
        model (str):
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceError | ListTtsVoicesResponse200]
    """

    kwargs = _get_kwargs(
        model=model,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model: str,
    x_workspace_id: str | Unset = UNSET,
) -> Error | InferenceError | ListTtsVoicesResponse200 | None:
    """List TTS voices for a model

    Args:
        model (str):
        x_workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceError | ListTtsVoicesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            model=model,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
