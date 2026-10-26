from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider_id: str,
    *,
    state: str,
    code: str | Unset = UNSET,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["state"] = state

    params["code"] = code

    params["error"] = error

    params["error_description"] = error_description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/oauth/connections/{provider_id}/callback".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset = UNSET,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
) -> Response[Any | Error]:
    """Complete a provider OAuth authorization

     Public OAuth callback. Tenant identity, PKCE data, and the final redirect
    are recovered exclusively from one-time encrypted state.

    Args:
        provider_id (str):
        state (str):
        code (str | Unset):
        error (str | Unset):
        error_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        state=state,
        code=code,
        error=error,
        error_description=error_description,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset = UNSET,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
) -> Any | Error | None:
    """Complete a provider OAuth authorization

     Public OAuth callback. Tenant identity, PKCE data, and the final redirect
    are recovered exclusively from one-time encrypted state.

    Args:
        provider_id (str):
        state (str):
        code (str | Unset):
        error (str | Unset):
        error_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        state=state,
        code=code,
        error=error,
        error_description=error_description,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset = UNSET,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
) -> Response[Any | Error]:
    """Complete a provider OAuth authorization

     Public OAuth callback. Tenant identity, PKCE data, and the final redirect
    are recovered exclusively from one-time encrypted state.

    Args:
        provider_id (str):
        state (str):
        code (str | Unset):
        error (str | Unset):
        error_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        state=state,
        code=code,
        error=error,
        error_description=error_description,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset = UNSET,
    error: str | Unset = UNSET,
    error_description: str | Unset = UNSET,
) -> Any | Error | None:
    """Complete a provider OAuth authorization

     Public OAuth callback. Tenant identity, PKCE data, and the final redirect
    are recovered exclusively from one-time encrypted state.

    Args:
        provider_id (str):
        state (str):
        code (str | Unset):
        error (str | Unset):
        error_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            state=state,
            code=code,
            error=error,
            error_description=error_description,
        )
    ).parsed
