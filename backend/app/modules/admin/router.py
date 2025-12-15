from fastapi import APIRouter, Depends

from app.core.rbac.permissions import require_roles
from app.core.rbac.roles import Role
from app.core.security.jwt import Principal

router = APIRouter(prefix="/admin")


@router.get("/stats")
async def admin_stats(principal: Principal = Depends(require_roles(Role.ADMIN, Role.OPS))):
    return {"ok": True, "message": f"Hello {principal.name or principal.sub}"}
