from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  #
    )
    
    DATABASE_URL: str
    DEBUG: bool = False

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()