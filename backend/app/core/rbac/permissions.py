from __future__ import annotations

from fastapi import Depends, HTTPException, status

from app.core.rbac.roles import Role
from app.core.security.dependencies import get_current_principal
from app.core.security.jwt import Principal


def require_roles(*allowed: Role):
    allowed_set = {r.value for r in allowed}

    async def _dep(principal: Principal = Depends(get_current_principal)) -> Principal:
        if not principal.roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No role assigned")
        if principal.roles.isdisjoint(allowed_set):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
        return principal

    return _dep
