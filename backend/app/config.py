from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "GitHub Dashboard API"
    environment: str = "development"

    # 🔑 GitHub
    github_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

