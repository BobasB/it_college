[![codecov](https://codecov.io/gh/BobasB/it_college/branch/main/graph/badge.svg?token=QIL2SPR92K)](https://codecov.io/gh/BobasB/it_college)
# Приклади

Робочі приклади коду, на які посилаються [лабораторні роботи](../notes/README.md). Приклади можна запускати локально; нічого не змінюйте в оригіналах — копіюйте їх у папку своєї роботи.

| Папка | Опис | Пов'язана робота | Як запустити |
| --- | --- | --- | --- |
| [basics](./basics) | ноутбуки з основ Python та класів | [04](../notes/04_python_basics/README.md), [05](../notes/05_OOP_first_class/README.md) | відкрити `.ipynb` у VS Code |
| [coverage_io](./coverage_io) | клас `Figure` з **навмисною помилкою** в `get_figure_length`; використовується в CI та Codecov | [07](../notes/07_testing/01_general_and_unittest/README.md), [08](../notes/08_github_actions/README.md) | `cd example/coverage_io && python -m pytest test.py -v` |
| [testing/01_general_and_unittest](./testing/01_general_and_unittest) | `unittest`, `subTest`, `mock` | [07 / 01](../notes/07_testing/01_general_and_unittest/README.md) | `cd example/testing/01_general_and_unittest && python -m unittest -v` |
| [testing/02_pytest](./testing/02_pytest) | `pytest`, fixtures, параметризація | [07 / 02](../notes/07_testing/02_pytest/README.md) | `cd example/testing/02_pytest && python -m pytest -v` |
| [testing/03_coverage](./testing/03_coverage) | вимірювання покриття, `.coveragerc` | [07 / 03](../notes/07_testing/03_coverage/README.md) | `cd example/testing/03_coverage && python -m coverage run -m pytest && python -m coverage report -m` |
| [testing/04_integration_testing](./testing/04_integration_testing) | Flask + SQLite + JSON, інтеграційні тести | [07 / 04](../notes/07_testing/04_integration_testing/README.md) | `cd example/testing/04_integration_testing && python -m pytest -v` (потрібен `flask`) |
| [databases](./databases) | CRUD для SQLite з тестами | [09](../notes/09_databases/README.md) | `cd example/databases && python -m pytest -v` |
| [data_science](./data_science) | приклад аналізу даних (ноутбук) | [11](../notes/11_numpy_basics/README.md) | відкрити `.ipynb` |
| [gw2_economics](./gw2_economics) | аналіз цін (NumPy + matplotlib) з виводом комірок; ноутбук без виводу є в [notes/13_linear_programming/gw2_economics](../notes/13_linear_programming/gw2_economics) | [13](../notes/13_linear_programming/README.md) | відкрити `ecto.ipynb` (потрібен `data.txt` поряд) |
| [multyprocessing](./multyprocessing) | паралельна обробка (скрапер, `tqdm`) | — (додатковий матеріал) | відкрити `main.ipynb` |
| [exam](./exam) | завдання для екзамену / заліку: [oop](./exam/oop), [oop_2](./exam/oop_2), [testing](./exam/testing), [testing/2026](./exam/testing/2026) | — | див. README у кожній папці |

## Правила запуску тестів
- Тести запускаються **з папки прикладу**: у різних папках є файли з однаковими іменами `app.py` та `test_app.py`, тому спільний запуск `pytest example/testing` завершиться помилкою `import file mismatch`.
- Потрібні пакети: `pytest`, `coverage`, `flask` (для `04_integration_testing`). Встановіть їх у віртуальне середовище: `pip install pytest coverage flask`.
- Помилка у [coverage_io/app.py](./coverage_io/app.py) (`get_figure_length` повертає `self.type`) **навмисна** — вона демонструє тест, що виявляє баг. Не виправляйте її без узгодження з викладачем.

## Що не потрібно комітити
`__pycache__/`, `.pytest_cache/`, `.coverage`, `htmlcov/`, `*.db`, `.env`, `.adk/` — усе це вже в [.gitignore](../.gitignore).
