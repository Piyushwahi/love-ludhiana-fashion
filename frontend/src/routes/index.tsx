/**
 * Love Ludhiana Fashion — Route Definitions.
 */

import { createBrowserRouter } from 'react-router-dom';

import { RootLayout } from '../layouts/RootLayout';
import { Home } from '../pages/Home';
import { NotFound } from '../pages/NotFound';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    children: [
      {
        index: true,
        element: <Home />,
      },
      // Feature routes will be added here:
      // { path: 'products', element: <Products /> },
      // { path: 'products/:slug', element: <ProductDetail /> },
      // { path: 'cart', element: <Cart /> },
      // { path: 'wishlist', element: <Wishlist /> },
      // { path: 'checkout', element: <Checkout /> },
      // { path: 'orders', element: <Orders /> },
      // { path: 'profile', element: <Profile /> },
      // { path: 'login', element: <Login /> },
      // { path: 'register', element: <Register /> },
      {
        path: '*',
        element: <NotFound />,
      },
    ],
  },
]);
