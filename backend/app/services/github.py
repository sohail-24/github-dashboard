import httpx
from app.config import settings
from app.logger import logger


def get_repositories(username: str):
    url = f"{settings.github_api_base}/users/{username}/repos"

    headers = {}
    if settings.github_token:
        headers["Authorization"] = f"Bearer {settings.github_token}"

    logger.info(f"Fetching repos for user={username}")

    try:
        with httpx.Client(timeout=10) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        logger.error(f"GitHub API error: {e}")
        raise

