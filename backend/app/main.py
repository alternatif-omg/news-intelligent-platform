from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import Base, engine
from app.models import news

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="News Intelligence Platform",
    description="Internal newsroom analytics system",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "message": "News Intelligence Platform API",
        "env": settings.ENV
    }
