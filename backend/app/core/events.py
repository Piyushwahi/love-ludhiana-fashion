"""
Love Ludhiana Fashion — Application Lifespan Events.

Startup and shutdown event handlers.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan context manager.

    Handles startup and shutdown events:
    - Startup: Initialize database, Redis, external services, monitoring
    - Shutdown: Close connections and clean up resources
    """
    # ── Startup ──────────────────────────────
    logger.info("🚀 Starting Love Ludhiana Fashion API...")

    from app.config.settings import get_settings

    settings = get_settings()

    # Initialize Cloudinary
    from app.config.cloudinary import init_cloudinary

    init_cloudinary(
        cloud_name=settings.CLOUDINARY_CLOUD_NAME,
        api_key=settings.CLOUDINARY_API_KEY,
        api_secret=settings.CLOUDINARY_API_SECRET,
    )

    # Initialize Razorpay
    from app.config.razorpay import init_razorpay

    init_razorpay(
        key_id=settings.RAZORPAY_KEY_ID,
        key_secret=settings.RAZORPAY_KEY_SECRET,
    )

    # Initialize Shiprocket
    from app.config.shiprocket import init_shiprocket

    init_shiprocket(
        email=settings.SHIPROCKET_EMAIL,
        password=settings.SHIPROCKET_PASSWORD,
        api_url=settings.SHIPROCKET_API_URL,
    )

    # Initialize Redis (connection only, no caching)
    try:
        from app.config.redis import init_redis

        await init_redis(
            redis_url=settings.REDIS_URL,
            max_connections=settings.REDIS_MAX_CONNECTIONS,
        )
    except Exception:
        logger.warning("Redis initialization failed — continuing without Redis")

    # Initialize Sentry (if configured)
    if settings.SENTRY_DSN:
        try:
            import sentry_sdk

            sentry_sdk.init(
                dsn=settings.SENTRY_DSN,
                environment=settings.SENTRY_ENVIRONMENT,
                traces_sample_rate=settings.SENTRY_TRACES_SAMPLE_RATE,
                send_default_pii=False,
            )
            logger.info("Sentry initialized")
        except Exception:
            logger.warning("Sentry initialization failed")

    logger.info(
        "✅ Application started | ENV: %s | DEBUG: %s",
        settings.APP_ENV,
        settings.APP_DEBUG,
    )

    yield

    # ── Shutdown ─────────────────────────────
    logger.info("🔄 Shutting down Love Ludhiana Fashion API...")

    # Close Redis
    try:
        from app.config.redis import close_redis

        await close_redis()
    except Exception:
        logger.warning("Redis shutdown failed")

    # Dispose database engine
    from app.database.session import dispose_engine

    await dispose_engine()

    logger.info("👋 Application shutdown complete")
