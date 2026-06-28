# AI Developer Guide & Architectural Blueprint

This guide serves as a persistent context memory for any AI coding assistant (including myself in future sessions or subagents) working on the **Love Ludhiana Fashion** project. It details the interconnections, files, patterns, and operational instructions of the foundation.

---

## 1. High-Level Flow of the Three-Tier Architecture

```
[React 19 SPA (Vite + TS)] 
       │ (Axios Client with interceptors)
       ▼ [REST HTTPS /api/v1/health]
[Nginx (Reverse Proxy & Static Serve)] (Production)
       │
       ▼
[FastAPI Backend Engine (Uvicorn)]
       │ (Lifespan Startup/Shutdown)
       ├─► [CORS / Request Logging / OWASP Security Headers Middlewares]
       ├─► [Global Exception Handlers (AppException -> JSON)]
       ├─► [Dependency Injection Container (get_db AsyncSession)]
       │
       ▼ [Service Layer]
[BaseService[Model, Repo]] (Business Validation, Transactions)
       │
       ▼ [Repository Layer]
[BaseRepository[Model]] (Async CRUD Queries, soft delete, count)
       │
       ▼ [Database Layer]
[PostgreSQL] (Async Engine via asyncpg driver)
```

---

## 2. Core Backend Components & Connections

### A. Environment & Configuration
* **Config Entry Point**: [settings.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/config/settings.py)
  Loads variables from the environment or `.env` file via Pydantic `BaseSettings`. Contains computed helper properties like `is_development`, `is_production`, and type validation for `CORS_ORIGINS`.
* **Constants**: [constants.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/config/constants.py)
  Declares global constants (page sizes, upload limits, status enums) to avoid magic values.

### B. Database Integration
* **Async Session Factory**: [session.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/database/session.py)
  Creates the `AsyncEngine` (using the `asyncpg` driver for async operations) and declares `async_session_factory` (`async_sessionmaker(class_=AsyncSession)`). It exposes the `get_async_session` dependency generator.
* **Declarative Base**: [base.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/database/base.py)
  Registers the base ORM metadata class `Base` used for schema generation and Alembic auto-detection.
* **Model Mixins**: [mixins.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/database/mixins.py)
  Provides reusable database properties:
  - `UUIDMixin`: UUID v4 primary keys.
  - `TimestampMixin`: Timezone-aware creation and update dates.
  - `SoftDeleteMixin`: Flags records as deleted without physical erasure (`is_deleted`, `deleted_at`).

### C. Data Access Pattern
* **Base Repository**: [base.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/repositories/base.py)
  Declares `BaseRepository[ModelType]` which wraps SQLAlchemy operations (`select`, `insert`, `update`, `delete`) in async methods. It dynamically filters out soft-deleted records (`is_deleted == False`) on multi-gets and counts.
* **Base Service**: [base.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/services/base.py)
  Declares `BaseService[ModelType, RepoType]` wrapping repository queries. Implements common validation patterns, translates missing records to custom `NotFoundException` classes, and structures paginated responses.

### D. Middleware & Request Handling
* **API Entry**: [main.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/main.py)
  Initializes FastAPI, binds exception handlers, registers middleware, and starts lifespan checks (Redis, Cloudinary, Razorpay, Shiprocket startup triggers).
* **Exception Handlers**: [handlers.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/exceptions/handlers.py)
  Converts Pydantic, SQLAlchemy, and custom HTTP exceptions into a standard REST response format: `{"success": false, "error": {"code": "...", "message": "...", "details": {...}}}`.
* **Security Headers**: [security_headers.py](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/backend/app/middleware/security_headers.py)
  Enforces HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), clickjacking defenses (`X-Frame-Options`), and MIME-type protection.

---

## 3. Core Frontend Components & Connections

### A. Build System & Styling
* **Vite Integration**: [vite.config.ts](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/vite.config.ts)
  Integrates Tailwind CSS v4 via `@tailwindcss/vite`.
* **Global CSS styles**: [index.css](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/index.css)
  Imports Tailwind, configures typography variables, and defines brand pastel colors under the `@theme` directive.

### B. Network & Global State
* **Axios API Client**: [api.ts](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/config/api.ts)
  Intercepts outgoing requests to attach authorization headers (`Bearer token`) and handles errors globally via `react-hot-toast` notifications.
* **Redux Store**: [store.ts](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/redux/store.ts)
  Centralized client state. Slices are injected here; UI state (sidebar toggles, themes) is managed by [uiSlice.ts](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/redux/slices/uiSlice.ts).

### C. Layouts, Routing & Rendering
* **Providers Composer**: [AppProviders.tsx](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/providers/AppProviders.tsx)
  Combines Redux, TanStack Query (caching configurations), React Helmet Async (SEO meta headers), and toast notifications.
* **App Shell Layout**: [RootLayout.tsx](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/layouts/RootLayout.tsx)
  Renders basic document layouts and loads Google Fonts (Inter, Playfair Display).
* **Responsive hooks**: [useMediaQuery.ts](file:///C:/Users/ASUS/.gemini/antigravity-ide/scratch/love-ludhiana-fashion/frontend/src/hooks/useMediaQuery.ts)
  Uses modern `useSyncExternalStore` for subscribing to window match queries, preventing rendering issues and hooks errors.

---

## 4. Operational Checklists

To make sure code passes verification:
1. **Linting**:
   - Backend: Run `ruff check app tests` and `black --check app tests`.
   - Frontend: Run `npx eslint .`.
2. **Types**:
   - Backend: Run `mypy app` (ensure generic parameters and explicit `cast` returns match the type definitions).
   - Frontend: Run `npm run build` (which executes `tsc -b && vite build` to check both typescript compilation and bundling).
3. **Docker Dev Stack**:
   - Spin up pgAdmin and Redis Commander: `docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build`.
