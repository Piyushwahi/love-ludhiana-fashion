"""
Love Ludhiana Fashion — Database Session Management.

Async database engine and session factory with connection pooling.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import get_settings

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

settings = get_settings()

# ── Engine Configuration ─────────────────────
_engine_kwargs: dict[str, Any] = {
    "url": settings.DATABASE_URL,
    "echo": settings.DATABASE_ECHO,
    "pool_size": settings.DATABASE_POOL_SIZE,
    "max_overflow": settings.DATABASE_MAX_OVERFLOW,
    "pool_timeout": settings.DATABASE_POOL_TIMEOUT,
    "pool_recycle": settings.DATABASE_POOL_RECYCLE,
    "pool_pre_ping": True,  # Verify connections before use
}

engine = create_async_engine(**_engine_kwargs)

# ── Session Factory ──────────────────────────
async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


def get_engine() -> AsyncEngine:
    """Get the async database engine."""
    return engine


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that provides an async database session.

    Yields an AsyncSession that is automatically closed after use.
    Use as a FastAPI dependency:

        @router.get("/items")
        async def get_items(db: AsyncSession = Depends(get_async_session)):
            ...
    """
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def dispose_engine() -> None:
    """Dispose of the database engine and all connections."""
    await engine.dispose()
