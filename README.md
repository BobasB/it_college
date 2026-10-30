[![Manual workflow](https://github.com/BobasB/it_college/actions/workflows/manual.yml/badge.svg)](https://github.com/BobasB/it_college/actions/workflows/manual.yml)
[![Coverage workflow](https://github.com/BobasB/it_college/actions/workflows/coverage.yml/badge.svg)](https://github.com/BobasB/it_college/actions/workflows/coverage.yml)
[![codecov](https://codecov.io/gh/BobasB/it_college/branch/main/graph/badge.svg?token=QIL2SPR92K)](https://codecov.io/gh/BobasB/it_college)

---
# IT College
Навчальний репозиторій для занять у Львівському ІТ Коледжі: лабораторні роботи, приклади коду та шаблон звіту. Основна мова курсу — Python.

## Структура репозиторію
| Папка | Призначення |
| --- | --- |
| [`notes/`](./notes/README.md) | Інструкції до лабораторних робіт (точка входу — [`notes/README.md`](./notes/README.md)) |
| [`example/`](./example/README.md) | Робочі приклади коду, ноутбуки, тести та екзаменаційні завдання |
| [`reports/`](./reports/README.md) | Шаблон звіту та приклад його оформлення |
| [`.github/`](./.github) | CI (GitHub Actions) та інструкції для Copilot / AI-агентів |

## Швидкий старт
1. [Лабораторні роботи](./notes/README.md) — оберіть потрібну тему та виконуйте кроки по порядку;
1. [Шаблон звіту](./reports/README.md) — скопіюйте його у папку своєї роботи;
1. [Приклади](./example/README.md) — перевірені приклади коду, на які посилаються лабораторні.

## Вимоги до середовища
- Python 3.13+ (CI використовує Python 3.10 для прикладу `example/coverage_io`);
- Git та Visual Studio Code з розширеннями `Python`, `Jupyter`, `GitHub Copilot`;
- додаткові інструменти (Poetry, Pipenv) встановлюються в ході відповідних робіт.

## Для викладачів та AI-агентів
Правила внесення змін у репозиторій описані в [`AGENTS.md`](./AGENTS.md) та [`.github/copilot-instructions.md`](./.github/copilot-instructions.md).

---
