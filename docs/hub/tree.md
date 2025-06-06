This repository follows a modular monorepo layout.

    qadence-hub/
    ├── qadence-commons/           # Shared utility libraries for Qadence
    ├── qadence-mitigation/        # Tools for error mitigation in quantum circuit execution
    ├── qadence-measurement/       # Interfaces for executing and analyzing quantum measurement
    ├── qadence-model/             # Quantum ML models built on variational quantum circuits
    ├── docs/                       # Root documentation site
    ├── pyproject.toml              # Project configuration (Hatch-based)
    └── .github/workflows/          # CI/CD pipelines (tests, docs, lint)

Each module is independently versioned and will be published to PyPI.
