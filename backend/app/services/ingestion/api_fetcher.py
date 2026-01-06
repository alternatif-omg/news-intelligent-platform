from app.core.config import NEWS_SOURCES
import requests
from sqlalchemy.orm import Session
from app.models.news import News
from app.models.keyword import Keyword
from app.services.nlp.preprocessing import preprocess_text
from app.services.nlp.keyword_extraction import extract_keywords
from app.services.nlp.topic_modeling import detect_topic
from dateutil import parser


def fetch_news_from_api(db: Session, limit_per_source: int = 5):
    total_ingested = 0

    for src, url in NEWS_SOURCES.items():
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            payload = response.json()
        except Exception as e:
            print(f"[{src}] Error fetching: {e}")
            continue

        # Pastikan 'data' ada
        articles = payload.get("data") or []
        if not isinstance(articles, list) or not articles:
            print(f"[{src}] No articles")
            continue

        for item in articles[:limit_per_source]:
            text = item.get("content") or item.get("title")
            if not text:
                continue

            # Preprocessing
            tokens = preprocess_text(text)
            if not tokens:
                tokens = text.lower().split()

            topic = detect_topic(tokens) if tokens else "general"

            # Parse isoDate ke datetime
            published_at = None
            iso_date = item.get("isoDate")
            if iso_date:
                try:
                    published_at = parser.isoparse(iso_date)
                except Exception:
                    published_at = None

            news = News(
                title=item.get("title", "Untitled"),
                content=text,
                processed_content=" ".join(tokens),
                source=src,
                category=topic,
                url=item.get("link"),
                image_url=(item.get("image") or {}).get("medium"),
                published_at=published_at
            )

            db.add(news)
            db.flush()

            # Extract keywords
            if tokens:
                keywords = extract_keywords([tokens])[0]
                for word in keywords:
                    db.add(Keyword(word=word, news_id=news.id))

            total_ingested += 1

        db.commit()
        print(f"[{src}] Ingested {min(limit_per_source, len(articles))} articles")

    print(f"Total ingested from all sources: {total_ingested}")
    return total_ingested
