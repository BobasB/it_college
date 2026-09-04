## Purpose
Short, actionable guidance to help AI coding agents contribute to the main IT College teaching repository.

## Language and audience
- Use Ukrainian for new instructional text, explanations in README files, and student-facing examples unless the surrounding file clearly uses another language.
- Keep examples accessible to students: prefer explicit code and small focused changes over abstractions or broad refactors.

## Big picture
- This repo is an educational collection of labs, notebooks and small examples for teaching Python and related topics. Major areas are:
  - `notes/` — lesson notes and lab instructions (entry point: `notes/README.md`).
  - `example/` — small runnable examples and tests (e.g., `example/coverage_io/app.py`, `example/coverage_io/test.py`).
  - `reports/` — report templates and assets.
- This repository is one of several independent Git repositories in the parent workspace. Run Git commands and project commands from this repository root, not from the workspace container.

## What to change and why
- Prefer small, self-contained edits: fix bugs in example scripts, improve notebook clarity, or add short unit tests.
- Avoid large refactors or introducing new frameworks; this repo is a teaching corpus and should remain accessible.

## Project conventions and patterns
- Code examples are mostly plain Python files and Jupyter notebooks. Notebooks live under `example/` and `notes/`.
- Tests use `unittest` and simple pytest-style functions inside example modules (see `example/coverage_io/test.py` and `example/coverage_io/app.py`).
- Some examples intentionally contain bugs for teaching (e.g., `example/coverage_io/app.py` returns `self.type` in `get_figure_length`). When changing, add a test that demonstrates the correct behavior.
- Read the relevant lesson README before changing an exercise; an apparently incorrect implementation may be part of the teaching task.

## Developer workflows (commands you can run locally)
- Run unit tests in a folder (using Python 3.x):
  - python -m unittest discover example/coverage_io
- Or run a single test module:
  - python -m unittest example.coverage_io.test -v
- The repository CI uses Python 3.10 with pytest and coverage; the exact workflow is in `.github/workflows/coverage.yml`.
- Many examples are notebooks. Use your preferred Jupyter tooling to run or export them.

## Files worth referencing for context
- `notes/README.md` — lab structure and ordering used by instructors.
- `example/coverage_io/app.py` — demonstrates a simple class + pytest-style test function.
- `example/coverage_io/test.py` — shows use of `unittest` and test fixtures.
- `notes/07_testing/README.md` — documents the Poetry, pytest, coverage, and integration-testing workflow used in the teaching material.

## How AI agents should propose changes
- Make minimal, well-tested edits. If fixing a bug, add or update a unit test demonstrating the bug and the fix.
- For notebooks, prefer editing cells that improve clarity (comments, minor code fixes). Keep notebook outputs minimal or cleared when committing.
- Before editing, check `git status` and preserve unrelated user changes. Do not commit unless explicitly requested.
- Include a short change summary referencing the affected lesson; do not create a commit as part of ordinary work.

## Examples (concrete guidance)
- Fixing the `get_figure_length` bug: update `example/coverage_io/app.py` to return `self.length`, then add or enable a test in `example/coverage_io/test.py` asserting the length.
- When adding tests, keep them deterministic (avoid randomness) or seed RNGs; existing tests use `random.choice` and `randint` — consider replacing with fixed values in new tests.

## Constraints and Do-not-touch
- Do not add heavy dependencies or CI changes without maintainers' approval. This repository is intended to be lightweight and educational.
- Avoid mass formatting edits across notebooks; prefer targeted, human-readable changes.
- Do not commit virtual environments, `.env` files, caches, coverage output, or generated notebook artifacts.

If anything in these notes is unclear or you want more examples for a specific directory, tell me which area to expand.
