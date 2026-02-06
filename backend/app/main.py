from fastapi import FastAPI, HTTPException, Query
import logging

from app.services.github import get_repositories

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("github-dashboard")

app = FastAPI(title="GitHub Dashboard API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/github/repos")
def github_repos(
    username: str = Query(..., description="GitHub username")
):
    try:
        return get_repositories(username)

    except Exception:
        logger.exception("Failed to fetch repositories")
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch data from GitHub API",
        )

