/**
 * Love Ludhiana Fashion — Environment Configuration.
 *
 * Type-safe access to Vite environment variables.
 */

interface AppEnv {
  API_URL: string;
  API_VERSION: string;
  APP_NAME: string;
  APP_DESCRIPTION: string;
  APP_VERSION: string;
  GOOGLE_CLIENT_ID: string;
  RAZORPAY_KEY_ID: string;
  SENTRY_DSN: string;
  ENABLE_ANALYTICS: boolean;
  ENABLE_CHAT: boolean;
}

export const env: AppEnv = {
  API_URL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  API_VERSION: import.meta.env.VITE_API_VERSION || 'v1',
  APP_NAME: import.meta.env.VITE_APP_NAME || 'Love Ludhiana Fashion',
  APP_DESCRIPTION:
    import.meta.env.VITE_APP_DESCRIPTION ||
    'Kids Clothing Store (0-20 Years)',
  APP_VERSION: import.meta.env.VITE_APP_VERSION || '0.1.0',
  GOOGLE_CLIENT_ID: import.meta.env.VITE_GOOGLE_CLIENT_ID || '',
  RAZORPAY_KEY_ID: import.meta.env.VITE_RAZORPAY_KEY_ID || '',
  SENTRY_DSN: import.meta.env.VITE_SENTRY_DSN || '',
  ENABLE_ANALYTICS: import.meta.env.VITE_ENABLE_ANALYTICS === 'true',
  ENABLE_CHAT: import.meta.env.VITE_ENABLE_CHAT === 'true',
};

export const API_BASE_URL = `${env.API_URL}/api/${env.API_VERSION}`;
