#!/bin/bash

# ==============================================================================
# Love Ludhiana Fashion — Local Development Environment Setup Script
# ==============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0;NC' # No Color

echo -e "${GREEN}🚀 Initializing Love Ludhiana Fashion Development Environment...${NC}\n"

# ── Check Dependencies ────────────────────────────────────────────────────────

# Python Check
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ python3 is not installed. Please install Python 3.12+.${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "Found Python version: ${GREEN}${PYTHON_VERSION}${NC}"

# Node Check
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js is not installed. Please install Node.js 20+.${NC}"
    exit 1
fi
NODE_VERSION=$(node -v)
echo -e "Found Node.js version: ${GREEN}${NODE_VERSION}${NC}"

# Docker Check
if ! command -v docker &> /dev/null; then
    echo -e "${YELLOW}⚠️ Docker is not installed or not in PATH. Docker workflows won't run.${NC}"
fi

# ── Environment Configurations ────────────────────────────────────────────────

echo -e "\n${YELLOW}⚙️ Copying Environment Configurations...${NC}"
if [ ! -f "backend/.env" ]; then
    cp backend/.env.example backend/.env
    echo -e "${GREEN}✓ Created backend/.env${NC}"
else
    echo -e "backend/.env already exists."
fi

if [ ! -f "frontend/.env" ]; then
    cp frontend/.env.example frontend/.env
    echo -e "${GREEN}✓ Created frontend/.env${NC}"
else
    echo -e "frontend/.env already exists."
fi

# ── Backend Setup ─────────────────────────────────────────────────────────────

echo -e "\n${YELLOW}🐍 Setting up Python Virtual Environment in backend...${NC}"
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -e ".[dev]"
cd ..
echo -e "${GREEN}✓ Backend packages installed successfully.${NC}"

# ── Frontend Setup ────────────────────────────────────────────────────────────

echo -e "\n${YELLOW}📦 Installing Frontend NPM Dependencies...${NC}"
cd frontend
npm install
cd ..
echo -e "${GREEN}✓ Frontend packages installed successfully.${NC}"

# ── Pre-commit Setup ──────────────────────────────────────────────────────────

echo -e "\n${YELLOW}⚓ Installing Git Pre-commit Hooks...${NC}"
if command -v git &> /dev/null && [ -d ".git" ]; then
    backend/.venv/bin/pre-commit install
    echo -e "${GREEN}✓ Pre-commit hooks installed.${NC}"
else
    echo -e "${YELLOW}⚠️ Git directory not found. Initialize git first to configure pre-commit hooks.${NC}"
fi

echo -e "\n${GREEN}🎉 Setup Complete! To start the development environment:${NC}"
echo -e "1. Activate backend environment: ${YELLOW}source backend/.venv/bin/activate${NC}"
echo -e "2. Run locally or with Docker:"
echo -e "   - Local Dev: ${YELLOW}cd backend && uvicorn app.main:app --reload${NC} AND ${YELLOW}cd frontend && npm run dev${NC}"
echo -e "   - Docker Compose: ${YELLOW}docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build${NC}"
