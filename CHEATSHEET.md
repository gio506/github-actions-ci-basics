# CI & Local Dev Cheatsheet

## Environment setup

```bash
python --version                 # confirm Python is available
python -m venv .venv             # create isolated environment
source .venv/bin/activate        # activate venv (Linux/macOS)
pip install -r requirements-dev.txt  # install formatter, linter, test, build tools
```

## Code quality commands

```bash
black .                          # auto-format code
black --check .                  # fail if formatting is needed
ruff check .                     # run static lint checks
ruff check . --fix               # auto-fix some lint findings
```

## Testing

```bash
pytest -q                        # run all tests (quiet mode)
pytest -k even -q                # run tests matching expression
pytest --maxfail=1 -q            # stop quickly on first failure
```

## Packaging / artifacts

```bash
python -m build                  # create sdist and wheel in dist/
ls dist                          # inspect generated package files
```

## GitHub Actions tips

```bash
git status                       # see local changes
git add .                        # stage files
git commit -m "feat: add CI pipeline demo"   # create commit
git push origin main             # push changes to trigger CI
```

## Troubleshooting quick fixes

```bash
pip install --upgrade pip        # update pip when installs fail
rm -rf .pytest_cache build dist *.egg-info  # clean common generated artifacts
```
