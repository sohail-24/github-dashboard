from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "GitHub Dashboard API"
    app_env: str = "dev"

    # GitHub
    github_token: str | None = None
    github_api_base: str = "https://api.github.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="forbid",   # strict by design
    )


settings = Settings()

