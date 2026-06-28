"""
Love Ludhiana Fashion — Request Logging Middleware.

Logs every incoming request and outgoing response with timing.
"""

from __future__ import annotations

import logging
import time
import uuid
from typing import TYPE_CHECKING

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

if TYPE_CHECKING:
    from starlette.requests import Request
    from starlette.responses import Response

logger = logging.getLogger("app.requests")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that logs request/response details.

    Logs:
    - Request method, path, client IP
    - Response status code
    - Processing duration in milliseconds
    - Unique request ID for tracing
    """

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Process request and log details."""
        request_id = str(uuid.uuid4())[:8]
        start_time = time.perf_counter()

        # Attach request ID to request state
        request.state.request_id = request_id

        # Log incoming request
        logger.info(
            "→ %s %s | Client: %s | ID: %s",
            request.method,
            request.url.path,
            request.client.host if request.client else "unknown",
            request_id,
        )

        try:
            response = await call_next(request)
        except Exception:
            duration_ms = (time.perf_counter() - start_time) * 1000
            logger.exception(
                "✗ %s %s | 500 | %.1fms | ID: %s",
                request.method,
                request.url.path,
                duration_ms,
                request_id,
            )
            raise

        duration_ms = (time.perf_counter() - start_time) * 1000

        # Add request ID to response headers
        response.headers["X-Request-ID"] = request_id

        # Log response
        log_fn = logger.info if response.status_code < 400 else logger.warning
        log_fn(
            "← %s %s | %d | %.1fms | ID: %s",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
            request_id,
        )

        return response
