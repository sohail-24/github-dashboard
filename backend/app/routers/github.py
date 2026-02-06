from fastapi import APIRouter, HTTPException
from typing import List

from app.services.github import get_repositories
from app.models.github import GitHubRepo
from app.logger import logger

router = APIRouter(prefix="/github", tags=["GitHub"])


@router.get("/repos", response_model=List[GitHubRepo])
def github_repos(username: str):
    try:
        return get_repositories(username)
    except Exception:
        logger.exception("Failed to fetch repositories")
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch data from GitHub API"
        )

