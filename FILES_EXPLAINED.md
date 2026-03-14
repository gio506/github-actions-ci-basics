# Files Explained

- `.github/workflows/ci.yml`: 4-stage CI pipeline for format, lint, tests, and build.
- `.github/workflows/pr.yml`: pull request workflow documenting the required CI checks.
- `CHEATSHEET.md`: quick local commands for Python, GitHub Actions, and Git.
- `FILES_EXPLAINED.md`: short description of every tracked file.
- `README.md`: main project guide and CI overview.
- `app.py`: tiny Python module used by the tests and packaging step.
- `pyproject.toml`: package metadata plus Black, Ruff, and pytest settings.
- `requirements-dev.txt`: pinned development dependencies used locally and in CI.
- `test_app.py`: unit tests for the demo application.
