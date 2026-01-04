from __future__ import annotations

import logging
import time
import uuid

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.request_context import set_request_id
from app.core.security.jwt import decode_and_validate

logger = logging.getLogger("audit")


class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # BYPASS OBLIGATORIO PARA PREFLIGHT CORS
        if request.method == "OPTIONS":
            return Response(status_code=200)

        rid = request.headers.get("X-Request-Id") or str(uuid.uuid4())
        set_request_id(rid)

        start = time.perf_counter()

        principal_sub = None
        principal_email = None

        # Intentar extraer identidad si viene Authorization
        auth = request.headers.get("Authorization")
        if auth and auth.lower().startswith("bearer "):
            token = auth.split(" ", 1)[1]
            try:
                principal = await decode_and_validate(token)
                principal_sub = principal.sub
                principal_email = principal.email
            except Exception:
                # No rompemos el request por errores de auditoría
                pass

        response: Response = await call_next(request)

        latency_ms = round((time.perf_counter() - start) * 1000, 2)

        logger.info(
            "request",
            extra={
                "extra": {
                    "request_id": rid,
                    "method": request.method,
                    "path": request.url.path,
                    "status": response.status_code,
                    "latency_ms": latency_ms,
                    "sub": principal_sub,
                    "email": principal_email,
                    "client": request.client.host if request.client else None,
                }
            },
        )

        response.headers["X-Request-Id"] = rid
        return response
