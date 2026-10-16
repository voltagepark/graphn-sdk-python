from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.inference_router import InferenceRouter
from ...models.publish_inference_router_body import PublishInferenceRouterBody
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    router_id: str,
    *,
    body: PublishInferenceRouterBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/inference-routers/{router_id}/publish".format(
            workspace_id=quote(str(workspace_id), safe=""),
            router_id=quote(str(router_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InferenceRouter | None:
    if response.status_code == 202:
        response_202 = InferenceRouter.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

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
) -> Response[Error | InferenceRouter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishInferenceRouterBody,
) -> Response[Error | InferenceRouter]:
    """Submit a draft revision for controller activation

     The existing active revision remains routable until acknowledgement.

    Args:
        workspace_id (str):
        router_id (str):
        body (PublishInferenceRouterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouter]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        router_id=router_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishInferenceRouterBody,
) -> Error | InferenceRouter | None:
    """Submit a draft revision for controller activation

     The existing active revision remains routable until acknowledgement.

    Args:
        workspace_id (str):
        router_id (str):
        body (PublishInferenceRouterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouter
    """

    return sync_detailed(
        workspace_id=workspace_id,
        router_id=router_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishInferenceRouterBody,
) -> Response[Error | InferenceRouter]:
    """Submit a draft revision for controller activation

     The existing active revision remains routable until acknowledgement.

    Args:
        workspace_id (str):
        router_id (str):
        body (PublishInferenceRouterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InferenceRouter]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        router_id=router_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    router_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublishInferenceRouterBody,
) -> Error | InferenceRouter | None:
    """Submit a draft revision for controller activation

     The existing active revision remains routable until acknowledgement.

    Args:
        workspace_id (str):
        router_id (str):
        body (PublishInferenceRouterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InferenceRouter
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            router_id=router_id,
            client=client,
            body=body,
        )
    ).parsed
