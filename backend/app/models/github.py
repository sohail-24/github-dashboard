from pydantic import BaseModel
from typing import Optional


class GitHubRepo(BaseModel):
    id: int
    name: str
    full_name: str
    html_url: str
    description: Optional[str] = None
    language: Optional[str] = None
    stargazers_count: int
    forks_count: int

