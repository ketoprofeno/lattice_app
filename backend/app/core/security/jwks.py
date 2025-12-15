from __future__ import annotations

import httpx
from cachetools import TTLCache

# Cache JWKS por 10 minutos (evita golpear IdP cada request)
_jwks_cache: TTLCache[str, dict] = TTLCache(maxsize=8, ttl=600)


async def fetch_jwks(jwks_url: str) -> dict:
    if jwks_url in _jwks_cache:
        return _jwks_cache[jwks_url]

    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(jwks_url)
        resp.raise_for_status()
        jwks = resp.json()

    _jwks_cache[jwks_url] = jwks
    return jwks
