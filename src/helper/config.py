from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional

BASE_DIR = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):

    OPENROUTER_API_KEY: Optional[str] = None
    HUGGING_FACE_TOKEN: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None
    TAVILY_API_KEY: Optional[str] = None

    APP_NAME: str

    model_config = ConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )


def get_settings():

    return Settings()
