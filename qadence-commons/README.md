# Qadence-Commons

**Qadence-Commons** is a Python package that provides shared libraries for qadence. **Commons** documentations is [here](https://pasqal-io.github.io/qadence-hub/qadence-commons/latest/)

[![Linting](https://github.com/pasqal-io/qadence-hub/actions/workflows/lint.yml/badge.svg)](https://github.com/pasqal-io/qadence-hub/actions/workflows/lint.yml)
[![Tests](https://github.com/pasqal-io/qadence-hub/actions/workflows/test.yml/badge.svg)](https://github.com/pasqal-io/qadence-hub/actions/workflows/test.yml)
[![Documentation](https://github.com/pasqal-io/qadence-hub/actions/workflows/build_docs.yml/badge.svg)](https://pasqal-io.github.io/qadence-hub/latest)
[![Pypi](https://badge.fury.io/py/qadence-commons.svg)](https://pypi.org/project/qadence-commons/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## Installation guide

[qadence-commons](https://pypi.org/project/qadence-commons/) and can be installed using `pip` as follows:

```bash
pip install qadence-commons
```

## Contributing

Before making a contribution, please review our [code of conduct](docs/CODE_OF_CONDUCT.md).

- **Submitting Issues:** To submit bug reports or feature requests, please use our [issue tracker](https://github.com/pasqal-io/qadence-hub/issues).
- **Developing in qadence:** To learn more about how to develop within `qadence-commons`, please refer to [contributing guidelines](docs/CONTRIBUTING.md).

### Setting up qadence in development mode

We recommend to use the [`hatch`](https://hatch.pypa.io/latest/) environment manager to install `qadence-commons` from source:

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
Qadence-Commons is a free and open source software package, released under the Apache License, Version 2.0.
