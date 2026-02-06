import httpx
from app.config import settings
from app.logger import logger


def get_repositories(username: str):
    url = f"{settings.github_api_base}/users/{username}/repos"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    # Add token ONLY if present
    if settings.github_token:
        headers["Authorization"] = f"Bearer {settings.github_token}"

    try:
        with httpx.Client(timeout=settings.http_timeout) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()

    except httpx.HTTPStatusError as e:
        logger.error(f"GitHub API error: {e.response.status_code}")
        raise Exception("GitHub API returned an error")

    except httpx.RequestError as e:
        logger.error(f"Network error calling GitHub: {e}")
        raise Exception("GitHub API unreachable")

