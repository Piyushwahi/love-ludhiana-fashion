"""
Love Ludhiana Fashion — API v1 Health Check.

System health endpoint for monitoring and load balancers.
"""

from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from typing import Any

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Health Check",
    description="Returns the current health status of the API.",
    response_class=ORJSONResponse,
)
async def health_check() -> dict[str, Any]:
    """
    System health check endpoint.

    Used by:
    - Docker HEALTHCHECK
    - Load balancers
    - Monitoring systems (Prometheus, Grafana)
    - Kubernetes liveness/readiness probes
    """
    return {
        "success": True,
        "status": "healthy",
        "service": "Love Ludhiana Fashion API",
        "version": "0.1.0",
        "timestamp": datetime.now(UTC).isoformat(),
    }


@router.get(
    "/health/ready",
    summary="Readiness Check",
    description="Checks if the application and its dependencies are ready.",
    response_class=ORJSONResponse,
)
async def readiness_check() -> ORJSONResponse:
    """
    Readiness check — verifies database and Redis connectivity.

    Returns degraded status if optional services (Redis) are unavailable.
    """
    checks: dict[str, str] = {}

    # Check database
    try:
        from sqlalchemy import text

        from app.database.session import async_session_factory

        async with async_session_factory() as session:
            await session.execute(text("SELECT 1"))
        checks["database"] = "connected"
    except Exception:
        checks["database"] = "disconnected"

    # Check Redis
    try:
        from app.config.redis import check_redis_health

        redis_ok = await check_redis_health()
        checks["redis"] = "connected" if redis_ok else "disconnected"
    except Exception:
        checks["redis"] = "disconnected"

    # Determine overall status
    db_ok = checks.get("database") == "connected"
    overall = "healthy" if db_ok else "unhealthy"

    status_code = 200 if db_ok else 503

    return ORJSONResponse(
        status_code=status_code,
        content={
            "success": db_ok,
            "status": overall,
            "checks": checks,
            "timestamp": datetime.now(UTC).isoformat(),
        },
    )
