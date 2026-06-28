"""
Love Ludhiana Fashion — Validators.

Reusable validation functions for common data types.
"""

from __future__ import annotations

import re
from pathlib import PurePosixPath

from app.config.constants import ALLOWED_IMAGE_EXTENSIONS, MAX_FILE_SIZE_MB


def validate_phone_number(phone: str) -> bool:
    """Validate an Indian phone number (10 digits, optionally with +91)."""
    pattern = r"^(\+91)?[6-9]\d{9}$"
    return bool(re.match(pattern, phone.replace(" ", "").replace("-", "")))


def validate_pincode(pincode: str) -> bool:
    """Validate an Indian postal code (6 digits)."""
    return bool(re.match(r"^\d{6}$", pincode))


def validate_image_extension(filename: str) -> bool:
    """Check if a filename has an allowed image extension."""
    ext = PurePosixPath(filename).suffix.lower()
    return ext in ALLOWED_IMAGE_EXTENSIONS


def validate_file_size(size_bytes: int) -> bool:
    """Check if file size is within the allowed limit."""
    max_bytes = MAX_FILE_SIZE_MB * 1024 * 1024
    return size_bytes <= max_bytes


def validate_gst_number(gst: str) -> bool:
    """Validate an Indian GST number."""
    pattern = r"^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d{1}[Z]{1}[A-Z\d]{1}$"
    return bool(re.match(pattern, gst.upper()))
