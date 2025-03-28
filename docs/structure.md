# 🗂️ Monorepo Structure

This repository follows a modular monorepo layout.

    prototype-qextras/
    ├── test-qadence-libs/               # Reusable core libraries
    ├── test-qadence-protocols/          # Quantum protocol implementations
    ├── docs/                            # Root documentation site (you are here)
    ├── pyproject.toml                   # Project configuration (Hatch-based)
    └── .github/workflows/               # CI/CD pipelines (tests, docs, deploy)

Each module (e.g., `test-qadence-libs`, `test-qadence-protocols`) is independently versioned and published to PyPI.

## Directory Conventions

- Use `src/` layout inside each module if needed  
- Tests should live in `tests/` inside each module  
- Documentation should reside in the root `docs/` or module-specific docs  