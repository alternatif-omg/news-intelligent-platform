from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True)
    word = Column(String(50))
    news_id = Column(Integer, ForeignKey("news.id"))
