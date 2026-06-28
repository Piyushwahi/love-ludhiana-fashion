# Local Development Guide

Welcome to the development guide for **Love Ludhiana Fashion**. This document guides you through setting up your machine and running the project locally.

---

## 1. Quick Start (One Command)

For quick environment initialization, run the setup script corresponding to your operating system:

**Linux / macOS:**
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

**Windows (PowerShell):**
```powershell
./scripts/setup.ps1
```

The scripts will:
1. Copy `.env.example` configurations to `.env` in both folders.
2. Initialize virtual environments and install Python development dependencies.
3. Install frontend Node modules.
4. Set up local pre-commit hooks for Git code checks.

---

## 2. Local Execution (Without Docker)

To run the application directly on your local system:

### A. Run Backend
1. Navigate to the `backend` directory.
2. Activate your virtual environment:
   ```bash
   # Unix/macOS
   source .venv/bin/activate
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   ```
3. Run the development server with live reload:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. Access the API at [http://localhost:8000](http://localhost:8000).
5. Access the API documentation:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### B. Run Frontend
1. Navigate to the `frontend` directory.
2. Run the Vite development server:
   ```bash
   npm run dev
   ```
3. Access the frontend app at [http://localhost:5173](http://localhost:5173).

---

## 3. Docker Workflow (Recommended)

Docker Compose manages your application services, database (PostgreSQL), and caching layer (Redis) seamlessly.

### A. Run in Development Mode
This builds dev containers with **hot-reload** enabled (via volume mounts) and includes auxiliary management tools like **pgAdmin** and **Redis Commander**.

```bash
# Start all containers in the background
docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build -d

# View logs in real-time
docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml logs -f
```

* **Frontend:** [http://localhost:5173](http://localhost:5173) (Hot reloading active)
* **Backend:** [http://localhost:8000](http://localhost:8000) (Hot reloading active)
* **pgAdmin:** [http://localhost:5050](http://localhost:5050) (Credentials: `admin@loveludhianafashion.com` / `admin`)
* **Redis Commander:** [http://localhost:8081](http://localhost:8081)

### B. Run in Production Mode
This builds minimized, hardened, resource-constrained, non-root production containers ready for deployment.

```bash
docker compose -f docker/docker-compose.yml -f docker/docker-compose.prod.yml up --build -d
```

---

## 4. Code Quality & Formatting Rules

We enforce high code standards prior to allowing commits.

### Pre-commit hooks
Before committing code, verify checks pass:
```bash
# Run against all files manually
pre-commit run --all-files
```

If formatting issues exist, Black/Ruff/Prettier will attempt auto-fixes. Commit again after the fixes.

---

## 5. Running Tests

### Backend Unit Tests
Run backend tests using pytest:
```bash
cd backend
pytest
```
Test coverage report is outputted in `backend/htmlcov/index.html`.
