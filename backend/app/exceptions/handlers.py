"""
Love Ludhiana Fashion — Global Exception Handlers.

Registers FastAPI exception handlers for consistent error responses.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.exceptions.base import AppException

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = logging.getLogger(__name__)


def _error_response(
    status_code: int,
    message: str,
    error_code: str,
    details: dict[str, Any] | list[Any] | None = None,
) -> ORJSONResponse:
    """Build a standardized error response."""
    return ORJSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": {
                "code": error_code,
                "message": message,
                "details": details or {},
            },
        },
    )


async def app_exception_handler(
    request: Request,
    exc: AppException,
) -> ORJSONResponse:
    """Handle all AppException subclasses."""
    logger.error(
        "AppException: %s | Code: %s | Path: %s",
        exc.message,
        exc.error_code,
        request.url.path,
        extra={"error_code": exc.error_code, "details": exc.details},
    )
    return _error_response(
        status_code=exc.status_code,
        message=exc.message,
        error_code=exc.error_code,
        details=exc.details,
    )


async def http_exception_handler(
    request: Request,
    exc: HTTPException,
) -> ORJSONResponse:
    """Handle FastAPI HTTPException."""
    logger.warning(
        "HTTPException: %s | Status: %d | Path: %s",
        exc.detail,
        exc.status_code,
        request.url.path,
    )
    return _error_response(
        status_code=exc.status_code,
        message=str(exc.detail),
        error_code="HTTP_ERROR",
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> ORJSONResponse:
    """Handle Pydantic request validation errors."""
    errors = []
    for error in exc.errors():
        errors.append(
            {
                "field": " → ".join(str(loc) for loc in error["loc"]),
                "message": error["msg"],
                "type": error["type"],
            }
        )

    logger.warning(
        "Validation error on %s: %d issues",
        request.url.path,
        len(errors),
    )
    return _error_response(
        status_code=422,
        message="Request validation failed",
        error_code="VALIDATION_ERROR",
        details=errors,
    )


async def pydantic_validation_handler(
    request: Request,
    exc: ValidationError,
) -> ORJSONResponse:
    """Handle Pydantic model validation errors."""
    logger.warning("Pydantic validation error on %s", request.url.path)
    return _error_response(
        status_code=422,
        message="Data validation failed",
        error_code="VALIDATION_ERROR",
        details=exc.errors(),
    )


async def sqlalchemy_exception_handler(
    request: Request,
    exc: SQLAlchemyError,
) -> ORJSONResponse:
    """Handle SQLAlchemy database errors."""
    logger.exception(
        "Database error on %s: %s",
        request.url.path,
        str(exc),
    )
    return _error_response(
        status_code=500,
        message="A database error occurred",
        error_code="DATABASE_ERROR",
    )


async def integrity_exception_handler(
    request: Request,
    exc: IntegrityError,
) -> ORJSONResponse:
    """Handle database integrity constraint violations."""
    logger.error(
        "Integrity error on %s: %s",
        request.url.path,
        str(exc.orig),
    )
    return _error_response(
        status_code=409,
        message="A conflict occurred. The resource may already exist.",
        error_code="INTEGRITY_ERROR",
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
) -> ORJSONResponse:
    """Catch-all handler for unhandled exceptions."""
    logger.exception(
        "Unhandled exception on %s: %s",
        request.url.path,
        str(exc),
    )
    return _error_response(
        status_code=500,
        message="An unexpected error occurred",
        error_code="INTERNAL_ERROR",
    )


def register_exception_handlers(app: FastAPI) -> None:
    """Register all exception handlers with the FastAPI application."""
    app.add_exception_handler(AppException, app_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(HTTPException, http_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(ValidationError, pydantic_validation_handler)  # type: ignore[arg-type]
    app.add_exception_handler(IntegrityError, integrity_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(Exception, unhandled_exception_handler)
