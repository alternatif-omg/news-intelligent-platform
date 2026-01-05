import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app.models.news import News


def scrape_dummy_news(db: Session):
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "Dummy News"

    news = News(
        title=title,
        content="Scraped content example",
        source="Web Scraper",
        category="general"
    )

    db.add(news)
    db.commit()
    return 1
 