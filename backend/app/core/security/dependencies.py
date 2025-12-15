from __future__ import annotations

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security.jwt import Principal, decode_and_validate

bearer_scheme = HTTPBearer(auto_error=True)


async def get_current_principal(
    creds: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> Principal:
    token = creds.credentials
    return await decode_and_validate(token)
