"""
Love Ludhiana Fashion — CORS Middleware Configuration.

Configures Cross-Origin Resource Sharing based on settings.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi.middleware.cors import CORSMiddleware

if TYPE_CHECKING:
    from fastapi import FastAPI


def configure_cors(app: FastAPI) -> None:
    """
    Add CORS middleware to the FastAPI application.

    Reads allowed origins from application settings.
    """
    from app.config.settings import get_settings

    settings = get_settings()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=[
            "Authorization",
            "Content-Type",
            "Accept",
            "Origin",
            "X-Requested-With",
            "X-CSRF-Token",
        ],
        expose_headers=[
            "X-Total-Count",
            "X-Page-Count",
            "X-Request-ID",
        ],
        max_age=600,  # Cache preflight for 10 minutes
    )
