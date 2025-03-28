# 🤝 Contributing Guide

We welcome contributions! Please follow the steps below to ensure consistency.

## 🧼 Code Style

We use the following tools for formatting and linting:

- `black`
- `ruff`
- `mypy`

Run all checks with:

    hatch run lint

## 🧪 Tests

- Write unit tests using `pytest`
- Place them in the `tests/` directory of the appropriate module

## 📄 Documentation

- Write or update relevant `*.md` files in `docs/`
- Confirm the site builds properly with:

    mkdocs build

## ✅ Pull Request Checklist

- [ ] All tests pass
- [ ] Linting passes
- [ ] Docs updated if needed
