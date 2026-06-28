/**
 * Love Ludhiana Fashion — Redux Store.
 */

import { configureStore } from '@reduxjs/toolkit';

import uiReducer from './slices/uiSlice';

export const store = configureStore({
  reducer: {
    ui: uiReducer,
    // Feature slices will be added here:
    // auth: authReducer,
    // cart: cartReducer,
    // wishlist: wishlistReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        // Ignore non-serializable values in specific actions if needed
        ignoredActions: [],
      },
    }),
  devTools: import.meta.env.DEV,
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
