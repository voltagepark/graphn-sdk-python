from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_model import CustomModel
from ...models.custom_model_adapter_attach import CustomModelAdapterAttach
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    model_id: str,
    *,
    body: CustomModelAdapterAttach,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{workspace_id}/custom-models/{model_id}/adapters".format(
            workspace_id=quote(str(workspace_id), safe=""),
            model_id=quote(str(model_id), safe=""),
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

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

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
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelAdapterAttach,
    idempotency_key: str | Unset = UNSET,
) -> Response[CustomModel | Error]:
    """Attach a LoRA adapter to a shared base

     Preview, refused with `409 SHARED_LORA_UNSUPPORTED` unless enabled
    for the workspace's deployment. Registers a LoRA adapter on a
    shared LoRA base (a custom model created with `lora_enabled`). The
    adapter uses no GPU of its own: the base loads it, and clients
    call it as `custom:<id>` in chat completions once it is `ready`,
    where `id` is the adapter's own ID from the response. The response
    returns immediately with the adapter `pending`.

    Refusals: `409 NOT_LORA_ENABLED` when the model is not a shared
    LoRA base, `409 BASE_NOT_AVAILABLE` when the base has failed or is
    being deleted, `422 ADAPTER_LIMIT_EXCEEDED` when the base already
    has `max_adapters` attached, and `409 ALREADY_EXISTS` when the name
    is taken in the workspace. Attaching is gated like importing a
    model: `402 PURCHASE_REQUIRED` and `403 CUSTOM_MODELS_DISABLED`.

    Staging validates the adapter's files after the attach. An adapter
    that fails then, or later fails to roll out, reads `failed` with an
    `error_message` that starts with a reason code: `ADAPTER_INVALID`,
    `ADAPTER_RANK_EXCEEDS_BASE`, `ADAPTER_BASE_MISMATCH`,
    `ADAPTER_LOAD_FAILED`, `WAITING_FOR_GPU_TIMEOUT` or
    `INFRASTRUCTURE_UNAVAILABLE`.

    Args:
        workspace_id (str):
        model_id (str):
        idempotency_key (str | Unset):
        body (CustomModelAdapterAttach): Preview. Request body for
            `POST /v1/{workspaceId}/custom-models/{modelId}/adapters`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModel | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        model_id=model_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelAdapterAttach,
    idempotency_key: str | Unset = UNSET,
) -> CustomModel | Error | None:
    """Attach a LoRA adapter to a shared base

     Preview, refused with `409 SHARED_LORA_UNSUPPORTED` unless enabled
    for the workspace's deployment. Registers a LoRA adapter on a
    shared LoRA base (a custom model created with `lora_enabled`). The
    adapter uses no GPU of its own: the base loads it, and clients
    call it as `custom:<id>` in chat completions once it is `ready`,
    where `id` is the adapter's own ID from the response. The response
    returns immediately with the adapter `pending`.

    Refusals: `409 NOT_LORA_ENABLED` when the model is not a shared
    LoRA base, `409 BASE_NOT_AVAILABLE` when the base has failed or is
    being deleted, `422 ADAPTER_LIMIT_EXCEEDED` when the base already
    has `max_adapters` attached, and `409 ALREADY_EXISTS` when the name
    is taken in the workspace. Attaching is gated like importing a
    model: `402 PURCHASE_REQUIRED` and `403 CUSTOM_MODELS_DISABLED`.

    Staging validates the adapter's files after the attach. An adapter
    that fails then, or later fails to roll out, reads `failed` with an
    `error_message` that starts with a reason code: `ADAPTER_INVALID`,
    `ADAPTER_RANK_EXCEEDS_BASE`, `ADAPTER_BASE_MISMATCH`,
    `ADAPTER_LOAD_FAILED`, `WAITING_FOR_GPU_TIMEOUT` or
    `INFRASTRUCTURE_UNAVAILABLE`.

    Args:
        workspace_id (str):
        model_id (str):
        idempotency_key (str | Unset):
        body (CustomModelAdapterAttach): Preview. Request body for
            `POST /v1/{workspaceId}/custom-models/{modelId}/adapters`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModel | Error
    """

    return sync_detailed(
        workspace_id=workspace_id,
        model_id=model_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelAdapterAttach,
    idempotency_key: str | Unset = UNSET,
) -> Response[CustomModel | Error]:
    """Attach a LoRA adapter to a shared base

     Preview, refused with `409 SHARED_LORA_UNSUPPORTED` unless enabled
    for the workspace's deployment. Registers a LoRA adapter on a
    shared LoRA base (a custom model created with `lora_enabled`). The
    adapter uses no GPU of its own: the base loads it, and clients
    call it as `custom:<id>` in chat completions once it is `ready`,
    where `id` is the adapter's own ID from the response. The response
    returns immediately with the adapter `pending`.

    Refusals: `409 NOT_LORA_ENABLED` when the model is not a shared
    LoRA base, `409 BASE_NOT_AVAILABLE` when the base has failed or is
    being deleted, `422 ADAPTER_LIMIT_EXCEEDED` when the base already
    has `max_adapters` attached, and `409 ALREADY_EXISTS` when the name
    is taken in the workspace. Attaching is gated like importing a
    model: `402 PURCHASE_REQUIRED` and `403 CUSTOM_MODELS_DISABLED`.

    Staging validates the adapter's files after the attach. An adapter
    that fails then, or later fails to roll out, reads `failed` with an
    `error_message` that starts with a reason code: `ADAPTER_INVALID`,
    `ADAPTER_RANK_EXCEEDS_BASE`, `ADAPTER_BASE_MISMATCH`,
    `ADAPTER_LOAD_FAILED`, `WAITING_FOR_GPU_TIMEOUT` or
    `INFRASTRUCTURE_UNAVAILABLE`.

    Args:
        workspace_id (str):
        model_id (str):
        idempotency_key (str | Unset):
        body (CustomModelAdapterAttach): Preview. Request body for
            `POST /v1/{workspaceId}/custom-models/{modelId}/adapters`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomModel | Error]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        model_id=model_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomModelAdapterAttach,
    idempotency_key: str | Unset = UNSET,
) -> CustomModel | Error | None:
    """Attach a LoRA adapter to a shared base

     Preview, refused with `409 SHARED_LORA_UNSUPPORTED` unless enabled
    for the workspace's deployment. Registers a LoRA adapter on a
    shared LoRA base (a custom model created with `lora_enabled`). The
    adapter uses no GPU of its own: the base loads it, and clients
    call it as `custom:<id>` in chat completions once it is `ready`,
    where `id` is the adapter's own ID from the response. The response
    returns immediately with the adapter `pending`.

    Refusals: `409 NOT_LORA_ENABLED` when the model is not a shared
    LoRA base, `409 BASE_NOT_AVAILABLE` when the base has failed or is
    being deleted, `422 ADAPTER_LIMIT_EXCEEDED` when the base already
    has `max_adapters` attached, and `409 ALREADY_EXISTS` when the name
    is taken in the workspace. Attaching is gated like importing a
    model: `402 PURCHASE_REQUIRED` and `403 CUSTOM_MODELS_DISABLED`.

    Staging validates the adapter's files after the attach. An adapter
    that fails then, or later fails to roll out, reads `failed` with an
    `error_message` that starts with a reason code: `ADAPTER_INVALID`,
    `ADAPTER_RANK_EXCEEDS_BASE`, `ADAPTER_BASE_MISMATCH`,
    `ADAPTER_LOAD_FAILED`, `WAITING_FOR_GPU_TIMEOUT` or
    `INFRASTRUCTURE_UNAVAILABLE`.

    Args:
        workspace_id (str):
        model_id (str):
        idempotency_key (str | Unset):
        body (CustomModelAdapterAttach): Preview. Request body for
            `POST /v1/{workspaceId}/custom-models/{modelId}/adapters`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomModel | Error
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            model_id=model_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
