from fastapi import FastAPI
from app.config import settings
from app.routers import health, github

app = FastAPI(title=settings.app_name)

app.include_router(health.router)
app.include_router(github.router)


@app.get("/")
def root():
    return {
        "message": "GitHub Dashboard API running"
    }

