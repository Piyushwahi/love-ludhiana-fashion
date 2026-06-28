"""
Love Ludhiana Fashion — Base Repository.

Generic repository implementing the Repository Pattern.
Provides CRUD operations for any SQLAlchemy model.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from sqlalchemy import func, select

from app.database.base import Base

if TYPE_CHECKING:
    import uuid

    from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Generic async repository with CRUD operations.

    Implements the Repository Pattern for data access abstraction.
    All domain-specific repositories should inherit from this class.

    Example:
        class UserRepository(BaseRepository[User]):
            def __init__(self, session: AsyncSession):
                super().__init__(User, session)

            async def find_by_email(self, email: str) -> User | None:
                ...
    """

    def __init__(self, model: type[ModelType], session: AsyncSession) -> None:
        self._model = model
        self._session = session

    async def create(self, **kwargs: Any) -> ModelType:
        """Create a new record."""
        instance = self._model(**kwargs)
        self._session.add(instance)
        await self._session.flush()
        await self._session.refresh(instance)
        return instance

    async def get_by_id(self, record_id: uuid.UUID | int) -> ModelType | None:
        """Get a single record by primary key."""
        return await self._session.get(self._model, record_id)

    async def get_multi(
        self,
        *,
        offset: int = 0,
        limit: int = 20,
        filters: dict[str, Any] | None = None,
        order_by: str | None = None,
        order_desc: bool = True,
    ) -> list[ModelType]:
        """
        Get multiple records with pagination, filtering, and sorting.

        Args:
            offset: Number of records to skip.
            limit: Maximum number of records to return.
            filters: Column-value pairs to filter by.
            order_by: Column name to sort by.
            order_desc: If True, sort descending.

        Returns:
            List of model instances.
        """
        query = select(self._model)

        # Apply filters
        if filters:
            for column_name, value in filters.items():
                if hasattr(self._model, column_name) and value is not None:
                    query = query.where(getattr(self._model, column_name) == value)

        # Apply soft delete filter if model supports it
        if hasattr(self._model, "is_deleted"):
            query = query.where(getattr(self._model, "is_deleted") == False)  # noqa: E712

        # Apply sorting
        if order_by and hasattr(self._model, order_by):
            column = getattr(self._model, order_by)
            query = query.order_by(column.desc() if order_desc else column.asc())

        # Apply pagination
        query = query.offset(offset).limit(limit)

        result = await self._session.execute(query)
        return list(result.scalars().all())

    async def count(self, filters: dict[str, Any] | None = None) -> int:
        """Count records, optionally filtered."""
        query = select(func.count()).select_from(self._model)

        if filters:
            for column_name, value in filters.items():
                if hasattr(self._model, column_name) and value is not None:
                    query = query.where(getattr(self._model, column_name) == value)

        if hasattr(self._model, "is_deleted"):
            query = query.where(getattr(self._model, "is_deleted") == False)  # noqa: E712

        result = await self._session.execute(query)
        return result.scalar_one()

    async def update(
        self,
        record_id: uuid.UUID | int,
        **kwargs: Any,
    ) -> ModelType | None:
        """Update a record by ID."""
        instance = await self.get_by_id(record_id)
        if instance is None:
            return None

        for key, value in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, value)

        await self._session.flush()
        await self._session.refresh(instance)
        return instance

    async def delete(self, record_id: uuid.UUID | int) -> bool:
        """Hard delete a record by ID."""
        instance = await self.get_by_id(record_id)
        if instance is None:
            return False

        await self._session.delete(instance)
        await self._session.flush()
        return True

    async def soft_delete(self, record_id: uuid.UUID | int) -> ModelType | None:
        """
        Soft delete a record by setting is_deleted=True and deleted_at.

        Only works on models with SoftDeleteMixin.
        """
        instance = await self.get_by_id(record_id)
        if instance is None:
            return None

        if not hasattr(instance, "is_deleted"):
            msg = f"{self._model.__name__} does not support soft delete"
            raise AttributeError(msg)

        instance.is_deleted = True  # type: ignore[attr-defined]
        instance.deleted_at = datetime.now(UTC)  # type: ignore[attr-defined]

        await self._session.flush()
        await self._session.refresh(instance)
        return instance

    async def exists(self, record_id: uuid.UUID | int) -> bool:
        """Check if a record exists by ID."""
        query = (
            select(func.count())
            .select_from(self._model)
            .where(self._model.id == record_id)  # type: ignore[attr-defined]
        )
        result = await self._session.execute(query)
        return result.scalar_one() > 0
