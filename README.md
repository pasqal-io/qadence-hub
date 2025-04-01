# Qadence-Hub


**Qadence-Hub** is a Github monorepo that hosts multiple Python packages developed under the **Qadence** initiative. It is structured to support independent development, testing, and deployment of each quantum features while maintaining a unified development environment.


<!-- [![Linting](https://github.com/pasqal-io/qadence-protocols/actions/workflows/lint.yml/badge.svg)](https://github.com/pasqal-io/qadence-protocols/actions/workflows/lint.yml)
[![Tests](https://github.com/pasqal-io/qadence-protocols/actions/workflows/test_fast.yml/badge.svg)](https://github.com/pasqal-io/qadence-protocols/actions/workflows/test.yml)
[![Documentation](https://github.com/pasqal-io/qadence-protocols/actions/workflows/build_docs.yml/badge.svg)](https://pasqal-io.github.io/qadence-protocols/latest)
[![Pypi](https://badge.fury.io/py/qadence-protocols.svg)](https://pypi.org/project/qadence-protocols/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) -->








This repository is a monorepo containing multiple Python packages for Qadence development, managed using [Hatch](https://hatch.pypa.io/).

## 📦 Projects

| Name | Description |
|------|-------------|
| `test-qadence-protocols` | Protocol definitions and APIs |
| `test-qadence-libs` | Common utility libraries |

## 📐 Project Structure

```
.
├── test-qadence-protocols/
│   ├── docs/
│   ├── tests/
│   ├── pyproject.toml
│   └── mkdocs.yml
├── test-qadence-libs/
│   ├── docs/
│   ├── tests/
│   ├── pyproject.toml
│   └── mkdocs.yml
├── .github/
│   └── workflows/
├── mkdocs.yml           # root-level docs config
├── pyproject.toml       # docs root config
└── README.md
```

## Contributing

Before making a contribution, please review our [code of conduct](docs/CODE_OF_CONDUCT.md).

- **Submitting Issues:** To submit bug reports or feature requests, please use our [issue tracker](https://github.com/pasqal-io/qadence-hub/issues).
- **Developing in qadence:** To learn more about how to develop within `qadence-hub`, please refer to [contributing guidelines](docs/CONTRIBUTING.md).

### Setting up qadence in development mode

We recommend to use the [`hatch`](https://hatch.pypa.io/latest/) environment manager to install `qadence_protocols` from source:

```bash
python -m pip install hatch

# get into a shell with all the dependencies
python -m hatch shell

# run a command within the virtual environment with all the dependencies
python -m hatch run python my_script.py
```

**WARNING**
`hatch` will not combine nicely with other environment managers such as Conda. If you still want to use Conda,
install it from source using `pip`:

```bash
# within the Conda environment
python -m pip install -e .
```

## License
Qadence-Protocols is a free and open source software package, released under the Apache License, Version 2.0.
