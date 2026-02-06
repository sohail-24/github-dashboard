from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "github-dashboard"
    app_env: str = "dev"

    github_api_base: str = "https://api.github.com"
    github_token: str | None = None

    http_timeout: int = 10

    class Config:
        env_file = ".env"


settings = Settings()

