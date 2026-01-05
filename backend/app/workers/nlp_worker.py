from sqlalchemy.orm import Session
from app.models.news import News
from app.models.keyword import Keyword
from app.services.nlp.preprocessing import preprocess_text
from app.services.nlp.keyword_extraction import extract_keywords
from app.services.nlp.topic_modeling import detect_topic


def run_nlp_worker(db: Session):
    news_list = db.query(News).filter(News.category == None).all()

    for news in news_list:
        tokens = preprocess_text(news.content)
        if not tokens:
            continue

        news.category = detect_topic(tokens)

        keywords = extract_keywords([tokens])[0]
        for word in keywords:
            db.add(Keyword(word=word, news_id=news.id))

    db.commit()
