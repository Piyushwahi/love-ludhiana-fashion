# ==============================================================================
# Love Ludhiana Fashion — Local Development Environment Setup Script (PowerShell)
# ==============================================================================

$ErrorActionPreference = "Stop"

Write-Host "🚀 Initializing Love Ludhiana Fashion Development Environment..." -ForegroundColor Green

# ── Check Dependencies ────────────────────────────────────────────────────────

# Python Check
try {
    $pythonVer = python --version 2>&1
    Write-Host "Found Python: $pythonVer" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed. Please install Python 3.12+ and add to PATH." -ForegroundColor Red
    exit 1
}

# Node Check
try {
    $nodeVer = node --version 2>&1
    Write-Host "Found Node.js: $nodeVer" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js is not installed. Please install Node.js 20+ and add to PATH." -ForegroundColor Red
    exit 1
}

# ── Environment Configurations ────────────────────────────────────────────────

Write-Host "`n⚙️ Copying Environment Configurations..." -ForegroundColor Yellow
if (-not (Test-Path "backend/.env")) {
    Copy-Item "backend/.env.example" "backend/.env"
    Write-Host "✓ Created backend/.env" -ForegroundColor Green
} else {
    Write-Host "backend/.env already exists."
}

if (-not (Test-Path "frontend/.env")) {
    Copy-Item "frontend/.env.example" "frontend/.env"
    Write-Host "✓ Created frontend/.env" -ForegroundColor Green
} else {
    Write-Host "frontend/.env already exists."
}

# ── Backend Setup ─────────────────────────────────────────────────────────────

Write-Host "`n🐍 Setting up Python Virtual Environment in backend..." -ForegroundColor Yellow
Set-Location "backend"
python -m venv .venv
& ".\.venv\Scripts\pip" install --upgrade pip setuptools wheel
& ".\.venv\Scripts\pip" install -e ".[dev]"
Set-Location ".."
Write-Host "✓ Backend packages installed successfully." -ForegroundColor Green

# ── Frontend Setup ────────────────────────────────────────────────────────────

Write-Host "`n📦 Installing Frontend NPM Dependencies..." -ForegroundColor Yellow
Set-Location "frontend"
npm install
Set-Location ".."
Write-Host "✓ Frontend packages installed successfully." -ForegroundColor Green

# ── Pre-commit Setup ──────────────────────────────────────────────────────────

Write-Host "`n⚓ Installing Git Pre-commit Hooks..." -ForegroundColor Yellow
if (Test-Path ".git") {
    & ".\backend\.venv\Scripts\pre-commit" install
    Write-Host "✓ Pre-commit hooks installed." -ForegroundColor Green
} else {
    Write-Host "⚠️ Git directory not found. Run 'git init' first to configure pre-commit hooks." -ForegroundColor Yellow
}

Write-Host "`n🎉 Setup Complete! To start the development environment:" -ForegroundColor Green
Write-Host "1. Activate backend environment: " -NoNewline
Write-Host ".\backend\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "2. Run locally or with Docker:"
Write-Host "   - Local Dev Backend: " -NoNewline
Write-Host "cd backend; uvicorn app.main:app --reload" -ForegroundColor Yellow
Write-Host "   - Local Dev Frontend: " -NoNewline
Write-Host "cd frontend; npm run dev" -ForegroundColor Yellow
Write-Host "   - Docker Compose: " -NoNewline
Write-Host "docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build" -ForegroundColor Yellow
