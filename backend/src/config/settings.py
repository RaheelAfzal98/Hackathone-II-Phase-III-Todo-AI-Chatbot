from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database settings
    DATABASE_URL: str

    # Auth settings
    BETTER_AUTH_SECRET: str
    BETTER_AUTH_URL: str

    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Todo API"

    # Security settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS settings
    ALLOWED_ORIGINS: List[str] = ["*"]  # In production, specify exact origins

    # Neon PostgreSQL settings
    NEON_DB_URL: str

    class Config:
        env_file = ".env"


settings = Settings()