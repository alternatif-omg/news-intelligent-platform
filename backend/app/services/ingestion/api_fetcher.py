import requests
from sqlalchemy.orm import Session
from app.models.news import News
from app.models.keyword import Keyword
from app.services.nlp.preprocessing import preprocess_text
from app.services.nlp.keyword_extraction import extract_keywords
from app.services.nlp.topic_modeling import detect_topic


NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "DUMMY_API_KEY"  


def fetch_news_from_api(db: Session, country="id"):
    params = {
        "apiKey": API_KEY,
        "country": country,
        "pageSize": 5
    }

    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code != 200:
        return 0

    data = response.json()
    articles = data.get("articles", [])
    if not articles:
        return 0

    count = 0
    for article in articles:
        tokens = preprocess_text(article.get("description") or "")
        if not tokens:
            continue

        topic = detect_topic(tokens)

        news = News(
            title=article.get("title", "Untitled"),
            content=" ".join(tokens),
            source=article["source"]["name"] if article.get("source") else None,
            category=topic
        )

        db.add(news)
        db.flush()  # 🔥 penting: supaya news.id tersedia

        keywords = extract_keywords([tokens])[0]
        for word in keywords:
            db.add(Keyword(word=word, news_id=news.id))

        count += 1

    db.commit()
    return count
