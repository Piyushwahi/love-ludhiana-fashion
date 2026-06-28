/**
 * Love Ludhiana Fashion — Root Layout.
 *
 * Base layout wrapping all pages with header/footer.
 */

import { Outlet } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';

export function RootLayout() {
  return (
    <>
      <Helmet>
        <title>Love Ludhiana Fashion — Kids Clothing Store</title>
        <meta
          name="description"
          content="Love Ludhiana Fashion — Premium kids clothing store for ages 0-20. Shop the latest trends in children's fashion."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </Helmet>

      <div id="app-root" className="flex min-h-screen flex-col">
        {/* Header will be added in future phases */}
        <header id="main-header" className="sticky top-0 z-50">
          {/* <Header /> */}
        </header>

        <main id="main-content" className="flex-1">
          <Outlet />
        </main>

        {/* Footer will be added in future phases */}
        <footer id="main-footer">
          {/* <Footer /> */}
        </footer>
      </div>
    </>
  );
}
