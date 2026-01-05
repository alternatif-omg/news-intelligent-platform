from fastapi import APIRouter

from app.api.v1.routes import health, news, analytics, search

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(news.router, prefix="/news", tags=["News"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(search.router, prefix="/search", tags=["Search"])
