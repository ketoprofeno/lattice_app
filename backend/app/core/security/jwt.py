from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from fastapi import HTTPException, status
from jose import jwt
from jose.exceptions import JWTError
from jose.utils import base64url_decode

from app.core.config.settings import settings
from app.core.security.jwks import fetch_jwks


@dataclass(frozen=True)
class Principal:
    sub: str
    email: str | None
    name: str | None
    groups: list[str]
    roles: set[str]
    raw_claims: dict[str, Any]


def _select_key(jwks: dict, token: str) -> dict:
    headers = jwt.get_unverified_header(token)
    kid = headers.get("kid")
    if not kid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing kid in token header")

    for key in jwks.get("keys", []):
        if key.get("kid") == kid:
            return key

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unknown signing key (kid)")


def _build_rsa_key(jwk: dict) -> dict:
    # python-jose acepta keys como dict con n/e
    if jwk.get("kty") != "RSA":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unsupported key type")
    return {"kty": "RSA", "kid": jwk.get("kid"), "use": jwk.get("use"), "n": jwk.get("n"), "e": jwk.get("e")}


async def decode_and_validate(token: str) -> Principal:
    jwks = await fetch_jwks(str(settings.oidc_jwks_url))
    jwk = _select_key(jwks, token)
    rsa_key = _build_rsa_key(jwk)

    try:
        claims = jwt.decode(
            token,
            rsa_key,
            algorithms=settings.oidc_algorithms_list,
            audience=settings.oidc_audience,
            issuer=settings.oidc_issuer,
            options={"verify_at_hash": False},
        )
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from e

    groups_claim = settings.auth_groups_claim
    groups = claims.get(groups_claim, [])
    if groups is None:
        groups = []
    if isinstance(groups, str):
        groups = [groups]
    if not isinstance(groups, list):
        groups = []

    # mapeo grupos → roles internos
    group_role_map = settings.rbac_group_role_map
    roles = {group_role_map[g] for g in groups if g in group_role_map}

    sub = claims.get("sub") or claims.get("preferred_username") or ""

    return Principal(
        sub=str(sub),
        email=claims.get("email"),
        name=claims.get("name") or claims.get("preferred_username"),
        groups=[str(g) for g in groups],
        roles=set(roles),
        raw_claims=claims,
    )
