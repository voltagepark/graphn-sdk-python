from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blueprint_deploy_request import BlueprintDeployRequest
from ...models.blueprint_deploy_response import BlueprintDeployResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    blueprint_id: str,
    *,
    body: BlueprintDeployRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/blueprints/{blueprint_id}/deploy".format(
            workspace_id=quote(str(workspace_id), safe=""),
            blueprint_id=quote(str(blueprint_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BlueprintDeployResponse | Error | None:
    if response.status_code == 201:
        response_201 = BlueprintDeployResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BlueprintDeployResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BlueprintDeployRequest,
) -> Response[BlueprintDeployResponse | Error]:
    """Deploy a blueprint into the workspace

    Args:
        workspace_id (str):
        blueprint_id (str):
        body (BlueprintDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlueprintDeployResponse | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        blueprint_id=blueprint_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BlueprintDeployRequest,
) -> BlueprintDeployResponse | Error | None:
    """Deploy a blueprint into the workspace

    Args:
        workspace_id (str):
        blueprint_id (str):
        body (BlueprintDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlueprintDeployResponse | Error
    """

    return sync_detailed(
        workspace_id=workspace_id,
        blueprint_id=blueprint_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BlueprintDeployRequest,
) -> Response[BlueprintDeployResponse | Error]:
    """Deploy a blueprint into the workspace

    Args:
        workspace_id (str):
        blueprint_id (str):
        body (BlueprintDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlueprintDeployResponse | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        blueprint_id=blueprint_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    blueprint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BlueprintDeployRequest,
) -> BlueprintDeployResponse | Error | None:
    """Deploy a blueprint into the workspace

    Args:
        workspace_id (str):
        blueprint_id (str):
        body (BlueprintDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlueprintDeployResponse | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            blueprint_id=blueprint_id,
            client=client,
            body=body,
        )
    ).parsed
