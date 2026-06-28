/**
 * Love Ludhiana Fashion — Home Page (Scaffold).
 *
 * Minimal placeholder confirming the application is running.
 * Full implementation in later phases.
 */

import { motion } from 'framer-motion';

export function Home() {
  return (
    <div className="flex min-h-[80vh] flex-col items-center justify-center px-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: 'easeOut' }}
        className="text-center"
      >
        <motion.h1
          className="mb-4 bg-gradient-to-r from-pink-500 via-purple-500 to-indigo-500 bg-clip-text font-display text-5xl font-bold text-transparent md:text-7xl"
          initial={{ scale: 0.9 }}
          animate={{ scale: 1 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          Love Ludhiana Fashion
        </motion.h1>

        <motion.p
          className="mb-8 text-lg text-gray-400 md:text-xl"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4 }}
        >
          Premium Kids Clothing Store — Ages 0 to 20
        </motion.p>

        <motion.div
          className="inline-flex items-center gap-2 rounded-full border border-emerald-500/30 bg-emerald-500/10 px-6 py-3 text-sm text-emerald-400"
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.6 }}
        >
          <span className="inline-block h-2 w-2 animate-pulse rounded-full bg-emerald-400" />
          Application Foundation Ready
        </motion.div>
      </motion.div>
    </div>
  );
}
