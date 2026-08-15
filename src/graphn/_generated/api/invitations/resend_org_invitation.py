from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.invitation import Invitation
from ...types import Response


def _get_kwargs(
    org_id: str,
    invitation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{org_id}/invitations/{invitation_id}/resend".format(
            org_id=quote(str(org_id), safe=""),
            invitation_id=quote(str(invitation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Invitation | None:
    if response.status_code == 200:
        response_200 = Invitation.from_dict(response.json())

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
) -> Response[Error | Invitation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Invitation]:
    """Resend an organization invitation

    Args:
        org_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Invitation]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        invitation_id=invitation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Invitation | None:
    """Resend an organization invitation

    Args:
        org_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Invitation
    """

    return sync_detailed(
        org_id=org_id,
        invitation_id=invitation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Invitation]:
    """Resend an organization invitation

    Args:
        org_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Invitation]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        invitation_id=invitation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Invitation | None:
    """Resend an organization invitation

    Args:
        org_id (str):
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Invitation
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            invitation_id=invitation_id,
            client=client,
        )
    ).parsed
