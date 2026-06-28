"""
Love Ludhiana Fashion — Utility Helpers.

Common helper functions used across the application.
"""

from __future__ import annotations

import re
from typing import Any

from slugify import slugify as _slugify


def generate_slug(text: str) -> str:
    """Generate a URL-safe slug from text."""
    return _slugify(text, max_length=200)


def sanitize_string(value: str) -> str:
    """Remove potentially dangerous characters from a string."""
    return re.sub(r"[<>&\"';]", "", value).strip()


def mask_email(email: str) -> str:
    """Mask an email for display (e.g., u***@gmail.com)."""
    if "@" not in email:
        return email
    local, domain = email.split("@", 1)
    masked_local = local[0] + "***" if len(local) > 1 else "***"
    return f"{masked_local}@{domain}"


def format_price(amount: float | int, currency: str = "INR") -> str:
    """Format a price with currency symbol."""
    symbols = {"INR": "₹", "USD": "$", "EUR": "€", "GBP": "£"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
