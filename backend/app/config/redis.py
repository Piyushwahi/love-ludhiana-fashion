"""
Love Ludhiana Fashion — Redis Configuration.

Prepared Redis client for future caching and session management.
Do NOT implement caching logic here — only connection setup.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from redis.asyncio import ConnectionPool, Redis

logger = logging.getLogger(__name__)

_redis_client: Redis[Any] | None = None


async def get_redis_client() -> Redis[Any]:
    """
    Get the Redis client instance.

    Returns:
        Redis async client instance.

    Raises:
        RuntimeError: If Redis has not been initialized.
    """
    if _redis_client is None:
        msg = "Redis client is not initialized. Call init_redis() first."
        raise RuntimeError(msg)
    return _redis_client


async def init_redis(redis_url: str, max_connections: int = 20) -> None:
    """
    Initialize the Redis connection pool.

    Args:
        redis_url: Redis connection URL.
        max_connections: Maximum number of connections in the pool.
    """
    global _redis_client
    from redis.asyncio import ConnectionPool, Redis

    pool: ConnectionPool[Any] = ConnectionPool.from_url(
        redis_url,
        max_connections=max_connections,
        decode_responses=True,
    )
    _redis_client = Redis(connection_pool=pool)
    logger.info("Redis client initialized successfully")


async def close_redis() -> None:
    """Close the Redis connection pool gracefully."""
    global _redis_client
    if _redis_client is not None:
        await _redis_client.close()
        _redis_client = None
        logger.info("Redis connection closed")


async def check_redis_health() -> bool:
    """
    Check Redis connection health.

    Returns:
        True if Redis is reachable, False otherwise.
    """
    try:
        client = await get_redis_client()
        return await client.ping()
    except Exception:
        logger.exception("Redis health check failed")
        return False
