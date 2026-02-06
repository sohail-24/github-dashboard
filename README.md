# GitHub Dashboard

A **production-minded GitHub analytics dashboard** that visualizes repository, contribution, and workflow data using the GitHub API.

This project is built incrementally with a **real-world architecture**, focusing on clean design, scalability, and DevOps best practices.

---

## 🎯 Purpose

The goal of this project is to:

* Practice **production-style system design**
* Work with real data from the GitHub API
* Build a dashboard that is **deployable, observable, and maintainable**
* Demonstrate **backend, frontend, and DevOps integration** in one project

This is **not a demo app** — it is designed as a realistic engineering project.

---

## 🧱 High-Level Architecture

```
Client (Web Dashboard)
        |
        v
Backend API (FastAPI)
        |
        v
GitHub API (REST / GraphQL)
```

Later stages will introduce:

* Caching
* Authentication
* Containerization
* CI/CD
* Kubernetes deployment

---

## 🛠️ Planned Tech Stack

### Backend

* Python
* FastAPI
* GitHub API integration
* Environment-based configuration

### Frontend

* React
* Modern charting library
* Clean, minimal UI

### DevOps (Planned)

* Docker
* GitHub Actions (CI)
* Kubernetes-ready manifests
* GitOps-compatible structure

---

### Backend API

Run locally:

```bash
cd backend
```

```bash
source venv/bin/activate
```

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Swagger UI:
http://<server-ip>:8000/docs


## 📦 Project Structure (Initial)

```
github-dashboard/
├── backend/        # API service
├── frontend/       # Web dashboard
├── docker/         # Container configs
├── k8s/            # Kubernetes manifests
└── README.md
```

Structure will evolve as features are added.

---

## 🚧 Project Status

**Current Phase:** Foundation

* [x] Repository setup
* [x] Project scope defined
* [ ] Backend skeleton
* [ ] Frontend skeleton
* [ ] API integration
* [ ] CI/CD & deployment

Each phase will be built and committed incrementally.

---
## ✅ Current Status

Backend API is live and integrated with GitHub API.

Implemented:
- Health check endpoint
- GitHub repositories API
- Live data fetch from GitHub (repos, stars, language, URLs)

Tested using:
- curl
- Browser access via public IP

Status: Foundation Phase Complete

- Backend container image published to Docker Hub

Docker Image:
sohail28/github-dashboard-backend:1.0


![Build & Push Backend Image]

```bash
(https://github.com/sohail-24/github-dashboard/actions/workflows/docker-backend.yml/badge.svg)
```

## 🔁 CI/CD Pipeline (GitHub Actions)

This repository uses **GitHub Actions** to automatically build and publish the backend Docker image.

### 🚀 What happens on every `push` to `main`?

1. GitHub Actions runner starts
2. Backend Docker image is built from `backend/Dockerfile`
3. Image is tagged using Docker Hub namespace
4. Image is pushed to Docker Hub automatically

### 🐳 Docker Image

```
sohail28/github-dashboard-backend:latest
```

### 🔐 Security

* Docker Hub credentials are stored securely using **GitHub Actions Secrets**
* No secrets are hardcoded in the repository

### 📂 Workflow File

```
.github/workflows/docker-backend.yml
```

This setup ensures:

* Reproducible builds
* Automated container publishing
* Production-ready CI pipeline

📦 Release Strategy

Backend images are versioned using Git tags (vX.Y.Z).
Each release produces:
- Immutable versioned image
- latest tag for convenience


## 📡 API Endpoints

GET /health
→ Service health status

GET /github/repos?username=<github-username>
→ Returns public repositories with metadata



## 📌 Notes

* No hardcoded secrets or tokens
* Configuration via environment variables
* Clean commits with clear intent
* Decisions documented as the project evolves

---

## 👤 Author

Built and maintained by **MD. Sohail**
GitHub: [https://github.com/sohail-24](https://github.com/sohail-24)
