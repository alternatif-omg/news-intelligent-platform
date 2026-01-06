from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    processed_content = Column(Text)        # tambahan untuk NLP tokens
    source = Column(String(100))
    category = Column(String(50))
    url = Column(String(500))               # untuk link artikel
    image_url = Column(String(500))         # untuk URL gambar
    published_at = Column(DateTime)         # harus datetime, bukan string
    created_at = Column(DateTime, default=datetime.utcnow)
