# Coding Standards & Guidelines

This document details the architectural principles and coding guidelines followed in **Love Ludhiana Fashion**. All contributions must adhere to these standards.

---

## 1. Core Engineering Principles

* **SOLID Principles**: Build single-purpose classes/modules, open to extension but closed to modification, substitutable interfaces, interface segregation, and depend on abstractions.
* **Separation of Concerns**: Logic is segregated cleanly into three tiers (UI → API Service → Database).
* **DRY (Don't Repeat Yourself)**: Abstract reusable business calculations, validation logic, and styling variables.
* **KISS (Keep It Simple, Stupid)**: Write clear, descriptive code instead of complex clever code.

---

## 2. Backend Coding Standards (Python & FastAPI)

### PEP8 Compliance & Type Safety
* All backend code must conform to **PEP8** specifications, enforced via **Ruff** and **Black**.
* Explicit type hinting is required for all function arguments and return signatures. Run `mypy` before committing.
  ```python
  async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
      ...
  ```

### Repository & Service Pattern
* **Repositories**: Abstract SQL interactions and DB dialect operations. Avoid raw session querying inside services.
* **Services**: Encapsulate business logic, validations, mapping, and external API requests. Avoid direct controllers logic here.
* **API Routers**: Controllers that receive requests, invoke service functions, and return schemas. Keep them thin.

### Dependency Injection
* Use FastAPI's `Depends` for managing database sessions and instantiating service instances.
  ```python
  @router.post("/register")
  async def register(
      data: UserCreate,
      db: AsyncSession = Depends(get_db)
  ):
      ...
  ```

---

## 3. Frontend Coding Standards (React & TypeScript)

### React 19 & TypeScript
* Use functional components with explicit TypeScript interfaces for props:
  ```typescript
  interface CardProps {
    title: string;
    description: string;
    onClick?: () => void;
  }
  
  export function Card({ title, description, onClick }: CardProps) {
    ...
  }
  ```
* Avoid using `any`. If a type is unknown or dynamic, type it accordingly or use generic parameters.

### State Management Guidelines
* **Server State**: Use **TanStack Query (React Query)** for server state (caching, loading states, mutations, and pagination). Do not store API responses in Redux.
* **Client UI State**: Use **Redux Toolkit** for cross-component global UI states (theme, sidebars, active filters, auth state).
* **Local Component State**: Use standard React `useState` for state limited to a single component or page.

### CSS Styling & Tailwind
* Utilize **Tailwind CSS v4** classes directly for styling.
* Use the class utility `cn(...)` (using `clsx` + `tailwind-merge`) when applying conditional classes to prevent styling conflicts.
  ```typescript
  className={cn(
    "px-4 py-2 rounded-md transition-colors",
    isActive ? "bg-pink-500 text-white" : "bg-gray-800 text-gray-400"
  )}
  ```
