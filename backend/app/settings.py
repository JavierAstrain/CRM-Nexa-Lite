import os
from pydantic import BaseModel

def normalize(url: str) -> str:
    if url.startswith("postgres://"):
        return "postgresql+psycopg://" + url.split("://", 1)[1]
    if url.startswith("postgresql://"):
        return "postgresql+psycopg://" + url.split("://", 1)[1]
    return url

class Settings(BaseModel):
    DATABASE_URL: str = normalize(os.getenv("DATABASE_URL", "sqlite:///./nexa.db"))
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "devsecret")
    FRONTEND_ORIGIN: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

settings = Settings()
