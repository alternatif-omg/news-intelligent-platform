from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.analytics.trend_analysis import analyze_trends

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/trends")
def get_trends(db: Session = Depends(get_db)):
    return analyze_trends(db)
