# Contributing to holidays-pt

Thank you for taking the time to contribute! 🎉
All types of contributions are welcome and appreciated — from bug reports to code improvements and documentation fixes.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Report a Bug](#how-to-report-a-bug)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Contribution](#your-first-contribution)
- [Development Setup](#development-setup)
- [Branch Naming Convention](#branch-naming-convention)
- [Commit Messages](#commit-messages)
- [Pull Request / Merge Request Process](#pull-request--merge-request-process)
- [Style Guide](#style-guide)
- [Available Labels](#available-labels)

---

## Code of Conduct

This project is open and welcoming to everyone. Please be respectful, constructive, and considerate when interacting with other contributors.

---

## How to Report a Bug

1. Check the [issue tracker](https://gitlab.com/majramos/holidays-pt/-/work_items) to see if the bug has already been reported.
2. If not, open a new issue and apply the **`bug`** label.
3. Include the following in your report:
   - A clear and descriptive title
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Your OS/distro and Python version
   - Any relevant logs or error output

> If the bug is severe or causes data loss, also apply the **`critical`** label.

---

## Suggesting Enhancements

1. Check the [issue tracker](https://gitlab.com/majramos/holidays-pt/-/work_items) for similar suggestions.
2. Open a new issue with the **`suggestion`** or **`enhancement`** label.
3. Describe:
   - What the feature does and why it would be useful
   - Any alternatives you considered
   - Example usage or expected output

For broader discussion topics, open an issue with the **`discussion`** label.

---

## Your First Contribution

Not sure where to start? Look for issues labeled **`support`** or **`documentation`** — these are usually good entry points that don't require deep knowledge of the codebase.

Steps for a typical contribution:

1. Fork the repository
2. Clone your fork locally:
   ```bash
   git clone https://gitlab.com/<YOUR_USERNAME>/holidays-pt.git
   cd holidays-pt
   ```
3. Create a new branch following the [naming convention](#branch-naming-convention)
4. Make your changes
5. Test your changes
6. Push your branch and open a Merge Request

---

## Development Setup

**Requirements:** Python 3.8+ and [uv](https://docs.astral.sh/uv/)

This project uses **uv** for dependency and environment management. All commands must be run through `uv`.

```bash
# Clone the repo (or your fork)
git clone https://gitlab.com/majramos/holidays-pt.git
cd holidays-pt

# Install all dependencies (including dev)
uv sync
```

### Running Checks Locally

Before opening a Merge Request, make sure all the following pass — they are enforced by the CI pipeline.

**1. Format & Lint (Ruff)**

```bash
# Check formatting
uv run ruff format --check

# Check linting rules
uv run ruff check
```

To auto-fix formatting and safe lint issues:

```bash
uv run ruff format
uv run ruff check --fix
```

**2. Type Checking (Mypy)**

```bash
uv run mypy
```

**3. Tests (Pytest)**

```bash
uv run pytest
```

> All three stages must pass before a Merge Request can be approved and merged.

---

## Branch Naming Convention

All branches must follow the pattern:
<type>/<issue-id>-<short-description>

If no issue is associated, the shorter form is acceptable:
<type>/<short-description>

### Allowed Types

| Type | Purpose |
|-----------|----------------------------------------------|
| `feature` | New functionality |
| `bugfix` | Fix a bug in an existing feature |
| `hotfix` | Urgent production fix |
| `refactor` | Code improvements without behavior changes |
| `docs` | Documentation-only changes |
| `test` | Adding or modifying tests |
| `chore` | Build process, dependency updates, CI config |

### Rules

- Use **lowercase only**
- Use **hyphens** (`-`) to separate words — no underscores or spaces
- Keep descriptions **concise** (under 50 characters)
- Be specific: `feature/add-dnf-support` not `feature/update`
- Never use bare numbers as leading parts

### Examples

```bash
# Good
feature/42-add-dnf-support
bugfix/17-fix-apt-version-parsing
docs/update-readme
chore/upgrade-dependencies
refactor/clean-package-detection-logic

# Bad
fix                          # too vague
Feature/AddDnf               # uppercase and no hyphens
update_stuff                 # underscore + generic name
```

---

## Commit Messages

This project uses the [Conventional Commits](https://www.conventionalcommits.org/) specification and the [Commitizen](https://commitizen-tools.github.io/commitizen/) tool for creating commit messages.

When committing changes, use Commitizen instead of writing the commit message manually:

```bash
cz commit
```

Commitizen will guide you through the required fields and generate a commit message that matches the expected format.

### Required Format

```text
<type>(<scope>): <short description>
```

### Allowed Commit Types

- `feat`: A new feature. Correlates with **MINOR** in SemVer.
- `fix`: A bug fix.
- `docs`: Documentation only changes.
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semicolons, etc.).
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `perf`: A code change that improves performance.
- `test`: Adding missing or correcting existing tests.
- `build`: Changes that affect the build system or external dependencies (example scopes: `pip`, `docker`, `npm`).
- `ci`: Changes to CI configuration files and scripts (example scopes: `GitLabCI`).
- `chore`: Maintenance tasks, dependency housekeeping, or tooling changes not covered above.

### Commit Rules

- Use the **imperative mood** in the description, for example `add`, not `added`.
- Keep the first line under **72 characters**.
- Add the related issue in the commit body when applicable, for example `Closes #42`.
- Note that **branch types** and **commit types** are not always the same; for example, a `feature/...` branch will usually contain a `feat(...)` commit.

### Commit Examples

```text
feat(checker): add support for pacman package manager
fix(apt): handle empty version string in parser
docs(readme): add installation instructions
style(lint): reformat shell scripts
refactor(core): simplify update detection logic
perf(parser): reduce package scan overhead
test(dnf): add unit tests for version comparison
build(docker): update base image to python 3.12
ci(gitlab): run tests on merge requests
chore(deps): bump requests to 2.31.0
```

---

## Pull Request / Merge Request Process

1. Ensure your branch is up to date with `main` before opening an MR
2. Fill in the MR description — explain what changed and why
3. Link the relevant issue (e.g. `Closes #17`)
4. Make sure all checks pass **locally** before pushing:
   - `uv run ruff format --check`
   - `uv run ruff check`
   - `uv run mypy`
   - `uv run pytest`
5. The CI pipeline will automatically run all checks on the MR — fix any failures before requesting review
6. Wait for a maintainer review and address any requested changes
7. Once approved, the maintainer will merge your MR

---

## Style Guide

- **[Ruff](https://docs.astral.sh/ruff/)** is used for both formatting and linting — do not use `black` or `flake8`
- **[Mypy](https://mypy.readthedocs.io/)** for static type checking — type hints are **required** for all function signatures
- **[PEP 8](https://pep8.org/)** conventions apply where Ruff does not already enforce them
- Write **docstrings** for all public functions, classes, and modules
- Keep functions small, focused, and well-named

---

## CI Pipeline

Every Merge Request and push to `main` runs the following pipeline stages automatically:

| Stage | Tool | Command |
|-------|------|---------|
| `fmt` | Ruff | `ruff format --check` + `ruff check` |
| `style` | Mypy | `mypy` |
| `test` | Pytest | `pytest --junitxml=report.xml` |

All stages must pass for an MR to be eligible for merge. Run them locally with `uv run <command>` before pushing to avoid CI failures.

---

## Available Labels

Use these labels when creating issues to help with triage:

| Label | When to use |
|---------------|------------------------------------------------------|
| `bug` | Something is not working as expected |
| `confirmed` | Bug has been confirmed and reproduced |
| `critical` | Severe bug causing crashes or data loss |
| `discussion` | Topic open for broader conversation |
| `documentation`| Related to docs, README, or inline comments |
| `enhancement` | Improvement to an existing feature |
| `suggestion` | A new feature idea proposed by the community |
| `support` | Question or help request |
