from fastapi import APIRouter, Depends

from app.core.security.dependencies import get_current_principal
from app.core.security.jwt import Principal

router = APIRouter(prefix="/me")


@router.get("")
async def whoami(principal: Principal = Depends(get_current_principal)):
    return {
        "sub": principal.sub,
        "email": principal.email,
        "name": principal.name,
        "groups": principal.groups,
        "roles": sorted(list(principal.roles)),
    }
