# CI & Local Dev Cheatsheet

## 1) Environment setup

```bash
python --version                        # Verify local Python version
python -m venv .venv                    # Create isolated virtual environment
source .venv/bin/activate               # Activate environment (Linux/macOS)
python -m pip install --upgrade pip     # Update pip to latest
pip install -r requirements-dev.txt     # Install formatter/linter/test/build tools
```

## 2) Code quality

```bash
black .                                 # Auto-format code
black --check .                         # CI-style format validation
ruff check .                            # Lint code for errors/style issues
ruff check . --fix                      # Auto-fix safe lint issues
```

## 3) Testing

```bash
pytest -q                               # Run all tests in quiet mode
pytest -k even -q                       # Run tests filtered by keyword
pytest --maxfail=1 -q                   # Stop after first failing test
pytest -q test_app.py::test_add         # Run one specific test
```

## 4) Packaging

```bash
python -m build                         # Build source + wheel into dist/
ls -lh dist                             # List generated package artifacts
```

## 5) Useful Git commands (expanded)

```bash
git status                              # Show working tree changes
git switch -c feat/ci-improvement       # Create and switch to new branch
git fetch origin                        # Fetch remote refs

git add .                               # Stage all modified/new files
git add -p                              # Stage changes interactively

git commit -m "feat(ci): improve quality gates"   # Create commit

git log --oneline --decorate -n 10      # Compact recent commit history
git show --stat HEAD                    # Show latest commit summary
git diff                                # Diff unstaged changes
git diff --staged                       # Diff staged changes

git restore --staged <file>             # Unstage a file
git restore <file>                      # Discard unstaged changes to a file

git rebase origin/main                  # Rebase branch onto latest main
git cherry-pick <commit_sha>            # Apply one commit onto current branch

git push origin HEAD                    # Push current branch
git push --force-with-lease             # Safer force push after rebase
```

## 6) CI troubleshooting

```bash
rm -rf .pytest_cache build dist *.egg-info __pycache__  # Clean generated artifacts
python -m pip cache purge                               # Clear pip cache
python -m compileall app.py test_app.py                 # Quick Python syntax check
```
