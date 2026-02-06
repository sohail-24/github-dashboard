
from fastapi import FastAPI
import os

app = FastAPI(title="GitHub Dashboard API")

APP_VERSION = os.getenv("APP_VERSION", "dev")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {
        "service": "github-dashboard-backend",
        "version": APP_VERSION
    }

