"""
Love Ludhiana Fashion — Custom Exception Classes.

Hierarchical exception classes for consistent error handling.
All application exceptions inherit from AppException.
"""

from __future__ import annotations

from typing import Any


class AppException(Exception):
    """
    Base application exception.

    All custom exceptions should inherit from this class.

    Attributes:
        message: Human-readable error message.
        status_code: HTTP status code to return.
        error_code: Machine-readable error code for the frontend.
        details: Additional error context.
    """

    def __init__(
        self,
        message: str = "An unexpected error occurred",
        status_code: int = 500,
        error_code: str = "INTERNAL_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)


class NotFoundException(AppException):
    """Resource not found."""

    def __init__(
        self,
        message: str = "Resource not found",
        error_code: str = "NOT_FOUND",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=404,
            error_code=error_code,
            details=details,
        )


class ConflictException(AppException):
    """Resource conflict (duplicate)."""

    def __init__(
        self,
        message: str = "Resource already exists",
        error_code: str = "CONFLICT",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=409,
            error_code=error_code,
            details=details,
        )


class ValidationException(AppException):
    """Validation error."""

    def __init__(
        self,
        message: str = "Validation error",
        error_code: str = "VALIDATION_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=422,
            error_code=error_code,
            details=details,
        )


class UnauthorizedException(AppException):
    """Authentication required or invalid credentials."""

    def __init__(
        self,
        message: str = "Authentication required",
        error_code: str = "UNAUTHORIZED",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=401,
            error_code=error_code,
            details=details,
        )


class ForbiddenException(AppException):
    """Insufficient permissions."""

    def __init__(
        self,
        message: str = "Insufficient permissions",
        error_code: str = "FORBIDDEN",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=403,
            error_code=error_code,
            details=details,
        )


class DatabaseException(AppException):
    """Database operation error."""

    def __init__(
        self,
        message: str = "Database error",
        error_code: str = "DATABASE_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=500,
            error_code=error_code,
            details=details,
        )


class RateLimitException(AppException):
    """Rate limit exceeded."""

    def __init__(
        self,
        message: str = "Rate limit exceeded. Please try again later.",
        error_code: str = "RATE_LIMIT_EXCEEDED",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=429,
            error_code=error_code,
            details=details,
        )


class ExternalServiceException(AppException):
    """External service (Razorpay, Shiprocket, etc.) error."""

    def __init__(
        self,
        message: str = "External service error",
        error_code: str = "EXTERNAL_SERVICE_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=502,
            error_code=error_code,
            details=details,
        )


class FileValidationException(AppException):
    """Invalid file upload."""

    def __init__(
        self,
        message: str = "Invalid file",
        error_code: str = "FILE_VALIDATION_ERROR",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            status_code=400,
            error_code=error_code,
            details=details,
        )
