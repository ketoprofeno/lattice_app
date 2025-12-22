from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.request_context import get_request_id


async def http_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "request_id": get_request_id(),
        },
    )
