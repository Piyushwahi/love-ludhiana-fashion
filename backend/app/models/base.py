"""
Love Ludhiana Fashion — Base Model.

Re-exports for convenient model imports.
All domain models should import Base and mixins from here.
"""

from app.database.base import Base
from app.database.mixins import SoftDeleteMixin, TimestampMixin, UUIDMixin

__all__ = ["Base", "SoftDeleteMixin", "TimestampMixin", "UUIDMixin"]
