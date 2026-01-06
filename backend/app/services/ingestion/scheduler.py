# app/services/ingestion/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.ingestion.api_fetcher import fetch_news_from_api
from app.core.database import get_db

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: fetch_news_from_api(get_db()), 'interval', minutes=30)
    scheduler.start()
