from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/news_db"
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = Settings()
