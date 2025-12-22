from __future__ import annotations

import contextvars

request_id_ctx = contextvars.ContextVar("request_id", default=None)


def set_request_id(value: str | None) -> None:
    request_id_ctx.set(value)


def get_request_id() -> str | None:
    return request_id_ctx.get()
