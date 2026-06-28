/**
 * Love Ludhiana Fashion — 404 Not Found Page.
 */

import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

export function NotFound() {
  return (
    <div className="flex min-h-[80vh] flex-col items-center justify-center px-4 text-center">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h1 className="mb-4 text-8xl font-bold text-gray-700">404</h1>
        <p className="mb-8 text-xl text-gray-400">
          Oops! The page you&apos;re looking for doesn&apos;t exist.
        </p>
        <Link
          to="/"
          className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-pink-500 to-purple-600 px-8 py-3 font-medium text-white transition-all hover:shadow-lg hover:shadow-purple-500/25"
        >
          ← Back to Home
        </Link>
      </motion.div>
    </div>
  );
}
