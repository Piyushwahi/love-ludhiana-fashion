# System Architecture & Enterprise Design

This document details the system design, components, and deployment architecture for **Love Ludhiana Fashion**.

---

## 1. System Architecture Diagram

The platform utilizes a decoupled, three-tier architecture ensuring complete separation of concerns between the React user interface, the FastAPI service layers, and the PostgreSQL storage systems.

```mermaid
graph TD
    %% Clients
    User([Customer / Admin Browser]) -- HTTPS / REST --> Nginx[Nginx Reverse Proxy / Static Serve]
    
    %% Frontend Tier
    subgraph Frontend [React 19 Frontend Tier]
        Nginx -- Serves HTML/JS/CSS --> ReactApp[React App - SPA]
        ReactApp -- Redux Toolkit --> State[State Management]
        ReactApp -- TanStack Query --> APIClient[Axios API Client]
    end

    %% Backend Tier
    subgraph Backend [FastAPI Backend Tier]
        APIClient -- REST API Request --> APIRouter[API Router /api/v1/]
        APIRouter -- Middleware --> SecurityHeaders[Security Headers / CORS]
        SecurityHeaders -- Request Logging --> Logger[Structured JSON Logger]
        Logger -- Auth verification stub --> DI[Dependency Injection Container]
        DI --> ServiceLayer[Service Layer]
        ServiceLayer --> RepoLayer[Repository Layer]
    end

    %% Storage Tier
    subgraph Storage [Storage Tier]
        RepoLayer -- Async Database Session --> Postgres[(PostgreSQL DB)]
        ServiceLayer -- Prepare integration --> Redis[(Redis Cache)]
    end

    %% Third Party Integrations
    subgraph External [External Services]
        ServiceLayer -. Configuration stubs .-> Cloudinary[Cloudinary CDN]
        ServiceLayer -. Configuration stubs .-> Razorpay[Razorpay Payments]
        ServiceLayer -. Configuration stubs .-> Shiprocket[Shiprocket Shipping]
    end

    classDef container fill:#1e293b,stroke:#475569,stroke-width:2px,color:#f8fafc;
    classDef external fill:#0f172a,stroke:#3b82f6,stroke-width:1px,stroke-dasharray: 5 5,color:#93c5fd;
    class Nginx,ReactApp,APIRouter,Postgres,Redis container;
    class Cloudinary,Razorpay,Shiprocket external;
```

---

## 2. Component Diagram (FastAPI Backend)

The backend follows the **Domain-Driven Repository & Service Layer Pattern** for optimal modularity and testability.

```mermaid
classDiagram
    class FastAPI_App {
        +lifespan()
        +middleware_stack()
        +exception_handlers()
    }
    class APIRouter {
        +v1_routes()
        +health_check()
    }
    class DependencyInjection {
        +get_db() AsyncSession
        +get_user_service()
    }
    class BaseService {
        -BaseRepository repository
        +create()
        +get_by_id()
        +get_multi()
        +update()
        +soft_delete()
    }
    class BaseRepository {
        -AsyncSession session
        +create()
        +get_by_id()
        +get_multi()
        +update()
        +delete()
        +soft_delete()
    }
    class SQLAlchemy_Model {
        +UUID id
        +DateTime created_at
        +DateTime updated_at
        +Boolean is_deleted
    }

    FastAPI_App --> APIRouter : routes requests
    APIRouter --> DependencyInjection : resolves
    DependencyInjection --> BaseService : injects
    BaseService --> BaseRepository : delegates data access
    BaseRepository --> SQLAlchemy_Model : interacts with ORM
```

---

## 3. Deployment Diagram (Docker Containers)

Containerized environments ensure parity between local development and cloud production.

```mermaid
graph TB
    Internet([Internet Request]) --> NginxContainer[Nginx Web Server Container<br>Port 80 / 443]
    
    subgraph Docker Network [llf-network Bridge]
        NginxContainer -- SPA Static Files --> StaticMount[Static Asset Volume]
        NginxContainer -- Reverse Proxy /api/v1/health --> FastAPIContainer[FastAPI Backend Container<br>Port 8000]
        FastAPIContainer -- Async TCP --> PostgresContainer[PostgreSQL Container<br>Port 5432]
        FastAPIContainer -- TCP Connection --> RedisContainer[Redis Container<br>Port 6379]
    end

    subgraph Host Storage
        PostgresContainer --> PG_Vol[(llf-postgres-data Volume)]
        RedisContainer --> Redis_Vol[(llf-redis-data Volume)]
    end
```

---

## 4. Database Architecture Diagram

The base model schema design enforces standard attributes across all enterprise tables.

```mermaid
erDiagram
    BASE_MODEL {
        UUID id PK "Indexed, Auto-generated UUID v4"
        TIMESTAMP created_at "Server default now()"
        TIMESTAMP updated_at "On update now()"
        BOOLEAN is_deleted "Default false, Indexed"
        TIMESTAMP deleted_at "Nullable"
    }

    USER ||--o{ ORDER : places
    PRODUCT ||--o{ ORDER_ITEM : contained_in
    ORDER ||--|{ ORDER_ITEM : contains
    USER {
        UUID id PK
        STRING email UK
        STRING password_hash
        STRING role
    }
    PRODUCT {
        UUID id PK
        STRING name
        STRING slug UK
        DECIMAL price
        INTEGER inventory_qty
    }
    ORDER {
        UUID id PK
        UUID user_id FK
        STRING status
        DECIMAL total_amount
    }
```
