# Qadence-Mitigations

**Qadence-Mitigations** is a Python package that provides error mitigation features for Qadence.

[![Linting](https://github.com/pasqal-io/qadence-hub/actions/workflows/lint.yml/badge.svg)](https://github.com/pasqal-io/qadence-hub/actions/workflows/lint.yml)
[![Tests](https://github.com/pasqal-io/qadence-hub/actions/workflows/test_fast.yml/badge.svg)](https://github.com/pasqal-io/qadence-hub/actions/workflows/test.yml)
[![Documentation](https://github.com/pasqal-io/qadence-hub/actions/workflows/build_docs.yml/badge.svg)](https://pasqal-io.github.io/qadence-hub/latest)
<!-- [![Pypi](https://badge.fury.io/py/qadence-hub.svg)](https://pypi.org/project/qadence-hub/) -->
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


<!-- ## Installation guide

[qadence-mitigations](https://pypi.org/project/qadence-mitigations/) and can be installed using `pip` as follows:

```bash
pip install qadence-mitigations
``` -->

## Contributing

Before making a contribution, please review our [code of conduct](docs/CODE_OF_CONDUCT.md).

- **Submitting Issues:** To submit bug reports or feature requests, please use our [issue tracker](https://github.com/pasqal-io/qadence-hub/issues).
- **Developing in qadence:** To learn more about how to develop within `qadence-measurements`, please refer to [contributing guidelines](docs/CONTRIBUTING.md).

### Setting up qadence in development mode

We recommend to use the [`hatch`](https://hatch.pypa.io/latest/) environment manager to install `qadence_mitigations` from source:

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

## Citation

If you use Qadence-Mitigations for a publication, we kindly ask you to cite our work using the following BibTex entry:

<!-- ```latex
@misc{qadence-protocols2024pasqal,
  url = {https://github.com/pasqal-io/qadence-protocols},
  title = {Qadence Protocols: {A}n {E}xperiment runner for Qadence.},
  year = {2023}
}
``` -->

## License
Qadence-Mitigations is a free and open source software package, released under the Apache License, Version 2.0.
