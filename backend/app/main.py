from fastapi import FastAPI
from app.core.api import api_router

app = FastAPI(
    title="Lattice App",
    version="0.1.0"
)

app.include_router(api_router)
