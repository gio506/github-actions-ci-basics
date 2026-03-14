# github-actions-ci-basics

A tiny Python example project that demonstrates a practical **GitHub Actions CI pipeline** with clear quality gates, PR checks, and local reproducibility.

## CI pipeline overview

The main workflow lives in `.github/workflows/ci.yml` and runs on pushes and pull requests. A second workflow, `.github/workflows/pr.yml`, documents the required PR gate for `dev -> main`.

### Stage 1: Format
- **Format check**: `black --check .`

### Stage 2: Lint
- **Lint check**: `ruff check .`

### Stage 3: Unit tests
- **Test runner**: `pytest -q`
- Uploads a JUnit XML result artifact for debugging.

### Stage 4: Build/package
- **Build command**: `python -m build`
- Uploads generated `dist/` files as a GitHub Actions artifact.

## Best-practice choices used

- **Least-privilege permissions** in workflow (`contents: read`).
- **Concurrency control** to cancel stale runs on the same branch/PR.
- **Pip cache** via `actions/setup-python` to speed up repeated runs.
- **Sequential job dependencies** (`needs`) for explicit CI gates.
- **Pinned tool versions** in `requirements-dev.txt` for reproducible checks.
- **Separate PR workflow** so the `dev -> main` merge policy is obvious in GitHub.

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
├── .github/workflows/pr.yml      # Pull request gate description for required checks
├── app.py                        # Tiny application module used by tests
├── test_app.py                   # Unit tests validating app behavior
├── pyproject.toml                # Packaging metadata + tool config for black/ruff/pytest
├── requirements-dev.txt          # Pinned dev dependencies for CI and local checks
├── CHEATSHEET.md                 # Command reference (Python, CI, Git, troubleshooting)
├── FILES_EXPLAINED.md            # File-by-file purpose list
├── .gitignore                    # Ignore local env/build/cache artifacts
└── README.md                     # CI documentation, stages, and local run guide
```

## Why this repository exists

- Keep code intentionally small so CI design is easy to understand.
- Provide a clean baseline that teams can copy and extend.
- Demonstrate the same checks locally and in CI for predictable results.

## Suggested branch flow

- Work on `dev`.
- Open a pull request from `dev` into `main`.
- Mark `ci / Stage 1 - Format check`, `ci / Stage 2 - Lint`, `ci / Stage 3 - Unit tests`, and `ci / Stage 4 - Build package` as required checks in GitHub.
