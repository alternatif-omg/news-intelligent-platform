from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.schemas.news import NewsCreate, NewsResponse
from app.models.news import News
from app.core.database import get_db
from app.services.ingestion.api_fetcher import fetch_news_from_api
from app.services.ingestion.scraper import scrape_dummy_news
from app.workers.crawl_worker import run_crawl_worker
from app.workers.nlp_worker import run_nlp_worker


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

@router.post("/ingest")
def ingest_news(db: Session = Depends(get_db)):
    api_count = fetch_news_from_api(db)
    scrape_count = scrape_dummy_news(db)

    return {
        "api_ingested": api_count,
        "scraped_ingested": scrape_count
    }
    
@router.post("/ingest/async")
def ingest_async(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    background_tasks.add_task(run_crawl_worker, db)
    background_tasks.add_task(run_nlp_worker, db)
    return {"status": "ingestion started"}
