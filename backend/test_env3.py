import os
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

    # OpenRouter API settings
    OPEN_ROUTER_API_KEY: Optional[str] = None

    # OpenAI API settings
    OPENAI_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields to prevent validation errors


# Force reload from .env
settings = Settings(_env_file='.env')

print('DATABASE_URL:', repr(settings.DATABASE_URL))
print('NEON_DB_URL:', repr(settings.NEON_DB_URL))
print('BETTER_AUTH_SECRET:', repr(settings.BETTER_AUTH_SECRET))
print('SECRET_KEY:', repr(settings.SECRET_KEY))