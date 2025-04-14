# Qadence Hub Overview

Welcome to the documentation for the **Qadence Hub**.
This repository contains multiple modular Python packages developed for **Qadence** features

## Included Packages

- [**qadence-mitigations**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-mitigations): Quantum error mitigation techniques
- [**qadence-measurements**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-measurements): Quantum output measurement methods
- [**qadence-gradient**](https://github.com/pasqal-io/qadence-hub/tree/main/qadence-gradient): Foundational quantum gradient utilities library
- **qadence-models**(https://github.com/pasqal-io/qadence-hub/tree/main/qadence-models): Quantum constructors for various blocks and ansätze.

## Module Docs

- [qadence-mitigations documentation](https://pasqal-io.github.io/qadence-hub/qadence-mitigations/latest/)
- [qadence-measurements documentation](https://pasqal-io.github.io/qadence-hub/qadence-measurements/latest/)
- [qadence-gradient documentation](https://pasqal-io.github.io/qadence-hub/qadence-gradient/latest/)
- [qadence-models documentation](https://pasqal-io.github.io/qadence-hub/qadence-models/latest/)

## Development Resources

- [Setup Guide](setup.md)
- [Testing](test.md)


## Qadence-Hub Structure

This repository follows a modular monorepo layout.

    qadence-hub/
    ├── qadence-measurements/       # Interfaces for executing and analyzing quantum measurements
    ├── qadence-mitigations/        # Tools for error mitigation in quantum circuit execution
    ├── qadence-gradient/           # Quantum optimizers and information geometry utilities
    ├── qadence-models/             # Quantum ML models built on variational quantum circuits
    ├── docs/                       # Root documentation site
    ├── pyproject.toml              # Project configuration (Hatch-based)
    └── .github/workflows/          # CI/CD pipelines (tests, docs, lint)

Each module is independently versioned and will be published to PyPI.

## Directory Conventions

- Use `project_name/` layout inside each module for source codes
- Tests should live in `tests/` inside each module
- Documentation should reside in the root `docs/` or module-specific docs
