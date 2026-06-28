# Love Ludhiana Fashion — Project Foundation Audit & Summary

This document summarizes the complete project foundation setup and describes the interconnections between the frontend React application, backend FastAPI engine, PostgreSQL database, and development tools.

---

## 1. Project Overview & Remote Repository
- **Project Name**: Love Ludhiana Fashion (Kids Clothing Store, 0-20 years)
- **Git Repository URL**: `https://github.com/Piyushwahi/love-ludhiana-fashion.git`
- **Git Init Status**: Initialized locally, remote origin configured successfully.

---

## 2. Decoupled Three-Tier Architecture

The platform uses a decoupled three-tier architecture ensuring complete separation of concerns between UI, API, and Database:

### Tier 1: Frontend SPA
- **Tech Stack**: React 19 + Vite + TypeScript + Tailwind CSS v4.
- **State Management**: Redux Toolkit (RTK) for UI/global client states, TanStack Query for server cache.
- **Client Configuration**: Pre-configured Axios instance ([api.ts](file:///p:/love-ludhiana-fashion/frontend/src/config/api.ts)) with interceptors that append authorization tokens and toast unhandled error messages automatically.

### Tier 2: FastAPI REST API
- **Tech Stack**: Python 3.11+ + FastAPI + Pydantic v2 + Uvicorn.
- **Database Access Pattern**: Decoupled using **Repository Pattern** and **Service Layer** for modularity and testability:
  - [BaseRepository](file:///p:/love-ludhiana-fashion/backend/app/repositories/base.py): Encapsulates async CRUD queries (using SQLAlchemy's async engines) and automatically handles soft-delete filtering.
  - [BaseService](file:///p:/love-ludhiana-fashion/backend/app/services/base.py): Encapsulates business validation rules, wraps repository calls, and formats standard paginated responses.
- **Exception Handlers**: [handlers.py](file:///p:/love-ludhiana-fashion/backend/app/exceptions/handlers.py) intercepts database constraint errors, schema validations, and custom API exceptions to yield standardized error payloads.
- **Middlewares**: Enforces CORS parameters, request execution time logging, and OWASP-compliant security headers (CSP, HSTS, X-Frame-Options).

### Tier 3: PostgreSQL Database
- **Connection URI**: `postgresql+asyncpg://postgres:Wahi2004@localhost:5432/love_ludhiana`
- **Driver**: `asyncpg` for non-blocking database I/O.
- **ORMs & Migrations**: SQLAlchemy 2.0 async engines, models utilizing Mixins (`UUIDMixin`, `TimestampMixin`, `SoftDeleteMixin`), and Alembic for async-configured database migration management.

---

## 3. Local Audit & Code Quality Metrics

Every check has been run and fixed automatically:
- **FastAPI compilation & startup**: Verified, compiles and executes cleanly.
- **pytest suite**: Completed successfully, health checks pass.
- **MyPy Static Type Safety**: 100% success (0 errors found in 67 source files).
- **Ruff Linting**: All checks passed (line lengths, commented-out code, type-import blocks resolved).
- **Black formatting**: Applied format auto-fixes to settings, repositories, and services.
- **isort**: Imports sorted cleanly.
- **Frontend typescript compilation (`tsc`)**: Compiled successfully.
- **Vite build pipeline**: Successfully generated minimized build chunk distributions in `frontend/dist/`.
- **Frontend ESLint Flat Config**: All checks passed (refactored responsive `useMediaQuery` hook using `useSyncExternalStore` to prevent cascading render warnings).
- **Docker Compose Configurations**: Dev Compose (includes pgAdmin and Redis Commander) and Production Compose syntactically verified.
- **pre-commit Hooks**: Configured for local git checks.

---

## 4. Architectural Maps & Developer Guides

Detailed guides can be found in the repository:
1. **AI Developer Blueprint**: [AI_DEVELOPER_GUIDE.md](file:///p:/love-ludhiana-fashion/docs/AI_DEVELOPER_GUIDE.md)
2. **Mermaid System Diagrams**: [architecture.md](file:///p:/love-ludhiana-fashion/docs/architecture.md)
3. **Local setup, script executions & Docker guide**: [development-guide.md](file:///p:/love-ludhiana-fashion/docs/development-guide.md)
4. **Folder hierarchy documentation**: [folder-structure.md](file:///p:/love-ludhiana-fashion/docs/folder-structure.md)
5. **Coding & naming standards specifications**: [coding-standards.md](file:///p:/love-ludhiana-fashion/docs/coding-standards.md)
6. **REST endpoints & response JSON structures**: [api-standards.md](file:///p:/love-ludhiana-fashion/docs/api-standards.md)
7. **Database migrations guide**: [database/README.md](file:///p:/love-ludhiana-fashion/database/README.md)
