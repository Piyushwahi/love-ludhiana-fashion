"""
Love Ludhiana Fashion — FastAPI Application Factory.

Entry point for the backend application.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.api.router import v1_router
from app.config.constants import API_DESCRIPTION, API_TITLE
from app.config.settings import get_settings
from app.core.events import lifespan
from app.exceptions.handlers import register_exception_handlers
from app.logging.config import setup_logging
from app.middleware.cors import configure_cors
from app.middleware.request_logging import RequestLoggingMiddleware
from app.middleware.security_headers import SecurityHeadersMiddleware


def create_application() -> FastAPI:
    """
    Application factory — creates and configures the FastAPI app.

    Follows the factory pattern for testability and flexibility.
    """
    settings = get_settings()

    # Initialize logging before anything else
    setup_logging(
        log_level=settings.LOG_LEVEL,
        log_format=settings.LOG_FORMAT,
        log_file=settings.LOG_FILE,
    )

    app = FastAPI(
        title=API_TITLE,
        description=API_DESCRIPTION,
        version=settings.APP_VERSION,
        debug=settings.APP_DEBUG,
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        openapi_tags=[
            {"name": "Health", "description": "System health checks"},
            {"name": "Authentication", "description": "Auth endpoints (Part 2)"},
            {"name": "Users", "description": "User management (Part 2)"},
            {"name": "Products", "description": "Product catalog (Part 3)"},
            {"name": "Categories", "description": "Product categories (Part 3)"},
            {"name": "Cart", "description": "Shopping cart (Part 4)"},
            {"name": "Orders", "description": "Order management (Part 4)"},
            {"name": "Payments", "description": "Payment processing (Part 4)"},
            {"name": "Shipping", "description": "Shipping integration (Part 4)"},
            {"name": "Reviews", "description": "Product reviews (Part 5)"},
            {"name": "Admin", "description": "Admin dashboard (Part 5)"},
        ],
        license_info={
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT",
        },
        contact={
            "name": "Love Ludhiana Fashion",
            "email": "dev@loveludhianafashion.com",
        },
    )

    # ── Middleware (order matters — last added = first executed) ──
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(RequestLoggingMiddleware)
    configure_cors(app)

    # Prometheus instrumentation (if available)
    try:
        from prometheus_fastapi_instrumentator import Instrumentator

        Instrumentator(
            should_group_status_codes=True,
            should_ignore_untemplated=True,
            excluded_handlers=["/docs", "/redoc", "/openapi.json", "/metrics"],
        ).instrument(app).expose(app, include_in_schema=False)
    except ImportError:
        pass

    # ── Exception Handlers ───────────────────
    register_exception_handlers(app)

    # ── Routers ──────────────────────────────
    app.include_router(v1_router)

    return app


# Create the application instance
app = create_application()
