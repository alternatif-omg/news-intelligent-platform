from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.search.query import search_news

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/")
def search(
    q: str = Query(..., min_length=2),
    category: str | None = None,
    db: Session = Depends(get_db)
):
    return search_news(db, q, category)
