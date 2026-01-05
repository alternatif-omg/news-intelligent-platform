from sqlalchemy.orm import Session
from app.models.news import News
from app.services.search.indexing import build_index


def search_news(
    db: Session,
    query: str,
    category: str | None = None
):
    index = build_index(db)
    keywords = query.lower().split()

    matched_ids = set()
    for word in keywords:
        matched_ids.update(index.get(word, []))

    if not matched_ids:
        return []

    q = db.query(News).filter(News.id.in_(matched_ids))

    if category:
        q = q.filter(News.category == category)

    return q.all()
