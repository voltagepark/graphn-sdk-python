"""Exception hierarchy for the Graphn SDK.

Mirrors the public ``Error`` schema from the OpenAPI spec
(``code`` / ``message`` / optional ``details``) and maps HTTP status
codes to specific subclasses so callers can ``except`` on intent rather
than on integers.

The fully implemented client lives in :mod:`graphn._client`; this
module is intentionally light so it can be imported during package
init without pulling in HTTP machinery.
"""

from __future__ import annotations

from typing import Any


class GraphnError(Exception):
    """Base class for all errors raised by the SDK."""


class APIConnectionError(GraphnError):
    """Raised when the SDK cannot reach the Graphn API at all."""


class APIError(GraphnError):
    """Raised when the API returns a non-2xx response.

    Attributes
    ----------
    status_code:
        HTTP status code of the failed response.
    code:
        Machine-readable error code (mirrors the spec's ``Error.code``).
    message:
        Human-readable message returned by the server.
    details:
        Optional structured ``details`` payload from the spec's
        ``Error.details`` field. ``None`` if the server did not include
        one.
    request_id:
        Value of the ``X-Request-Id`` response header, if present.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        code: str | None = None,
        details: dict[str, Any] | None = None,
        request_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.message = message
        self.details = details
        self.request_id = request_id

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(status_code={self.status_code}, "
            f"code={self.code!r}, message={self.message!r}, "
            f"request_id={self.request_id!r})"
        )


class AuthenticationError(APIError):
    """HTTP 401 — missing or invalid API key."""


class PermissionDeniedError(APIError):
    """HTTP 403 — the API key cannot access this workspace or resource."""


class NotFoundError(APIError):
    """HTTP 404 — the requested resource does not exist."""


class ConflictError(APIError):
    """HTTP 409 — request conflicts with the current resource state."""


class ValidationError(APIError):
    """HTTP 422 — request body failed server-side validation."""


class RateLimitError(APIError):
    """HTTP 429 — the workspace has exceeded its rate limit."""


class ServerError(APIError):
    """HTTP 5xx — the API itself failed."""


_STATUS_TO_EXC: dict[int, type[APIError]] = {
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    422: ValidationError,
    429: RateLimitError,
}


def from_response(
    *,
    status_code: int,
    code: str | None,
    message: str,
    details: dict[str, Any] | None = None,
    request_id: str | None = None,
) -> APIError:
    """Build the appropriate :class:`APIError` subclass for ``status_code``."""

    if status_code >= 500:
        cls: type[APIError] = ServerError
    else:
        cls = _STATUS_TO_EXC.get(status_code, APIError)
    return cls(
        message,
        status_code=status_code,
        code=code,
        details=details,
        request_id=request_id,
    )
