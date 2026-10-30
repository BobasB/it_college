## Purpose
Short, actionable guidance for AI coding agents contributing to the IT College teaching repository. Full rules for all agents are in [AGENTS.md](../AGENTS.md) — read it first; this file highlights what matters most for Copilot.

## Language and audience
- Use Ukrainian for new instructional text, explanations in README files, and student-facing examples unless the surrounding file clearly uses another language.
- Keep examples accessible to beginners: explicit code, small focused changes, no broad refactors or abstractions.

## Big picture
- Educational collection of labs, notebooks and small examples for teaching Python and related topics:
  - `notes/` — lab instructions (entry point and order: `notes/README.md`; new labs follow `notes/LAB_TEMPLATE.md`).
  - `example/` — runnable examples and tests (index: `example/README.md`).
  - `reports/` — student report template.
  - `.github/workflows/` — CI (`coverage.yml`, `manual.yml`; `cron.md` is a disabled example).
- This repository is one of several independent Git repositories in the parent workspace. Run Git and project commands from this repository root, not from the workspace container.

## Lab README structure
Every lab README has: Мета → Що потрібно знати → Хід роботи → Що має бути у звіті → Критерії оцінювання → Контрольні питання → Здача роботи. Markers: `:star:` (must appear in the report), `:fire:` (advanced), `> [!WARNING]` (common mistake). Give OS-specific commands for Windows and macOS/Linux when they differ. Verify every command/snippet you add by running it.

## Project conventions
- Examples are plain Python files and Jupyter notebooks (under `example/` and `notes/`).
- Tests use `unittest` and `pytest`; each folder in `example/testing/*` has its own `app.py`/`test_app.py`, so **run tests from the example folder** (a combined `pytest example/testing` fails with `import file mismatch`).
- Some examples intentionally contain bugs for teaching (e.g. `example/coverage_io/app.py` returns `self.type` from `get_figure_length`, and its length test is commented out). Read the lab README before “fixing” anything; if you do fix it, add a test demonstrating the correct behavior.
- Keep notebooks in `notes/` without outputs; edit individual cells, avoid mass formatting; use NumPy 2.x-compatible code.

## Developer workflows
```bash
cd example/coverage_io && python -m pytest test.py -v            # same as CI
cd example/testing/02_pytest && python -m pytest -v
cd example/testing/03_coverage && python -m coverage run -m pytest && python -m coverage report -m
cd example/testing/04_integration_testing && python -m pytest -v  # needs flask
cd example/databases && python -m pytest -v
```
- CI (`.github/workflows/coverage.yml`) uses Python 3.10, `pytest` and `coverage`, then uploads to Codecov.
- Dependencies for examples: `pytest`, `coverage`, `flask`. Labs on agents use Poetry (`notes/06_python_agents/pyproject.toml`, Python 3.13+).

## Files worth referencing
- `AGENTS.md` — full agent rules, commands and checklist.
- `notes/README.md` — lab order; `notes/LAB_TEMPLATE.md` — template for new labs.
- `example/README.md` — map of examples and how to run each.
- `example/coverage_io/app.py`, `example/coverage_io/test.py` — class + tests with an intentional bug.
- `notes/07_testing/README.md` — Poetry, pytest, coverage and integration-testing workflow.

## How to propose changes
- Make minimal, well-tested edits. For a bug fix add or update a test showing the bug and the fix.
- Check `git status` first and preserve unrelated user changes. Do not commit unless asked; work on a separate branch for pull requests.
- Include a short change summary referencing the affected lesson.

## Constraints and do-not-touch
- No heavy dependencies, new frameworks or CI changes without maintainers' approval.
- Never commit virtual environments, `.env` files or API keys (use `.env.example`), caches, `*.db`, coverage output, `.DS_Store` or generated notebook artifacts.
- Use parameterized SQL (`?`) in every example.
- Avoid mass formatting edits across notebooks; prefer targeted, human-readable changes.
