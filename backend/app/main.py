from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.api import api_router
from app.core.config.settings import settings

app = FastAPI(title="Lattice App", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
