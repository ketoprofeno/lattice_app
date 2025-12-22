from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.core.api import api_router
from app.core.config.settings import settings
from app.core.logging import configure_logging
from app.core.middleware.audit import AuditMiddleware
from app.core.middleware.errors import http_exception_handler

configure_logging()

app = FastAPI(title="Lattice App", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(AuditMiddleware)

# Registrar handler global de HTTPException
app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(api_router)
