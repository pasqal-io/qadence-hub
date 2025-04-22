# Qadence Hub Overview

Welcome to the documentation for the **Qadence Hub**.
This repository contains multiple modular Python packages developed for **Qadence** features

## Included Packages

- [**qadence-mitigation**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-mitigation): Quantum error mitigation techniques
- [**qadence-measurement**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-measurement): Quantum output measurement methods
- [**qadence-gradient**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-gradient): Foundational quantum gradient utilities library
- [**qadence-model**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-model): Quantum constructors for various blocks and ansätze.

## Module Docs

- [qadence-mitigation documentation](https://pasqal-io.github.io/qadence-hub/qadence-mitigation/latest/)
- [qadence-measurement documentation](https://pasqal-io.github.io/qadence-hub/qadence-measurement/latest/)
- [qadence-gradient documentation](https://pasqal-io.github.io/qadence-hub/qadence-gradient/latest/)
- [qadence-model documentation](https://pasqal-io.github.io/qadence-hub/qadence-model/latest/)

## Development Resources

- [Setup Guide](setup.md)
- [Testing](test.md)


## Qadence-Hub Structure

This repository follows a modular monorepo layout.

    qadence-hub/
    ├── qadence-measurement/       # Interfaces for executing and analyzing quantum measurement
    ├── qadence-mitigation/        # Tools for error mitigation in quantum circuit execution
    ├── qadence-gradient/           # Quantum optimizers and information geometry utilities
    ├── qadence-model/             # Quantum ML models built on variational quantum circuits
    ├── qadence-commons/            # Qadence hub common library for subprojects
    ├── docs/                       # Root documentation site
    ├── pyproject.toml              # Project configuration (Hatch-based)
    └── .github/workflows/          # CI/CD pipelines (tests, docs, lint)

Each module is independently versioned and will be published to PyPI.

## Directory Conventions

- Use `project_name/` layout inside each module for source codes
- Tests should live in `tests/` inside each module
- Documentation should reside in the root `docs/` or module-specific docs
