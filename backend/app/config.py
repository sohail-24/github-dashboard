from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "GitHub Dashboard API"
    environment: str = "development"
    github_token: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()

