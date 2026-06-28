# Love Ludhiana Fashion — Enterprise E-Commerce Platform

Welcome to the core codebase for **Love Ludhiana Fashion**, an enterprise-grade, highly scalable e-commerce platform designed for a hybrid kids' clothing business (ages 0 to 20 years) operating both physical and online stores.

---

## 🏗️ Architecture & Technology Stack

The platform is designed under a decoupled **Three-Tier Architecture** pattern. The user interface runs completely independently of the backend API servers, facilitating modular scaling and high availability.

### Tech Stack Summary
* **Frontend**: React 19, TypeScript, Vite, Tailwind CSS v4, Redux Toolkit (RTK), React Router v7, Axios, React Hook Form, Zod, TanStack Query (v5), Framer Motion, React Helmet Async, React Hot Toast.
* **Backend**: Python 3.12+, FastAPI, SQLAlchemy 2.0 (Async), Alembic, Pydantic v2, Uvicorn, structlog (Structured JSON Logging).
* **Database**: PostgreSQL (Production) / Redis (Cache Integration Prepared).
* **External Stubs**: Cloudinary (Image CDN), Razorpay (Payments), Shiprocket (Logistics).

---

## 📂 Project Directory Map

* [docker-compose.yml](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docker/docker-compose.yml) — Container coordination configuration.
* [backend/](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/) — FastAPI backend codebase.
* [frontend/](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/) — React 19 Single Page Application.
* [docs/](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docs/) — Architecture and guideline documentation.
* [scripts/](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/scripts/) — Setup and automation utilities.

For a detailed visual guide of the codebase directories, refer to the [Folder Structure Documentation](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docs/folder-structure.md).

---

## 🛠️ Setup & Local Running

Ensure you have **Python 3.12+**, **Node.js 20+**, and **Docker** installed.

### 1. Initialize the Environment
Run the setup script corresponding to your operating system to install dependencies, copy environment configs, and configure pre-commit hooks:

* **Windows PowerShell:**
  ```powershell
  .\scripts\setup.ps1
  ```
  *(See file: [setup.ps1](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/scripts/setup.ps1))*

* **Linux / macOS Bash:**
  ```bash
  ./scripts/setup.sh
  ```
  *(See file: [setup.sh](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/scripts/setup.sh))*

### 2. Run Local Servers (Direct Host)
* **Backend:**
  ```bash
  cd backend
  source .venv/bin/activate
  uvicorn app.main:app --reload
  ```
  *(See entry file: [main.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/main.py))*

* **Frontend:**
  ```bash
  cd frontend
  npm run dev
  ```
  *(See file: [App.tsx](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/App.tsx))*

### 3. Run with Docker Compose
To run the entire platform with database and support tools (pgAdmin, Redis Commander):
```bash
docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build
```
*(See files: [docker-compose.yml](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docker/docker-compose.yml), [docker-compose.dev.yml](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docker/docker-compose.dev.yml))*

---

## 📘 Project Documentation

For deeper details, consult the following architectural and coding standards documents:
1. **Architecture & Diagram Guide**: [architecture.md](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docs/architecture.md)
2. **Development Workflows & Instructions**: [development-guide.md](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docs/development-guide.md)
3. **Coding Standards & Best Practices**: [coding-standards.md](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docs/coding-standards.md)
4. **REST API Versioning & Response Conventions**: [api-standards.md](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/docs/api-standards.md)
5. **Database Seeding and Alembic Guidelines**: [database/README.md](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/database/README.md)
