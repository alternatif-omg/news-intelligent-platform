from collections import defaultdict
from sqlalchemy.orm import Session
from app.models.news import News


def build_index(db: Session):
    index = defaultdict(list)

    news_list = db.query(News).all()
    for news in news_list:
        for word in news.content.split():
            index[word].append(news.id)

    return index
