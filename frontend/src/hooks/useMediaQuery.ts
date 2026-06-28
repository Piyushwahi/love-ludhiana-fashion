import { useSyncExternalStore } from 'react';

/**
 * Custom hook to detect screen matches for responsive layouts.
 *
 * Example:
 *   const isMobile = useMediaQuery('(max-width: 768px)');
 */
export function useMediaQuery(query: string): boolean {
  return useSyncExternalStore(
    (callback) => {
      const media = window.matchMedia(query);
      media.addEventListener('change', callback);
      return () => media.removeEventListener('change', callback);
    },
    () => window.matchMedia(query).matches,
    () => false // Server-side rendering fallback
  );
}
