from fastapi import APIRouter
from app.modules.health.router import router as health_router
from app.modules.me.router import router as me_router
from app.modules.admin.router import router as admin_router

api_router = APIRouter(prefix="/api")

api_router.include_router(health_router, tags=["health"])
api_router.include_router(me_router, tags=["me"])
api_router.include_router(admin_router, tags=["admin"])
