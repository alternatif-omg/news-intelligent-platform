# app/services/analytics/statistics.py
from sqlalchemy.orm import Session
from app.models.news import News

def compute_statistics(db: Session):
    news = db.query(News).all()
    total = len(news)
    categories = {}
    for n in news:
        categories[n.category] = categories.get(n.category, 0) + 1
    average_per_category = total / (len(categories) or 1)
    return {
        "total": total,
        "categories": categories,
        "average_per_category": average_per_category
    }
