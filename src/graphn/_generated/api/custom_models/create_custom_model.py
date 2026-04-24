from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_model import CustomModel
from ...models.custom_model_create import CustomModelCreate
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    *,
    body: CustomModelCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/custom-models".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomModel | Error | None:
    if response.status_code == 201:
        response_201 = CustomModel.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

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
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelCreate,
) -> Response[CustomModel | Error]:
    r"""Register a new custom model

     Begin import + deployment of a custom model. The response returns
    immediately with `status: \"deploying\"`. Poll `getCustomModel`
    (or use the SDK's `wait_until_ready`) until the status reaches
    `ready` or `failed`.

    Args:
        workspace_id (str):
        body (CustomModelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModel | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelCreate,
) -> CustomModel | Error | None:
    r"""Register a new custom model

     Begin import + deployment of a custom model. The response returns
    immediately with `status: \"deploying\"`. Poll `getCustomModel`
    (or use the SDK's `wait_until_ready`) until the status reaches
    `ready` or `failed`.

    Args:
        workspace_id (str):
        body (CustomModelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModel | Error
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelCreate,
) -> Response[CustomModel | Error]:
    r"""Register a new custom model

     Begin import + deployment of a custom model. The response returns
    immediately with `status: \"deploying\"`. Poll `getCustomModel`
    (or use the SDK's `wait_until_ready`) until the status reaches
    `ready` or `failed`.

    Args:
        workspace_id (str):
        body (CustomModelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModel | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelCreate,
) -> CustomModel | Error | None:
    r"""Register a new custom model

     Begin import + deployment of a custom model. The response returns
    immediately with `status: \"deploying\"`. Poll `getCustomModel`
    (or use the SDK's `wait_until_ready`) until the status reaches
    `ready` or `failed`.

    Args:
        workspace_id (str):
        body (CustomModelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModel | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
