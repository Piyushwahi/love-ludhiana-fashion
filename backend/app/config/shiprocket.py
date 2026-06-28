"""
Love Ludhiana Fashion — Shiprocket Configuration.

Prepared Shiprocket shipping integration.
Actual shipping logic will be implemented in later phases.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class ShiprocketConfig:
    """Shiprocket API configuration holder."""

    def __init__(
        self,
        email: str = "",
        password: str = "",
        api_url: str = "https://apiv2.shiprocket.in/v1/external",
    ) -> None:
        self.email = email
        self.password = password
        self.api_url = api_url
        self._token: str | None = None

    @property
    def is_configured(self) -> bool:
        """Check if Shiprocket credentials are set."""
        return bool(self.email and self.password)


_shiprocket_config: ShiprocketConfig | None = None


def init_shiprocket(email: str, password: str, api_url: str) -> None:
    """
    Initialize Shiprocket configuration.

    Args:
        email: Shiprocket account email.
        password: Shiprocket account password.
        api_url: Shiprocket API base URL.
    """
    global _shiprocket_config
    _shiprocket_config = ShiprocketConfig(
        email=email,
        password=password,
        api_url=api_url,
    )

    if not _shiprocket_config.is_configured:
        logger.warning(
            "Shiprocket credentials not configured. Shipping will be disabled."
        )
    else:
        logger.info("Shiprocket configuration initialized")


def get_shiprocket_config() -> ShiprocketConfig:
    """
    Get the Shiprocket configuration.

    Returns:
        ShiprocketConfig instance.

    Raises:
        RuntimeError: If Shiprocket has not been initialized.
    """
    if _shiprocket_config is None:
        msg = "Shiprocket is not initialized. Call init_shiprocket() first."
        raise RuntimeError(msg)
    return _shiprocket_config
