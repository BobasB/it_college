# Тестування
> Роботу №07 поділено на чотири послідовні частини. Для кожної частини використовуйте окрему папку з матеріалами та прикладами. Даний опис містить загальне налаштування проєкту та інструкції щодо запуску тестів.

## Мета роботи
Навчитись перевіряти правильність програм автоматично: писати юніт-тести (`unittest`, `pytest`), вимірювати покриття коду (`coverage`) та тестувати взаємодію компонентів (веб, база даних, файли).

## Що потрібно знати / підготувати
- виконані роботи про [ООП](../05_OOP_first_class/README.md) та [віртуальні середовища](../06_python_virtualenvs/README.md);
- Python 3.13+ та Poetry (`poetry --version`) або віртуальне середовище з `pip`;
- робочі приклади лежать у [example/testing](../../example/testing); їх можна запускати прямо з цих папок (див. нижче).

## Порядок виконання
1. [Загальне тестування та юніт-тести](01_general_and_unittest/README.md)
2. [Тестування з бібліотекою pytest](02_pytest/README.md)
3. [Покриття коду](03_coverage/README.md)
4. [Інтеграційне тестування: вебзастосунки, файли та бази даних](04_integration_testing/README.md)

## Швидкий запуск прикладів
У кожній папці `example/testing/*` є власний `app.py`, тому тести запускаються **з відповідної папки** (інакше `pytest` повідомить `import file mismatch`, адже файли `test_app.py` та `app.py` називаються однаково в різних папках):
```bash
cd example/testing/02_pytest
python -m pytest -v
```

## Формат проєкту
Робота виконується як окремий Python-проєкт із використанням [Poetry](https://python-poetry.org/). Poetry створює ізольоване середовище, встановлює залежності та зберігає їхні сумісні версії у файлі `poetry.lock`.

1. Створіть або ініціалізуйте проєкт у кореневій папці роботи:
	```bash
	poetry init
	poetry install
	```
2. Основні залежності проєкту та інструменти для розробки потрібно розділяти. Бібліотеки, необхідні для роботи програми, додаються у звичайну групу, а тестові інструменти — у групу `dev`:
	```bash
	poetry add flask
	poetry add --group dev pytest pytest-cov coverage
	```
3. Для запуску команд у середовищі проєкту використовуйте `poetry run`:
	```bash
	poetry run pytest
	poetry run coverage report -m
	```
4. Перевірте у `pyproject.toml`, що залежності потрапили до правильних груп. Не встановлюйте їх глобально через `pip`, якщо команда запускається через Poetry.

## Конфігурація у pyproject.toml
Файл `pyproject.toml` використовується не лише для залежностей. У ньому можна зберігати налаштування `pytest`, coverage та інших інструментів проєкту в одному місці:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
markers = [
	"unit: швидкі юніт-тести",
	"integration: інтеграційні тести"
]

[tool.coverage.run]
branch = true
source = ["app"]

[tool.coverage.report]
omit = [
	"*/test_*.py",
	"*/__init__.py"
]
```

> [!WARNING]
> Не вказуйте у `testpaths` одразу всі папки `example/testing/*`: у них однакові назви `app.py` та `test_app.py`, і `pytest` завершиться помилкою `import file mismatch`. У власному проєкті тримайте один `app.py` та тести в одній папці.

Такі налаштування дозволяють запускати короткі команди без повторення параметрів:
```bash
poetry run pytest
poetry run pytest -m integration
poetry run pytest --cov --cov-report=term-missing
```

## Автоматизація за допомогою Makefile
`Makefile` містить іменовані команди для повторюваних дій. Це спрощує запуск тестів і coverage та зменшує кількість команд, які потрібно запам'ятовувати. Створіть `Makefile` у корені Poetry-проєкту:

```make
.PHONY: install test unit integration coverage html clean

install:
	poetry install

test:
	poetry run pytest -v

unit:
	poetry run pytest -m unit -v

integration:
	poetry run pytest -m integration -v

coverage:
	poetry run pytest --cov --cov-report=term-missing

html:
	poetry run pytest --cov --cov-report=html

clean:
	rm -rf .pytest_cache htmlcov .coverage
```

Запуск команд виконується за назвою цілі:
```bash
make install
make test
make unit
make integration
make coverage
make html
make clean
```

У `Makefile` кожен відступ перед командою має бути символом табуляції. Цілі `unit` та `integration` працюватимуть після додавання відповідних маркерів до тестів. `make html` створює папку `htmlcov/`, яку не потрібно комітити до репозиторію.

## Критерії оцінювання (для всієї роботи №07)
| Рівень | Що потрібно виконати |
| --- | --- |
| Достатній | виконано :star: завдання частин 1-2, тести проходять |
| Високий | + частина 3 (coverage з branch-звітом) та частина 4 |
| Відмінний | + :fire: завдання, налаштування `pyproject.toml`, `Makefile` та перевірка coverage у CI ([робота №08](../08_github_actions/README.md)) |

## Контрольні питання
1. Чим юніт-тест відрізняється від інтеграційного?
1. Що таке fixture і навіщо вона потрібна?
1. Що означає 100% покриття та чому воно не гарантує відсутність помилок?
1. Для чого потрібні маркери `pytest` і конфігурація у `pyproject.toml`?

---
