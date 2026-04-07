# CI/CD Explained — GitHub Actions Basics

Real notes on what each stage of this pipeline does and why it's structured this way.

---

## Why This Pipeline Structure?

The pipeline has two separate workflow files:

- `ci.yml` — runs on every push to `main` and `dev`
- `pr.yml` — runs on pull requests targeting `main`

**Why separate?** PRs need additional context (conflict check, PR metadata). Push workflows just need to validate the commit. Merging them would add noise.

---

## Stage-by-Stage Breakdown

### Stage 1: Structure Check

```yaml
run: |
  required_files=(
    "README.md"
    ".github/workflows/ci.yml"
    "scripts/hello.sh"
  )
  for file in "${required_files[@]}"; do
    test -f "$file" || { echo "Missing: $file"; exit 1; }
  done
```

**Why**: Catches accidental deletions before any code runs. Fast (~5s). Runs first because subsequent stages depend on these files existing.

### Stage 2: Shell Lint (ShellCheck)

ShellCheck catches real bugs in bash scripts:
- Quoting issues (`$var` vs `"$var"`)
- Uninitialized variables
- Incorrect use of `[` vs `[[`
- Deprecated syntax that varies across bash versions

### Stage 3: Script Tests

```bash
bash scripts/hello.sh
```

Simple smoke test. For scripts that emit specific output, we also check:

```bash
output=$(bash scripts/hello.sh)
[ "$output" = "expected output" ] || exit 1
```

### Stage 4: Final Status Gate

```yaml
if: always()
needs:
  - structure-check
  - shellcheck
  - script-tests
```

The `if: always()` ensures this runs even if earlier jobs fail. It then checks each job's result and fails if any were `failure` or `cancelled`. This ensures the overall workflow is marked as failed even when some jobs are skipped.

---

## Managing GitHub Secrets

For repos that use secrets in CI:

1. Go to **Settings → Secrets and variables → Actions**
2. Click **New repository secret**
3. Name it with `SCREAMING_SNAKE_CASE` (e.g., `DOCKERHUB_TOKEN`)
4. Reference it in workflow: `${{ secrets.DOCKERHUB_TOKEN }}`

**Best practices**:
- Never echo a secret value in a run step
- Use environment-scoped secrets for production (`environment: prod`)
- Rotate PATs and tokens every 90 days
- Use OIDC (Workload Identity Federation) for cloud credentials instead of long-lived keys

---

## Adding a CI Status Badge

Add to `README.md`:

```markdown
[![CI](https://github.com/gio506/github-actions-ci-basics/actions/workflows/ci.yml/badge.svg)](https://github.com/gio506/github-actions-ci-basics/actions/workflows/ci.yml)
```

The badge shows the status of the latest run on the default branch. It turns red on failure, green on success.

---

## Debugging a Failed Workflow

```bash
# Check run locally using act (docker-based GitHub Actions runner)
act push --job shellcheck

# Or add a debug step to the workflow temporarily
- name: Debug environment
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    env | sort
```
