# How to contribute

We're grateful for your interest in participating in qadence-measurement. Please follow our guidelines to ensure a smooth contribution process.

## Contribution Guide for Developers

- **Submitting Issues:** To submit bug reports or feature requests, please use our [issue tracker](https://github.com/pasqal-io/qadence-hub/issues).

### Reporting an issue or proposing a feature

Your course of action will depend on your objective, but generally, you should start by creating an issue. If you've discovered a bug or have a feature you'd like to see added to **qadence-measurement**, feel free to create an issue on [qadence-hubs's GitHub issue tracker](https://github.com/pasqal-io/qadence-hub/issues). Here are some steps to take:

1. Quickly search the existing issues using relevant keywords to ensure your issue hasn't been addressed already.
2. If your issue is not listed, create a new one. Try to be as detailed and clear as possible in your description.

- If you're merely suggesting an improvement or reporting a bug, that's already excellent! We thank you for it. Your issue will be listed and, hopefully, addressed at some point.

### Setup with downloading the whole git repository

To work with `qadence-measurement`, you should clone the entire GitHub repository and then access the individual projects. This approach is recommended for easier branch management, and cloning only a specific project is discouraged. After cloning the full repository, navigate to the desired project folder to run the Hatch environment or make code modifications. The example code snippet is like below:

```shell
git clone https://github.com/pasqal-io/qadence-hub.git
cd qadence-hub/qadence-measurement
```

### Making Pull Request

If you’ve modified the code of a `qadence-measurement` package, you should create a pull request targeting the `main-measurement` branch. Our branch structure manages each package through its corresponding `sub-main branch` before anything is merged into the `main branch`. Therefore, after cloning the repository, you should follow your previous workflow to create a local branch and push it—but your pull request target should be your `main-measurement` branch, not `main`. After your branch is merged to `main-measurement` branch, you can initiate merge request to the `main` branch. Merging into `main` branch should be done only when a release is being prepared.

### Releasing Projects and Publishing to PyPI

After you merge your `main-measurement` branch to `main` branch, you can publish your documents and Python package through release. To do this, you need to update the version number in the package's `pyproject.toml`. Then, you create a release with the format of `package_name-v.x.y.z,` where x, y, and z are for version numbers. For example, if you want to publish `qadence-measurement` with version 1.2.5, you must put `measurement-v1.2.5` as your release name.


## Setting up your development environment

We recommended to use `hatch` for managing environments.

To develop within qadence-hub packages, use:
```shell
cd qadence-measurement
pip install hatch
hatch -v shell
```

### Useful thing for your workflow: linting

Use `pre-commit` to lint your code and run the unit tests before pushing a new commit.

Using `hatch`, it's simply:

```shell
pre-commit install
hatch -e tests run pre-commit run --all-files
```

Our CI/CD pipeline will also test if the documentation can be built correctly. To test it locally, please run:

```shell
hatch -e docs run mkdocs build --clean --strict
```

Without `hatch`, `pip` install those libraries first:
"mkdocs",
"mkdocs-material",
"mkdocstrings",
"mkdocstrings-python",
"mkdocs-section-index",
"mkdocs-jupyter",
"mkdocs-exclude",
"markdown-exec"


And then:

```shell
 mkdocs build --clean --strict
```
