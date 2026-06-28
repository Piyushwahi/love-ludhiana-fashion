"""
Love Ludhiana Fashion — Base Response Schemas.

Standard response format for all API endpoints.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class BaseSchema(BaseModel):
    """Base Pydantic schema with common configuration."""

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        str_strip_whitespace=True,
    )


class SuccessResponseSchema(BaseModel, Generic[T]):
    """
    Standard success response wrapper.

    All successful API responses follow this format:
    {
        "success": true,
        "message": "...",
        "data": { ... },
        "timestamp": "..."
    }
    """

    success: bool = True
    message: str = "Request successful"
    data: T | None = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)


class ErrorDetail(BaseModel):
    """Error detail sub-schema."""

    code: str
    message: str
    details: dict[str, Any] | list[Any] = {}


class ErrorResponseSchema(BaseModel):
    """
    Standard error response wrapper.

    All error API responses follow this format:
    {
        "success": false,
        "error": {
            "code": "...",
            "message": "...",
            "details": { ... }
        }
    }
    """

    success: bool = False
    error: ErrorDetail


class BaseResponseSchema(BaseModel, Generic[T]):
    """Generic response schema that can be success or error."""

    success: bool
    message: str | None = None
    data: T | None = None
    error: ErrorDetail | None = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)
