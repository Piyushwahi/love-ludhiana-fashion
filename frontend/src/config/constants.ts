/**
 * Love Ludhiana Fashion — Application Constants.
 */

export const APP_NAME = 'Love Ludhiana Fashion';
export const APP_TAGLINE = 'Stylish Kids Clothing (0-20 Years)';

export const PAGINATION = {
  DEFAULT_PAGE_SIZE: 20,
  MAX_PAGE_SIZE: 100,
} as const;

export const BREAKPOINTS = {
  SM: 640,
  MD: 768,
  LG: 1024,
  XL: 1280,
  '2XL': 1536,
} as const;

export const ROUTES = {
  HOME: '/',
  LOGIN: '/login',
  REGISTER: '/register',
  PRODUCTS: '/products',
  PRODUCT_DETAIL: '/products/:slug',
  CART: '/cart',
  WISHLIST: '/wishlist',
  CHECKOUT: '/checkout',
  ORDERS: '/orders',
  PROFILE: '/profile',
  ADMIN: '/admin',
  NOT_FOUND: '*',
} as const;

export const QUERY_KEYS = {
  PRODUCTS: 'products',
  CATEGORIES: 'categories',
  BRANDS: 'brands',
  CART: 'cart',
  WISHLIST: 'wishlist',
  ORDERS: 'orders',
  USER: 'user',
  REVIEWS: 'reviews',
  BANNERS: 'banners',
} as const;
