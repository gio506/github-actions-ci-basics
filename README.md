# github-actions-ci-basics

A tiny Python project that demonstrates a clean **GitHub Actions CI pipeline** with clear stages and local parity.

## Pipeline stages

This repository uses `.github/workflows/ci.yml` with 4 sequential jobs:

1. **Format check** (`black --check .`)
2. **Lint** (`ruff check .`)
3. **Unit tests** (`pytest -q`)
4. **Build/package** (`python -m build`) and upload `dist/` as artifact

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

black --check .
ruff check .
pytest -q
python -m build
```

## Project tree

```text
.
├── .github/workflows/ci.yml      # GitHub Actions workflow with 4 CI stages
├── app.py                        # Tiny app with simple functions under test
├── test_app.py                   # Unit tests for app behavior
├── pyproject.toml                # Python project metadata + tool configuration
├── requirements-dev.txt          # Dev dependencies for local checks and CI
├── CHEATSHEET.md                 # Quick command reference for contributors
└── README.md                     # Project overview and CI explanation
```

## Why this example is useful

- Keeps application code intentionally tiny so CI concepts are the focus.
- Mirrors CI steps locally to reduce "works on my machine" issues.
- Shows artifact packaging as a final stage in a multi-step pipeline.
