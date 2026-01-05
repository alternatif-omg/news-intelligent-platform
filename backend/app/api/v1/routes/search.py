from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.search.query import search_news
from fastapi import Request, HTTPException
from app.core.security import rate_limit

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search(
    request: Request,
    q: str,
    category: str | None = None,
    db: Session = Depends(get_db)
):
    if not rate_limit(request.client.host):
        raise HTTPException(status_code=429, detail="Too many requests")

    return search_news(db, q, category)
