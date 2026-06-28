"""
Love Ludhiana Fashion — Structured Logging Configuration.

Sets up JSON structured logging with separate handlers for:
- Application logs
- Request logs
- Error logs
- Audit logs

Supports log rotation and configurable log levels.
"""

from __future__ import annotations

from typing import Any

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

import structlog


def setup_logging(
    log_level: str = "DEBUG",
    log_format: str = "json",
    log_file: str = "logs/app.log",
) -> None:
    """
    Configure structured logging for the application.

    Args:
        log_level: Minimum log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        log_format: Output format — "json" for structured, "console" for human-readable.
        log_file: Path to the main log file.
    """
    # Create log directory
    log_dir = Path(log_file).parent
    log_dir.mkdir(parents=True, exist_ok=True)

    # Configure structlog
    shared_processors: list[structlog.types.Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
    ]

    renderer: Any
    if log_format == "json":
        renderer = structlog.processors.JSONRenderer()
    else:
        renderer = structlog.dev.ConsoleRenderer()

    structlog.configure(
        processors=[
            *shared_processors,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    formatter = structlog.stdlib.ProcessorFormatter(
        processor=renderer,
        foreign_pre_chain=shared_processors,
    )

    # ── Root Logger ──────────────────────────
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level.upper(), logging.DEBUG))

    # Clear existing handlers
    root_logger.handlers.clear()

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(getattr(logging, log_level.upper(), logging.DEBUG))
    root_logger.addHandler(console_handler)

    # ── Application Log File ─────────────────
    app_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
        encoding="utf-8",
    )
    app_handler.setFormatter(formatter)
    app_handler.setLevel(logging.DEBUG)
    root_logger.addHandler(app_handler)

    # ── Error Log File ───────────────────────
    error_log = log_dir / "error.log"
    error_handler = RotatingFileHandler(
        filename=str(error_log),
        maxBytes=10 * 1024 * 1024,
        backupCount=10,
        encoding="utf-8",
    )
    error_handler.setFormatter(formatter)
    error_handler.setLevel(logging.ERROR)
    root_logger.addHandler(error_handler)

    # ── Request Log File ─────────────────────
    request_logger = logging.getLogger("app.requests")
    request_handler = RotatingFileHandler(
        filename=str(log_dir / "requests.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    request_handler.setFormatter(formatter)
    request_logger.addHandler(request_handler)

    # ── Audit Log File ───────────────────────
    audit_logger = logging.getLogger("app.audit")
    audit_handler = RotatingFileHandler(
        filename=str(log_dir / "audit.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=20,  # Keep more audit history
        encoding="utf-8",
    )
    audit_handler.setFormatter(formatter)
    audit_logger.addHandler(audit_handler)

    # Suppress noisy third-party loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(
        logging.DEBUG if log_level == "DEBUG" else logging.WARNING
    )

    logging.info("Logging configured | Level: %s | Format: %s", log_level, log_format)
