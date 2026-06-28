"""
Love Ludhiana Fashion — Cloudinary Configuration.

Prepared Cloudinary integration for image storage.
Actual upload/management logic will be implemented in later phases.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def init_cloudinary(
    cloud_name: str,
    api_key: str,
    api_secret: str,
) -> None:
    """
    Initialize Cloudinary SDK configuration.

    Args:
        cloud_name: Cloudinary cloud name.
        api_key: Cloudinary API key.
        api_secret: Cloudinary API secret.
    """
    if not all([cloud_name, api_key, api_secret]):
        logger.warning(
            "Cloudinary credentials not configured. Image uploads will be disabled."
        )
        return

    import cloudinary

    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret,
        secure=True,
    )
    logger.info("Cloudinary initialized for cloud: %s", cloud_name)
