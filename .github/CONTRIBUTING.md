# Contributing to Love Ludhiana Fashion

Thank you for contributing! Following these guidelines ensures a smooth development lifecycle.

## Development Workflow

1. **Branch Naming Conventions**:
   - `feat/feature-name` for new features
   - `fix/bug-desc` for bug fixes
   - `docs/doc-updates` for documentation changes
   - `chore/task-name` for setup or dependencies

2. **Commit Message Standards (Conventional Commits)**:
   We use conventional commit messages. Your commit messages must follow this structure:
   ```
   <type>(<scope>): <description>

   [optional body]
   ```
   Allowed types:
   - `feat`: A new feature
   - `fix`: A bug fix
   - `docs`: Documentation changes
   - `style`: Formatting, missing semi-colons, etc. (no code changes)
   - `refactor`: Refactoring production code (no bug fixes, no new features)
   - `perf`: Code changes that improve performance
   - `test`: Adding missing tests or correcting existing tests
   - `build`: Build system or external dependencies
   - `ci`: CI configuration files and scripts
   - `chore`: Other changes that don't modify src or test files

3. **Pre-commit Hooks**:
   Before committing, install and run pre-commit hooks to ensure code quality:
   ```bash
   pip install pre-commit
   pre-commit install
   pre-commit run --all-files
   ```

4. **Pull Request Process**:
   - Create a branch off `main` or the designated base branch.
   - Ensure linting, typing (`mypy` for backend, `tsc` for frontend), and tests pass.
   - Open a PR, fill in the PR template, and request reviews.
