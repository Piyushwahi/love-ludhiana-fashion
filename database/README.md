# Database Migrations & Seed Management

This directory contains database documentation, schemas, and configurations for **Love Ludhiana Fashion**. We use **SQLAlchemy 2.0** ORM and **Alembic** for schema migrations.

---

## 1. Migration Commands (Alembic)

Migrations are run from the `backend` directory.

### Initialize/Apply Migrations
To update your database to the latest schema version:
```bash
# Activate your backend virtual environment first
cd backend
alembic upgrade head
```

### Generate a New Migration
When you create or update SQLAlchemy models, generate a new migration script:
```bash
cd backend
alembic revision --autogenerate -m "description_of_changes"
```
Review the generated file in `backend/migrations/versions/` to verify correctness.

### Revert a Migration
To roll back the last migration step:
```bash
cd backend
alembic downgrade -1
```

---

## 2. Seed Data Management

Seed configurations and data structures reside under `database/seeds/`.

* Seed data is formatted as static JSON documents under `database/seeds/` corresponding to tables (e.g. `categories.json`, `brands.json`).
* In future phases, seed scripts will read these files to hydrate PostgreSQL with baseline values (categories, product attributes, base administrative credentials) on initial workspace setups.
