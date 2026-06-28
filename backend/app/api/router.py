"""
Love Ludhiana Fashion — API Router.

Aggregates all versioned API routers.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.config.constants import API_V1_PREFIX

# ── v1 Router ────────────────────────────────
v1_router = APIRouter(prefix=API_V1_PREFIX)
v1_router.include_router(health_router)

# Feature module routers will be added here:
# v1_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
# v1_router.include_router(users_router, prefix="/users", tags=["Users"])
# v1_router.include_router(products_router, prefix="/products", tags=["Products"])
# v1_router.include_router(categories_router, prefix="/categories", tags=["Categories"])
# v1_router.include_router(orders_router, prefix="/orders", tags=["Orders"])
# v1_router.include_router(cart_router, prefix="/cart", tags=["Cart"])
# v1_router.include_router(wishlist_router, prefix="/wishlist", tags=["Wishlist"])
# v1_router.include_router(payments_router, prefix="/payments", tags=["Payments"])
# v1_router.include_router(reviews_router, prefix="/reviews", tags=["Reviews"])
# v1_router.include_router(shipping_router, prefix="/shipping", tags=["Shipping"])
# v1_router.include_router(coupons_router, prefix="/coupons", tags=["Coupons"])
# v1_router.include_router(banners_router, prefix="/banners", tags=["Banners"])
# v1_router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
# v1_router.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
# v1_router.include_router(
#     notifications_router, prefix="/notifications", tags=["Notifications"]
# )
# v1_router.include_router(faq_router, prefix="/faq", tags=["FAQ"])
# v1_router.include_router(contact_router, prefix="/contact", tags=["Contact"])
# v1_router.include_router(settings_router, prefix="/settings", tags=["Settings"])
# v1_router.include_router(admin_router, prefix="/admin", tags=["Admin"])
