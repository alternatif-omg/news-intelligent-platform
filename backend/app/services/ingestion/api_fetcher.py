import requests
from sqlalchemy.orm import Session
from app.models.news import News

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "DUMMY_API_KEY"  # nanti pindah ke env


def fetch_news_from_api(db: Session, country="id"):
    params = {
        "apiKey": API_KEY,
        "country": country,
        "pageSize": 5
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if "articles" not in data:
        return 0

    count = 0
    for article in data["articles"]:
        news = News(
            title=article["title"],
            content=article.get("description") or "",
            source=article["source"]["name"],
            category="general"
        )
        db.add(news)
        count += 1

    db.commit()
    return count
