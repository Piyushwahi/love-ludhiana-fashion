/**
 * Framer Motion transition and variant presets for premium UX animations.
 */

export const transitionSlow = { duration: 0.6, ease: [0.16, 1, 0.3, 1] };
export const transitionMedium = { duration: 0.4, ease: 'easeInOut' };
export const transitionFast = { duration: 0.2, ease: 'easeOut' };

export const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: transitionMedium },
};

export const slideUp = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: transitionSlow },
};

export const slideInLeft = {
  hidden: { opacity: 0, x: -30 },
  visible: { opacity: 1, x: 0, transition: transitionSlow },
};

export const slideInRight = {
  hidden: { opacity: 0, x: 30 },
  visible: { opacity: 1, x: 0, transition: transitionSlow },
};

export const scaleUp = {
  hidden: { opacity: 0, scale: 0.95 },
  visible: { opacity: 1, scale: 1, transition: transitionSlow },
};

export const staggerContainer = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.05,
    },
  },
};
