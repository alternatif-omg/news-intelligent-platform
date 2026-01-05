from sqlalchemy.orm import Session
from app.repositories.analytics_repository import (
    get_topic_trends,
    get_top_keywords
)


def analyze_trends(db: Session):
    topics = get_topic_trends(db)
    keywords = get_top_keywords(db)

    return {
        "topic_trends": [
            {"topic": t[0], "count": t[1]} for t in topics
        ],
        "top_keywords": [
            {"keyword": k[0], "count": k[1]} for k in keywords
        ]
    }
