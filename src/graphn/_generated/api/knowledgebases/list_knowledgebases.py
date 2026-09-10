from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.knowledge_base import KnowledgeBase
from ...models.knowledge_base_list_response import KnowledgeBaseListResponse
from ...models.list_knowledgebases_order import ListKnowledgebasesOrder
from ...models.list_knowledgebases_sort import ListKnowledgebasesSort
from ...models.list_knowledgebases_status import ListKnowledgebasesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    status: ListKnowledgebasesStatus | Unset = UNSET,
    sort: ListKnowledgebasesSort | Unset = ListKnowledgebasesSort.CREATED_AT,
    order: ListKnowledgebasesOrder | Unset = ListKnowledgebasesOrder.DESC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["q"] = q

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{workspace_id}/knowledgebases".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | KnowledgeBaseListResponse | list[KnowledgeBase] | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> KnowledgeBaseListResponse | list[KnowledgeBase]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:
                    response_200_type_0_item = KnowledgeBase.from_dict(
                        response_200_type_0_item_data
                    )

                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = KnowledgeBaseListResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Error | KnowledgeBaseListResponse | list[KnowledgeBase]]:
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    status: ListKnowledgebasesStatus | Unset = UNSET,
    sort: ListKnowledgebasesSort | Unset = ListKnowledgebasesSort.CREATED_AT,
    order: ListKnowledgebasesOrder | Unset = ListKnowledgebasesOrder.DESC,
) -> Response[Error | KnowledgeBaseListResponse | list[KnowledgeBase]]:
    """List knowledge bases

     Default response is a JSON array. When `cursor` or any filter/sort control
    is supplied, the service returns a paginated envelope.

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):
        status (ListKnowledgebasesStatus | Unset):
        sort (ListKnowledgebasesSort | Unset):  Default: ListKnowledgebasesSort.CREATED_AT.
        order (ListKnowledgebasesOrder | Unset):  Default: ListKnowledgebasesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | KnowledgeBaseListResponse | list[KnowledgeBase]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        limit=limit,
        cursor=cursor,
        q=q,
        status=status,
        sort=sort,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    status: ListKnowledgebasesStatus | Unset = UNSET,
    sort: ListKnowledgebasesSort | Unset = ListKnowledgebasesSort.CREATED_AT,
    order: ListKnowledgebasesOrder | Unset = ListKnowledgebasesOrder.DESC,
) -> Error | KnowledgeBaseListResponse | list[KnowledgeBase] | None:
    """List knowledge bases

     Default response is a JSON array. When `cursor` or any filter/sort control
    is supplied, the service returns a paginated envelope.

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):
        status (ListKnowledgebasesStatus | Unset):
        sort (ListKnowledgebasesSort | Unset):  Default: ListKnowledgebasesSort.CREATED_AT.
        order (ListKnowledgebasesOrder | Unset):  Default: ListKnowledgebasesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | KnowledgeBaseListResponse | list[KnowledgeBase]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        limit=limit,
        cursor=cursor,
        q=q,
        status=status,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    status: ListKnowledgebasesStatus | Unset = UNSET,
    sort: ListKnowledgebasesSort | Unset = ListKnowledgebasesSort.CREATED_AT,
    order: ListKnowledgebasesOrder | Unset = ListKnowledgebasesOrder.DESC,
) -> Response[Error | KnowledgeBaseListResponse | list[KnowledgeBase]]:
    """List knowledge bases

     Default response is a JSON array. When `cursor` or any filter/sort control
    is supplied, the service returns a paginated envelope.

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):
        status (ListKnowledgebasesStatus | Unset):
        sort (ListKnowledgebasesSort | Unset):  Default: ListKnowledgebasesSort.CREATED_AT.
        order (ListKnowledgebasesOrder | Unset):  Default: ListKnowledgebasesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | KnowledgeBaseListResponse | list[KnowledgeBase]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        limit=limit,
        cursor=cursor,
        q=q,
        status=status,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    status: ListKnowledgebasesStatus | Unset = UNSET,
    sort: ListKnowledgebasesSort | Unset = ListKnowledgebasesSort.CREATED_AT,
    order: ListKnowledgebasesOrder | Unset = ListKnowledgebasesOrder.DESC,
) -> Error | KnowledgeBaseListResponse | list[KnowledgeBase] | None:
    """List knowledge bases

     Default response is a JSON array. When `cursor` or any filter/sort control
    is supplied, the service returns a paginated envelope.

    Args:
        workspace_id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):
        status (ListKnowledgebasesStatus | Unset):
        sort (ListKnowledgebasesSort | Unset):  Default: ListKnowledgebasesSort.CREATED_AT.
        order (ListKnowledgebasesOrder | Unset):  Default: ListKnowledgebasesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | KnowledgeBaseListResponse | list[KnowledgeBase]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            limit=limit,
            cursor=cursor,
            q=q,
            status=status,
            sort=sort,
            order=order,
        )
    ).parsed
