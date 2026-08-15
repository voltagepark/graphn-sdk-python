from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.function_test_request import FunctionTestRequest
from ...models.function_test_response import FunctionTestResponse
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    function_id: str,
    *,
    body: FunctionTestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/functions/{function_id}/test".format(
            workspace_id=quote(str(workspace_id), safe=""),
            function_id=quote(str(function_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | FunctionTestResponse | None:
    if response.status_code == 200:
        response_200 = FunctionTestResponse.from_dict(response.json())

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
) -> Response[Error | FunctionTestResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    function_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FunctionTestRequest,
) -> Response[Error | FunctionTestResponse]:
    """Test a function

    Args:
        workspace_id (str):
        function_id (str):
        body (FunctionTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FunctionTestResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        function_id=function_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    function_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FunctionTestRequest,
) -> Error | FunctionTestResponse | None:
    """Test a function

    Args:
        workspace_id (str):
        function_id (str):
        body (FunctionTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FunctionTestResponse
    """

    return sync_detailed(
        workspace_id=workspace_id,
        function_id=function_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    function_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FunctionTestRequest,
) -> Response[Error | FunctionTestResponse]:
    """Test a function

    Args:
        workspace_id (str):
        function_id (str):
        body (FunctionTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FunctionTestResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        function_id=function_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    function_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FunctionTestRequest,
) -> Error | FunctionTestResponse | None:
    """Test a function

    Args:
        workspace_id (str):
        function_id (str):
        body (FunctionTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FunctionTestResponse
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            function_id=function_id,
            client=client,
            body=body,
        )
    ).parsed
