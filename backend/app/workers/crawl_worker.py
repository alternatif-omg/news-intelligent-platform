from sqlalchemy.orm import Session
from app.services.ingestion.api_fetcher import fetch_news_from_api


def run_crawl_worker(db: Session):
    fetch_news_from_api(db)
