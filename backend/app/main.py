from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# IMPORT ROUTERS
from app.routers.github import router as github_router

app = FastAPI(title="GitHub Dashboard API")

# -----------------------------
# CORS CONFIGURATION
# -----------------------------
# Read allowed origins from environment
# Example value: "http://localhost,http://frontend"
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")

if CORS_ORIGINS == "*":
    allow_origins = ["*"]
else:
    allow_origins = [origin.strip() for origin in CORS_ORIGINS.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# APP METADATA
# -----------------------------
APP_VERSION = os.getenv("APP_VERSION", "dev")

# -----------------------------
# CORE ROUTES
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {
        "service": "github-dashboard-backend",
        "version": APP_VERSION
    }

# -----------------------------
# FEATURE ROUTES
# -----------------------------
app.include_router(
    github_router,
    prefix="/github",
    tags=["GitHub"]
)

