"""
Love Ludhiana Fashion — Dependency Injection.

FastAPI dependency functions for injecting services and sessions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.database.session import async_session_factory

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Provide an async database session via dependency injection.

    Usage:
        @router.get("/items")
        async def list_items(db: AsyncSession = Depends(get_db)):
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


# ── Service dependencies will be added per feature module ──
# Example (to be implemented in Part 2+):
#
# async def get_user_service(
#     db: AsyncSession = Depends(get_db),
# ) -> UserService:
#     repository = UserRepository(db)
#     return UserService(repository)
