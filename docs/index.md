# Qadence Hub Overview

Welcome to the documentation for the **Qadence Hub**.
This repository contains multiple modular Python packages developed for **Qadence** features

## Included Packages

- [**qadence-protocols**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-protocols): Quantum mitigation and measurement workflows
- [**qadence-libs**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-libs): Foundational quantum utilities library
- **qadence-models**: Quantum constructors for various blocks and ansätze.

## Module Docs

- [qadence-protocols documentation](https://pasqal-io.github.io/qadence-hub/qadence-protocols/latest/)
- [qadence-libs documentation](https://pasqal-io.github.io/qadence-hub/qadence-libs/latest/)
- [qadence-models documentation]

## Development Resources

- [Setup Guide](setup.md)
- [Testing](test.md)


## Qadence-Hub Structure

This repository follows a modular monorepo layout.

    qadence-hub/
    ├── qadence-protocols/          # Qadence-protocols implementations
    ├── qadence-libs/               # Qadence-lib libraries
    ├── docs/                            # Root documentation site
    ├── pyproject.toml                   # Project configuration (Hatch-based)
    └── .github/workflows/               # CI/CD pipelines (tests, docs, lint)

Each module (e.g., `qadence-libs`, `qadence-protocols`) is independently versioned and will be published to PyPI.

## Directory Conventions

- Use `project_name/` layout inside each module for source codes
- Tests should live in `tests/` inside each module
- Documentation should reside in the root `docs/` or module-specific docs
