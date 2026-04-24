from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.inference_error import InferenceError
from ...models.tts_request import TTSRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TTSRequest,
    x_workspace_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-Id"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InferenceError | None:
    if response.status_code == 400:
        response_400 = InferenceError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = InferenceError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | InferenceError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TTSRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | InferenceError]:
    """Synthesize speech from text

     Returns audio bytes in the format implied by `responseFormat`
    (Qwen models) or fixed by the upstream provider (Rime returns
    MP3). Streaming is provider-defined.

    Args:
        x_workspace_id (str | Unset):
        body (TTSRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TTSRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Error | InferenceError | None:
    """Synthesize speech from text

     Returns audio bytes in the format implied by `responseFormat`
    (Qwen models) or fixed by the upstream provider (Rime returns
    MP3). Streaming is provider-defined.

    Args:
        x_workspace_id (str | Unset):
        body (TTSRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TTSRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | InferenceError]:
    """Synthesize speech from text

     Returns audio bytes in the format implied by `responseFormat`
    (Qwen models) or fixed by the upstream provider (Rime returns
    MP3). Streaming is provider-defined.

    Args:
        x_workspace_id (str | Unset):
        body (TTSRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TTSRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Error | InferenceError | None:
    """Synthesize speech from text

     Returns audio bytes in the format implied by `responseFormat`
    (Qwen models) or fixed by the upstream provider (Rime returns
    MP3). Streaming is provider-defined.

    Args:
        x_workspace_id (str | Unset):
        body (TTSRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
