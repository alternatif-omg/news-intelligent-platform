import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app.models.news import News
from app.models.keyword import Keyword
from app.services.nlp.preprocessing import preprocess_text
from app.services.nlp.keyword_extraction import extract_keywords
from app.services.nlp.topic_modeling import detect_topic


def scrape_dummy_news(db: Session):
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    base_title = soup.title.string if soup.title else "Dummy News"

    
    samples = [
        (
            f"{base_title} - Teknologi",
            "AI dan startup mendorong inovasi teknologi digital"
        ),
        (
            f"{base_title} - Ekonomi",
            "Inflasi dan pasar global mempengaruhi ekonomi nasional"
        ),
        (
            f"{base_title} - Olahraga",
            "Pemain mencetak gol di liga nasional"
        ),
    ]

    count = 0
    for title, raw_content in samples:
        tokens = preprocess_text(raw_content)
        topic = detect_topic(tokens)

        news = News(
            title=title,
            content=" ".join(tokens),
            source="Web Scraper",
            category=topic
        )

        db.add(news)
        db.flush()  # supaya news.id tersedia

        keywords = extract_keywords([tokens])[0]
        for word in keywords:
            db.add(Keyword(word=word, news_id=news.id))

        count += 1

    db.commit()
    return count
