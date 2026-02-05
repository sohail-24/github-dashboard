from fastapi import APIRouter, HTTPException
import requests
from app.config import settings

router = APIRouter(prefix="/github", tags=["github"])


@router.get("/repos")
def list_repos(username: str):
    """
    Fetch public repositories for a GitHub user
    """
    url = f"https://api.github.com/users/{username}/repos"

    headers = {
        "Authorization": f"Bearer {settings.github_token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="GitHub API request failed"
        )

    repos = response.json()

    return [
        {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"],
            "url": repo["html_url"],
        }
        for repo in repos
    ]

