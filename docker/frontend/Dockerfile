# ============================================
# Love Ludhiana Fashion — Frontend Dockerfile
# Multi-stage build for development and production
# ============================================

# ── Stage 1: Base ────────────────────────────
FROM node:20-alpine AS base

WORKDIR /app

# ── Stage 2: Dependencies ────────────────────
FROM base AS dependencies

COPY package.json package-lock.json* ./
RUN npm ci

# ── Stage 3: Development ────────────────────
FROM dependencies AS development

COPY . .

EXPOSE 5173

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:5173 || exit 1

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# ── Stage 4: Build ──────────────────────────
FROM dependencies AS build

COPY . .
RUN npm run build

# ── Stage 5: Production (nginx) ─────────────
FROM nginx:alpine AS production

# Copy custom nginx config
COPY docker/frontend/nginx.conf /etc/nginx/nginx.conf

# Copy built assets
COPY --from=build /app/dist /usr/share/nginx/html

# Create non-root user
RUN addgroup -S appuser && adduser -S appuser -G appuser && \
    chown -R appuser:appuser /usr/share/nginx/html && \
    chown -R appuser:appuser /var/cache/nginx && \
    chown -R appuser:appuser /var/log/nginx && \
    touch /var/run/nginx.pid && \
    chown -R appuser:appuser /var/run/nginx.pid

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:80 || exit 1

CMD ["nginx", "-g", "daemon off;"]
