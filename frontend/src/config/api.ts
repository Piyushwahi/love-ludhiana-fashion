/**
 * Love Ludhiana Fashion — Axios API Client.
 *
 * Pre-configured Axios instance with interceptors for
 * authentication, error handling, and request/response logging.
 */

import axios, {
  type AxiosError,
  type AxiosResponse,
  type InternalAxiosRequestConfig,
} from 'axios';
import toast from 'react-hot-toast';

import { API_BASE_URL } from './env';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
  withCredentials: true,
});

// ── Request Interceptor ─────────────────────
apiClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // Attach JWT token if available
    const token = localStorage.getItem('access_token');
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error: AxiosError) => Promise.reject(error),
);

// ── Response Interceptor ────────────────────
apiClient.interceptors.response.use(
  (response: AxiosResponse) => response,
  async (error: AxiosError<{ error?: { message?: string } }>) => {
    const status = error.response?.status;
    const message =
      error.response?.data?.error?.message || 'An unexpected error occurred';

    switch (status) {
      case 401:
        // Token expired — attempt refresh (Part 2)
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        // window.location.href = '/login';
        break;
      case 403:
        toast.error('You do not have permission to perform this action');
        break;
      case 404:
        // Let the calling code handle 404s
        break;
      case 429:
        toast.error('Too many requests. Please try again later.');
        break;
      case 500:
        toast.error('Server error. Please try again later.');
        break;
      default:
        if (!error.response) {
          toast.error('Network error. Please check your connection.');
        } else {
          toast.error(message);
        }
    }

    return Promise.reject(error);
  },
);

export default apiClient;
