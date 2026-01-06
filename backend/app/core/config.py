from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App
    app_env: str = "development"
    app_name: str = "News Intelligence Platform"

    # Database
    database_url: str

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379

    # Base URL Berita Indo API
    berita_indo_api_url: str = "https://berita-indo-api.vercel.app/"

    # Opsional untuk NewsAPI.org atau API berbayar
    news_api_key: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()

# ----------------------------
# Dictionary semua source berita
# Bisa dipakai langsung di fetch_news_from_api
# ----------------------------
NEWS_SOURCES = {
    "okezone": f"{settings.berita_indo_api_url}v1/okezone-news",
    "cnn": f"{settings.berita_indo_api_url}v1/cnn-news/",
    "cnbc": f"{settings.berita_indo_api_url}v1/cnbc-news/",
    "republika": f"{settings.berita_indo_api_url}v1/republika-news/",
    "tempo": f"{settings.berita_indo_api_url}v1/tempo-news/",
    "antara": f"{settings.berita_indo_api_url}v1/antara-news/",
    "bbc": f"{settings.berita_indo_api_url}v1/bbc-news",
    "kumparan": f"{settings.berita_indo_api_url}v1/kumparan-news",
    "liputan6": f"{settings.berita_indo_api_url}v1/liputan6-news",
    "tribun": f"{settings.berita_indo_api_url}v1/tribun-news",
    "jawa_pos": f"{settings.berita_indo_api_url}v1/jawa-pos",
    "vice": f"{settings.berita_indo_api_url}v1/vice",
    "suara": f"{settings.berita_indo_api_url}v1/suara",
    "voa": f"{settings.berita_indo_api_url}v1/voa",
}
