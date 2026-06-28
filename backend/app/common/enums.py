"""
Love Ludhiana Fashion — Common Enums.

Application-wide enumerations.
"""

from __future__ import annotations

from enum import StrEnum


class Environment(StrEnum):
    """Application environment."""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class UserRole(StrEnum):
    """User roles for authorization."""

    CUSTOMER = "customer"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"
    STAFF = "staff"


class Gender(StrEnum):
    """Gender options for kids clothing."""

    BOY = "boy"
    GIRL = "girl"
    UNISEX = "unisex"


class AgeGroup(StrEnum):
    """Age group categories."""

    NEWBORN = "0-1"
    TODDLER = "1-3"
    KIDS = "3-8"
    TWEENS = "8-12"
    TEENS = "12-16"
    YOUNG_ADULT = "16-20"
