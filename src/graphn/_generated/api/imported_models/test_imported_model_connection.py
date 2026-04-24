from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.inference_error import InferenceError
from ...models.test_connection_request import TestConnectionRequest
from ...models.test_connection_response import TestConnectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TestConnectionRequest,
    x_workspace_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-Id"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/imported-models/test-connection",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InferenceError | TestConnectionResponse | None:
    if response.status_code == 200:
        response_200 = TestConnectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InferenceError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 502:
        response_502 = InferenceError.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | InferenceError | TestConnectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TestConnectionRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | InferenceError | TestConnectionResponse]:
    """Test connectivity to an external chat model

     Sends a single chat completion to the configured endpoint and
    returns the response text. Use to verify credentials and
    endpoint URL before importing.

    Args:
        x_workspace_id (str | Unset):
        body (TestConnectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceError | TestConnectionResponse]
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
    body: TestConnectionRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Error | InferenceError | TestConnectionResponse | None:
    """Test connectivity to an external chat model

     Sends a single chat completion to the configured endpoint and
    returns the response text. Use to verify credentials and
    endpoint URL before importing.

    Args:
        x_workspace_id (str | Unset):
        body (TestConnectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceError | TestConnectionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TestConnectionRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Response[Error | InferenceError | TestConnectionResponse]:
    """Test connectivity to an external chat model

     Sends a single chat completion to the configured endpoint and
    returns the response text. Use to verify credentials and
    endpoint URL before importing.

    Args:
        x_workspace_id (str | Unset):
        body (TestConnectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceError | TestConnectionResponse]
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
    body: TestConnectionRequest,
    x_workspace_id: str | Unset = UNSET,
) -> Error | InferenceError | TestConnectionResponse | None:
    """Test connectivity to an external chat model

     Sends a single chat completion to the configured endpoint and
    returns the response text. Use to verify credentials and
    endpoint URL before importing.

    Args:
        x_workspace_id (str | Unset):
        body (TestConnectionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceError | TestConnectionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
