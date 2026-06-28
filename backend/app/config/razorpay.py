"""
Love Ludhiana Fashion — Razorpay Configuration.

Prepared Razorpay payment gateway integration.
Actual payment logic will be implemented in later phases.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

_razorpay_client = None


def init_razorpay(key_id: str, key_secret: str) -> None:
    """
    Initialize Razorpay client.

    Args:
        key_id: Razorpay API key ID.
        key_secret: Razorpay API key secret.
    """
    global _razorpay_client

    if not all([key_id, key_secret]):
        logger.warning(
            "Razorpay credentials not configured. Payment processing will be disabled."
        )
        return

    logger.info("Razorpay client configuration prepared (key_id: %s...)", key_id[:8])


from typing import Any


def get_razorpay_client() -> Any:
    """
    Get the Razorpay client instance.

    Returns:
        Razorpay client instance.

    Raises:
        RuntimeError: If Razorpay has not been initialized.
    """
    if _razorpay_client is None:
        msg = "Razorpay client is not initialized. Call init_razorpay() first."
        raise RuntimeError(msg)
    return _razorpay_client
