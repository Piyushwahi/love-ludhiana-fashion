"""
Love Ludhiana Fashion — Security Architecture.

JWT and OAuth architecture stubs.
Actual authentication will be implemented in Part 2.
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any, cast

from jose import jwt  # type: ignore[import-untyped]

# Architecture stubs — implementation in Part 2


def create_access_token(
    data: dict[str, Any],
    secret: str,
    algorithm: str = "HS256",
    expires_delta: timedelta | None = None,
) -> str:
    """
    Create a JWT access token.

    Stub — will be fully implemented in Part 2.

    Args:
        data: Claims to encode in the token.
        secret: Secret key for signing.
        algorithm: JWT algorithm.
        expires_delta: Token expiration time.

    Returns:
        Encoded JWT string.
    """
    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire, "type": "access"})
    return cast(str, jwt.encode(to_encode, secret, algorithm=algorithm))


def create_refresh_token(
    data: dict[str, Any],
    secret: str,
    algorithm: str = "HS256",
    expires_delta: timedelta | None = None,
) -> str:
    """
    Create a JWT refresh token.

    Stub — will be fully implemented in Part 2.
    """
    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(days=7))
    to_encode.update({"exp": expire, "type": "refresh"})
    return cast(str, jwt.encode(to_encode, secret, algorithm=algorithm))


def verify_token(token: str, secret: str, algorithm: str = "HS256") -> dict[str, Any]:
    """
    Verify and decode a JWT token.

    Stub — will be fully implemented in Part 2.

    Raises:
        JWTError: If the token is invalid or expired.
    """
    return cast(dict[str, Any], jwt.decode(token, secret, algorithms=[algorithm]))


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    from passlib.context import CryptContext

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return cast(str, pwd_context.hash(password))


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    from passlib.context import CryptContext

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return cast(bool, pwd_context.verify(plain_password, hashed_password))
