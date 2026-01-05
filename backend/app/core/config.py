from pydantic import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    app_name: str = "News Intelligence Platform"

    database_url: str
    redis_host: str = "localhost"
    redis_port: int = 6379
    news_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
