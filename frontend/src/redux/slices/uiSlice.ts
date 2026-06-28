/**
 * Love Ludhiana Fashion — UI Slice.
 *
 * Global UI state (sidebar, theme, loading).
 */

import { createSlice, type PayloadAction } from '@reduxjs/toolkit';

interface UIState {
  sidebarOpen: boolean;
  theme: 'light' | 'dark' | 'system';
  globalLoading: boolean;
  mobileMenuOpen: boolean;
}

const initialState: UIState = {
  sidebarOpen: false,
  theme: 'system',
  globalLoading: false,
  mobileMenuOpen: false,
};

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    toggleSidebar(state) {
      state.sidebarOpen = !state.sidebarOpen;
    },
    setSidebarOpen(state, action: PayloadAction<boolean>) {
      state.sidebarOpen = action.payload;
    },
    setTheme(state, action: PayloadAction<UIState['theme']>) {
      state.theme = action.payload;
    },
    setGlobalLoading(state, action: PayloadAction<boolean>) {
      state.globalLoading = action.payload;
    },
    toggleMobileMenu(state) {
      state.mobileMenuOpen = !state.mobileMenuOpen;
    },
  },
});

export const {
  toggleSidebar,
  setSidebarOpen,
  setTheme,
  setGlobalLoading,
  toggleMobileMenu,
} = uiSlice.actions;

export default uiSlice.reducer;
