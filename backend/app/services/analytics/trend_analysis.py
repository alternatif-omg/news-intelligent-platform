from app.core.cache import get_cache, set_cache
from app.repositories.analytics_repository import (
    get_topic_trends,
    get_top_keywords
)


def analyze_trends(db):
    cache_key = "analytics:trends"
    cached = get_cache(cache_key)
    if cached:
        return cached

    topics = get_topic_trends(db)
    keywords = get_top_keywords(db)

    result = {
        "topic_trends": [
            {"topic": t[0], "count": t[1]} for t in topics
        ],
        "top_keywords": [
            {"keyword": k[0], "count": k[1]} for k in keywords
        ]
    }

    set_cache(cache_key, result, ttl=120)
    return result

