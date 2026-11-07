from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.applicable_spend_limit_status import ApplicableSpendLimitStatus


T = TypeVar("T", bound="ApplicableSpendLimitsResponse")


@_attrs_define
class ApplicableSpendLimitsResponse:
    """
    Attributes:
        user (ApplicableSpendLimitStatus | None):
        workspace (ApplicableSpendLimitStatus | None):
    """

    user: ApplicableSpendLimitStatus | None
    workspace: ApplicableSpendLimitStatus | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.applicable_spend_limit_status import ApplicableSpendLimitStatus

        user: dict[str, Any] | None
        if isinstance(self.user, ApplicableSpendLimitStatus):
            user = self.user.to_dict()
        else:
            user = self.user

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ApplicableSpendLimitStatus):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user": user,
                "workspace": workspace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.applicable_spend_limit_status import ApplicableSpendLimitStatus

        d = dict(src_dict)

        def _parse_user(data: object) -> ApplicableSpendLimitStatus | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = ApplicableSpendLimitStatus.from_dict(data)

                return user_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplicableSpendLimitStatus | None, data)

        user = _parse_user(d.pop("user"))

        def _parse_workspace(data: object) -> ApplicableSpendLimitStatus | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_1 = ApplicableSpendLimitStatus.from_dict(data)

                return workspace_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplicableSpendLimitStatus | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        applicable_spend_limits_response = cls(
            user=user,
            workspace=workspace,
        )

        return applicable_spend_limits_response
