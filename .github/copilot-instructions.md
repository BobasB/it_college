## Purpose
Short, actionable guidance to help AI coding agents contribute to the IT College repository.

## Big picture
- This repo is an educational collection of labs, notebooks and small examples for teaching Python and related topics. Major areas are:
  - `notes/` — lesson notes and lab instructions (entry point: `notes/README.md`).
  - `example/` — small runnable examples and tests (e.g., `example/coverage_io/app.py`, `example/coverage_io/test.py`).
  - `reports/` — report templates and assets.

## What to change and why
- Prefer small, self-contained edits: fix bugs in example scripts, improve notebook clarity, or add short unit tests.
- Avoid large refactors or introducing new frameworks; this repo is a teaching corpus and should remain accessible.

## Project conventions and patterns
- Code examples are mostly plain Python files and Jupyter notebooks. Notebooks live under `example/` and `notes/`.
- Tests use `unittest` and simple pytest-style functions inside example modules (see `example/coverage_io/test.py` and `example/coverage_io/app.py`).
- Some examples intentionally contain bugs for teaching (e.g., `example/coverage_io/app.py` returns `self.type` in `get_figure_length`). When changing, add a test that demonstrates the correct behavior.

## Developer workflows (commands you can run locally)
- Run unit tests in a folder (using Python 3.x):
  - python -m unittest discover example/coverage_io
- Or run a single test module:
  - python -m unittest example.coverage_io.test -v
- Many examples are notebooks. Use your preferred Jupyter tooling to run or export them.

## Files worth referencing for context
- `notes/README.md` — lab structure and ordering used by instructors.
- `example/coverage_io/app.py` — demonstrates a simple class + pytest-style test function.
- `example/coverage_io/test.py` — shows use of `unittest` and test fixtures.

## How AI agents should propose changes
- Make minimal, well-tested edits. If fixing a bug, add or update a unit test demonstrating the bug and the fix.
- For notebooks, prefer editing cells that improve clarity (comments, minor code fixes). Keep notebook outputs minimal or cleared when committing.
- Include a short commit message explaining the intent and referencing the affected lesson (e.g., "fix: get_figure_length to return length — updates example/coverage_io tests").

## Examples (concrete guidance)
- Fixing the `get_figure_length` bug: update `example/coverage_io/app.py` to return `self.length`, then add or enable a test in `example/coverage_io/test.py` asserting the length.
- When adding tests, keep them deterministic (avoid randomness) or seed RNGs; existing tests use `random.choice` and `randint` — consider replacing with fixed values in new tests.

## Constraints and Do-not-touch
- Do not add heavy dependencies or CI changes without maintainers' approval. This repository is intended to be lightweight and educational.
- Avoid mass formatting edits across notebooks; prefer targeted, human-readable changes.

If anything in these notes is unclear or you want more examples for a specific directory, tell me which area to expand.
