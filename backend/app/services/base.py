"""
Love Ludhiana Fashion — Base Service.

Service layer that wraps repository operations with business logic hooks.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar

from app.database.base import Base
from app.exceptions.base import NotFoundException
from app.repositories.base import BaseRepository
from app.schemas.common import PaginatedResponse, PaginationParams

if TYPE_CHECKING:
    import uuid

ModelType = TypeVar("ModelType", bound=Base)
RepoType = TypeVar("RepoType", bound=BaseRepository[Any])


class BaseService(Generic[ModelType, RepoType]):
    """
    Base service implementing common business logic.

    Services sit between API routes and repositories,
    handling validation, authorization, and business rules.

    Example:
        class UserService(BaseService[User, UserRepository]):
            def __init__(self, repository: UserRepository):
                super().__init__(repository)

            async def register(self, data: UserCreate) -> User:
                # Business logic here
                ...
    """

    def __init__(self, repository: RepoType) -> None:
        self._repository: BaseRepository[ModelType] = repository

    async def get_by_id(self, record_id: uuid.UUID | int) -> ModelType:
        """
        Get a record by ID.

        Raises:
            NotFoundException: If the record does not exist.
        """
        instance = await self._repository.get_by_id(record_id)
        if instance is None:
            raise NotFoundException(
                message=f"Record with ID {record_id} not found",
            )
        return instance

    async def get_multi(
        self,
        pagination: PaginationParams,
        filters: dict[str, Any] | None = None,
        order_by: str | None = None,
        order_desc: bool = True,
    ) -> PaginatedResponse[Any]:
        """Get multiple records with pagination."""
        items = await self._repository.get_multi(
            offset=pagination.offset,
            limit=pagination.limit,
            filters=filters,
            order_by=order_by,
            order_desc=order_desc,
        )
        total = await self._repository.count(filters=filters)

        return PaginatedResponse.create(
            items=items,
            total=total,
            params=pagination,
        )

    async def create(self, **kwargs: Any) -> ModelType:
        """Create a new record."""
        return await self._repository.create(**kwargs)

    async def update(self, record_id: uuid.UUID | int, **kwargs: Any) -> ModelType:
        """Update a record by ID."""
        instance = await self._repository.update(record_id, **kwargs)
        if instance is None:
            raise NotFoundException(
                message=f"Record with ID {record_id} not found",
            )
        return instance

    async def delete(self, record_id: uuid.UUID | int) -> bool:
        """Hard delete a record by ID."""
        deleted = await self._repository.delete(record_id)
        if not deleted:
            raise NotFoundException(
                message=f"Record with ID {record_id} not found",
            )
        return True

    async def soft_delete(self, record_id: uuid.UUID | int) -> ModelType:
        """Soft delete a record by ID."""
        instance = await self._repository.soft_delete(record_id)
        if instance is None:
            raise NotFoundException(
                message=f"Record with ID {record_id} not found",
            )
        return instance
