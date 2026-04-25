from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.secret import Secret
from ...models.secret_update import SecretUpdate
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    secret_id: str,
    *,
    body: SecretUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/{workspace_id}/secrets/{secret_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            secret_id=quote(str(secret_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Secret | None:
    if response.status_code == 200:
        response_200 = Secret.from_dict(response.json())

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
) -> Response[Error | Secret]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    secret_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SecretUpdate,
) -> Response[Error | Secret]:
    """Update a secret's value

     Rotates the secret's plaintext value. The secret's `name` and
    other metadata are immutable; create a new secret if you need
    a different name.

    Args:
        workspace_id (str):
        secret_id (str):
        body (SecretUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Secret]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        secret_id=secret_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    secret_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SecretUpdate,
) -> Error | Secret | None:
    """Update a secret's value

     Rotates the secret's plaintext value. The secret's `name` and
    other metadata are immutable; create a new secret if you need
    a different name.

    Args:
        workspace_id (str):
        secret_id (str):
        body (SecretUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Secret
    """

    return sync_detailed(
        workspace_id=workspace_id,
        secret_id=secret_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    secret_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SecretUpdate,
) -> Response[Error | Secret]:
    """Update a secret's value

     Rotates the secret's plaintext value. The secret's `name` and
    other metadata are immutable; create a new secret if you need
    a different name.

    Args:
        workspace_id (str):
        secret_id (str):
        body (SecretUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Secret]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        secret_id=secret_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    secret_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SecretUpdate,
) -> Error | Secret | None:
    """Update a secret's value

     Rotates the secret's plaintext value. The secret's `name` and
    other metadata are immutable; create a new secret if you need
    a different name.

    Args:
        workspace_id (str):
        secret_id (str):
        body (SecretUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Secret
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            secret_id=secret_id,
            client=client,
            body=body,
        )
    ).parsed
