from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.news import NewsCreate, NewsResponse
from app.models.news import News
from app.core.database import get_db

router = APIRouter(prefix="/news", tags=["News"])


@router.post("/", response_model=NewsResponse)
def create_news(payload: NewsCreate, db: Session = Depends(get_db)):
    news = News(**payload.dict())
    db.add(news)
    db.commit()
    db.refresh(news)
    return news


@router.get("/", response_model=list[NewsResponse])
def list_news(db: Session = Depends(get_db)):
    return db.query(News).all()
