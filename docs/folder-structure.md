# Folder Structure Documentation

This document explains the organization and purpose of the enterprise-level folder structure used in **Love Ludhiana Fashion**.

---

## Complete Project Directory Layout

```
love-ludhiana-fashion/
├── .devcontainer/             # Visual Studio Code Dev Container configs
│   └── devcontainer.json      # Workspace container runtime definition
├── .github/                   # GitHub integration configuration
│   ├── ISSUE_TEMPLATE/        # Issue reporting templates (bug/feature)
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml             # Github Actions continuous integration workflow
├── .vscode/                   # VS Code configuration workspace
│   ├── extensions.json        # Recommended team extensions
│   ├── launch.json            # Debugger configurations (FastAPI/Pytest/Chrome)
│   └── settings.json          # Workspace-specific linting/formatter rules
├── backend/                   # Three-tier REST API Backend
│   ├── alembic.ini            # Database migration CLI configuration
│   ├── pyproject.toml         # Python packaging, metadata, and dependencies
│   ├── .env.example           # Shared backend configuration environment
│   ├── app/                   # FastAPI core source code
│   │   ├── main.py            # API Server main initialization & middlewares
│   │   ├── api/               # Router endpoints versioning controllers
│   │   ├── common/            # Enums, variables, schemas shared globally
│   │   ├── config/            # Base settings & third-party config stubs
│   │   ├── core/              # Dependency injection, events, security helpers
│   │   ├── database/          # Connection pools, declarative bases, mixins
│   │   ├── exceptions/        # Custom exception classes & global handlers
│   │   ├── logging/           # Rotating structured JSON logger configuration
│   │   ├── middleware/        # CORS, Logging, OWASP security header filters
│   │   ├── models/            # SQLAlchemy database entity models
│   │   ├── modules/           # Feature-based modular logic folders (stubs)
│   │   ├── repositories/      # Base generic and entity specific DB access
│   │   ├── schemas/           # Pydantic request/response validation schemas
│   │   ├── services/          # Business logic wrappers around repositories
│   │   └── utils/             # Validators, helpers, common utility logic
│   ├── migrations/            # Alembic migrations scripts version tree
│   └── tests/                 # Pytest suite with conftest fixtures
├── database/                  # Enterprise database scripts
│   ├── seeds/                 # Data population mock JSON files
│   └── README.md              # DB migration and seeding documentation
├── docker/                    # Docker infrastructure scripts
│   ├── backend/
│   │   └── Dockerfile         # Multi-stage image build for backend API
│   ├── frontend/
│   │   ├── Dockerfile         # Multi-stage build (Node build -> Nginx serve)
│   │   └── nginx.conf         # Production Nginx SPA configuration file
│   ├── docker-compose.yml     # Compose base services mapping
│   ├── docker-compose.dev.yml # Local hot-reloading dev configuration
│   ├── docker-compose.prod.yml# Tightened production compose configuration
│   └── prometheus.yml         # Metric scraper config mapping file
├── docs/                      # Global documentation library
│   ├── api-standards.md
│   ├── architecture.md
│   ├── coding-standards.md
│   ├── development-guide.md
│   └── folder-structure.md
├── frontend/                  # React Single Page Web Application
│   ├── package.json           # Node configuration and module imports
│   ├── vite.config.ts         # Vite configuration with Tailwind CSS v4 integration
│   ├── eslint.config.js       # ESLint Flat Config rules
│   ├── .prettierrc            # Formatting conventions config file
│   ├── .env.example           # Frontend settings templates
│   ├── src/                   # React source code folder
│   │   ├── main.tsx           # Entry React DOM renderer
│   │   ├── App.tsx            # Routes provider mount loader
│   │   ├── index.css          # Tailwind and global typography styles
│   │   ├── animations/        # Framer Motion animation transition presets
│   │   ├── components/        # UI primitives, shared templates, layout
│   │   ├── config/            # Env loaders, constant definitions, Axios configs
│   │   ├── layouts/           # Page structural grids (Root, Auth)
│   │   ├── pages/             # View routers endpoints
│   │   ├── providers/         # Global React Providers composer container
│   │   ├── redux/             # RTK store, hooks, global slices
│   │   ├── routes/            # React Router dynamic path mappings
│   │   ├── types/             # TypeScript interfaces and REST models
│   │   └── utils/             # Class merger, formatters, hooks helpers
│   └── public/                # Static public folder assets
├── scripts/                   # Automations setup scripts
│   ├── setup.sh               # Local bash bootstrapper (Linux/macOS)
│   └── setup.ps1              # Local PowerShell bootstrapper (Windows)
├── .editorconfig              # IDE cross-editor coding standards mapping
├── .gitignore                 # Version control file ignoring rules
├── LICENSE                    # MIT License certificate
├── README.md                  # Project overview document
└── CHANGELOG.md               # Standard version history logging
```
