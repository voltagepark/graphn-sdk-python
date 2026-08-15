from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.invitation_list import InvitationList
from ...types import Response


def _get_kwargs(
    org_id: str,
    workspace_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{org_id}/{workspace_id}/invitations".format(
            org_id=quote(str(org_id), safe=""),
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InvitationList | None:
    if response.status_code == 200:
        response_200 = InvitationList.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | InvitationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | InvitationList]:
    """List workspace invitations

    Args:
        org_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvitationList]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | InvitationList | None:
    """List workspace invitations

    Args:
        org_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvitationList
    """

    return sync_detailed(
        org_id=org_id,
        workspace_id=workspace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | InvitationList]:
    """List workspace invitations

    Args:
        org_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvitationList]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | InvitationList | None:
    """List workspace invitations

    Args:
        org_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvitationList
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            workspace_id=workspace_id,
            client=client,
        )
    ).parsed
