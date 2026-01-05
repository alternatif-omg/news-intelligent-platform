from sqlalchemy.orm import Session
from app.models.news import News
from app.services.search.indexing import build_index
from app.core.cache import get_cache, set_cache


def search_news(db, query, category=None):
    cache_key = f"search:{query}:{category}"
    cached = get_cache(cache_key)
    if cached:
        return cached

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

    result = [
        {"id": n.id, "title": n.title, "category": n.category}
        for n in q.all()
    ]

    set_cache(cache_key, result, ttl=60)
    return result

