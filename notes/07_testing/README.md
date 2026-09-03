# Тестування
> Роботу №07 поділено на чотири послідовні частини. Для кожної частини використовуйте окрему папку з матеріалами та прикладами.

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
testpaths = [
	"example/testing"
]
python_files = ["test_*.py"]
markers = [
	"unit: швидкі юніт-тести",
	"integration: інтеграційні тести"
]

[tool.coverage.run]
branch = true
source = ["example/testing"]

[tool.coverage.report]
omit = [
	"*/test_*.py",
	"*/__init__.py"
]
```

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

1. [Загальне тестування та юніт-тести](01_general_and_unittest/README.md)
2. [Тестування з бібліотекою pytest](02_pytest/README.md)
3. [Покриття коду](03_coverage/README.md)
4. [Інтеграційне тестування: вебзастосунки, файли та бази даних](04_integration_testing/README.md)

---
### Здача роботи
- :star: завантажте до репозиторію файли тієї частини, яку виконуєте;
- :star: перевірте, що тести запускаються з командного рядка;
- :star: додайте URL посилання на роботу до завдання в Google Classroom.
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;

---
