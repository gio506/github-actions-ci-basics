# github-actions-ci-basics

A tiny Python example project that demonstrates a practical **GitHub Actions CI pipeline** with clear quality gates and local reproducibility.

## CI pipeline overview

The workflow lives in `.github/workflows/ci.yml` and runs on pushes to `main` and on pull requests.

### Stage 1: Quality checks (format + lint)
- **Format check**: `black --check .`
- **Lint check**: `ruff check .`

Both checks are grouped in one job so code quality feedback appears together and early.

### Stage 2: Unit tests
- **Test runner**: `pytest -q`
- Runs only after quality checks pass.

### Stage 3: Build/package
- **Build command**: `python -m build`
- Uploads generated `dist/` files as a GitHub Actions artifact.

## Best-practice choices used

- **Least-privilege permissions** in workflow (`contents: read`).
- **Concurrency control** to cancel stale runs on the same branch/PR.
- **Pip cache** via `actions/setup-python` to speed up repeated runs.
- **Sequential job dependencies** (`needs`) for explicit CI gates.
- **Pinned tool versions** in `requirements-dev.txt` for reproducible checks.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt

black --check .
ruff check .
pytest -q
python -m build
```

## Project tree

```text
.
├── .github/workflows/ci.yml      # CI workflow: quality checks, tests, build, artifact upload
├── app.py                        # Tiny application module used by tests
├── test_app.py                   # Unit tests validating app behavior
├── pyproject.toml                # Packaging metadata + tool config for black/ruff/pytest
├── requirements-dev.txt          # Pinned dev dependencies for CI and local checks
├── CHEATSHEET.md                 # Command reference (Python, CI, Git, troubleshooting)
├── .gitignore                    # Ignore local env/build/cache artifacts
└── README.md                     # CI documentation, stages, and local run guide
```

## Why this repository exists

- Keep code intentionally small so CI design is easy to understand.
- Provide a clean baseline that teams can copy and extend.
- Demonstrate the same checks locally and in CI for predictable results.
