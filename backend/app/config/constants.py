"""
Love Ludhiana Fashion — Application Constants.

Centralized constants used across the application.
"""

from __future__ import annotations

# ── API Versioning ───────────────────────────
API_V1_PREFIX = "/api/v1"
API_TITLE = "Love Ludhiana Fashion API"
API_DESCRIPTION = """
🛍️ **Love Ludhiana Fashion** — Enterprise E-Commerce API

Kids Clothing Store (0-20 Years) | Physical Store + Online Store

## Features
- 🔐 JWT & OAuth Authentication
- 👕 Product Catalog Management
- 🛒 Shopping Cart & Wishlist
- 📦 Order Management
- 💳 Razorpay Payment Integration
- 🚚 Shiprocket Shipping Integration
- 📊 Analytics & Dashboard
- 🔔 Notifications

## API Documentation
- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`
- **OpenAPI JSON**: `/openapi.json`
"""

# ── Pagination ───────────────────────────────
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
MIN_PAGE_SIZE = 1

# ── Security ─────────────────────────────────
BCRYPT_ROUNDS = 12
TOKEN_TYPE_ACCESS = "access"
TOKEN_TYPE_REFRESH = "refresh"

# ── File Upload ──────────────────────────────
MAX_FILE_SIZE_MB = 5
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp", "image/gif"}
ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

# ── Date Formats ─────────────────────────────
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

# ── Cache TTL (seconds) ─────────────────────
CACHE_TTL_SHORT = 60  # 1 minute
CACHE_TTL_MEDIUM = 300  # 5 minutes
CACHE_TTL_LONG = 3600  # 1 hour
CACHE_TTL_DAY = 86400  # 24 hours


# ── Order Status ─────────────────────────────
class OrderStatus:
    """Order status constants."""

    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"
    REFUNDED = "refunded"


# ── Payment Status ───────────────────────────
class PaymentStatus:
    """Payment status constants."""

    PENDING = "pending"
    AUTHORIZED = "authorized"
    CAPTURED = "captured"
    FAILED = "failed"
    REFUNDED = "refunded"
