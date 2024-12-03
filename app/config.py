from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "your_secret_key"

    class Config:
        env_file = ".env"

settings = Settings()
