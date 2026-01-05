from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.news import News
from app.models.keyword import Keyword


def get_topic_trends(db: Session):
    return (
        db.query(News.category, func.count(News.id).label("count"))
        .group_by(News.category)
        .all()
    )


def get_top_keywords(db: Session, limit=10):
    return (
        db.query(Keyword.word, func.count(Keyword.id).label("count"))
        .group_by(Keyword.word)
        .order_by(func.count(Keyword.id).desc())
        .limit(limit)
        .all()
    )
