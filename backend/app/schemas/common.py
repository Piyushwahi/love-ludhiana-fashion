"""
Love Ludhiana Fashion — Common Schemas.

Pagination, filtering, sorting, and search schemas.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

from app.config.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, MIN_PAGE_SIZE

T = TypeVar("T")


class SortOrder(StrEnum):
    """Sort order options."""

    ASC = "asc"
    DESC = "desc"


class PaginationParams(BaseModel):
    """Query parameters for pagination."""

    page: int = Field(default=1, ge=1, description="Page number (1-indexed)")
    page_size: int = Field(
        default=DEFAULT_PAGE_SIZE,
        ge=MIN_PAGE_SIZE,
        le=MAX_PAGE_SIZE,
        description="Number of items per page",
    )

    @property
    def offset(self) -> int:
        """Calculate offset for database query."""
        return (self.page - 1) * self.page_size

    @property
    def limit(self) -> int:
        """Alias for page_size."""
        return self.page_size


class SortParams(BaseModel):
    """Query parameters for sorting."""

    sort_by: str = Field(default="created_at", description="Field to sort by")
    sort_order: SortOrder = Field(
        default=SortOrder.DESC, description="Sort order (asc/desc)"
    )


class FilterParams(BaseModel):
    """Query parameters for filtering and search."""

    search: str | None = Field(default=None, description="Search query string")
    is_active: bool | None = Field(default=None, description="Filter by active status")


class PaginationMeta(BaseModel):
    """Pagination metadata included in paginated responses."""

    page: int
    page_size: int
    total_items: int
    total_pages: int
    has_next: bool
    has_previous: bool

    model_config = ConfigDict(from_attributes=True)


class PaginatedResponse(BaseModel, Generic[T]):
    """
    Standardized paginated response.

    Example response:
    {
        "success": true,
        "message": "Items retrieved successfully",
        "data": [...],
        "pagination": {
            "page": 1,
            "page_size": 20,
            "total_items": 150,
            "total_pages": 8,
            "has_next": true,
            "has_previous": false
        }
    }
    """

    success: bool = True
    message: str = "Items retrieved successfully"
    data: list[T] = []
    pagination: PaginationMeta

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def create(
        cls,
        items: list[T],
        total: int,
        params: PaginationParams,
        message: str = "Items retrieved successfully",
    ) -> PaginatedResponse[T]:
        """Factory method to create a paginated response."""
        total_pages = (total + params.page_size - 1) // params.page_size
        return cls(
            message=message,
            data=items,
            pagination=PaginationMeta(
                page=params.page,
                page_size=params.page_size,
                total_items=total,
                total_pages=total_pages,
                has_next=params.page < total_pages,
                has_previous=params.page > 1,
            ),
        )
