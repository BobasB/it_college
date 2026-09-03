# Тестування з бібліотекою pytest
> `pytest` — стороння бібліотека, яка дозволяє писати короткі тести у вигляді звичайних функцій.

## Встановлення
1. Створіть або використайте віртуальне середовище з попередньої роботи.
2. Встановіть бібліотеку як залежність для розробки:
    ```bash
    pip install pytest
    # або
    poetry add --group dev pytest
    ```
3. Документація: [pytest](https://docs.pytest.org/).

## Основи
1. У файлі `test_app.py` функції з назвою `test_` автоматично розпізнаються як тести.
2. Для перевірки достатньо звичайного `assert`:
    ```python
    def test_triangle_type():
        triangle = Figure("трикутник", 4)
        assert triangle.type == "трикутник"
    ```
3. Винятки перевіряються через `pytest.raises`:
    ```python
    def test_invalid_length():
        with pytest.raises(AssertionError):
            Figure("квадрат", 0)
    ```
4. Запустіть приклад:
    ```bash
    cd example/testing/02_pytest
    pytest -v
    pytest test_app.py::test_triangle_type -v
    ```

## Параметризація та fixtures
1. `pytest.mark.parametrize` дозволяє виконати один тест для кількох наборів даних:
    ```python
    @pytest.mark.parametrize("figure", Figure.FIGURES)
    def test_allowed_figure(figure):
        assert Figure(figure, 1).type == figure
    ```
2. Fixture підготовлює спільні дані для тестів:
    ```python
    @pytest.fixture
    def square():
        return Figure("квадрат", 5)
    ```
3. :star: Додайте параметризований тест для всіх дозволених фігур.
4. :star: Створіть fixture, яка повертає фігуру з довжиною 10, і перевірте її властивості.
5. :fire: Додайте тест для кожного неправильного типу та кожного неправильного значення довжини.

## Розширені можливості pytest
1. Fixture за замовчуванням створюється для кожного тесту. Параметр `scope` змінює час її існування:
    ```python
    @pytest.fixture(scope="module")
    def allowed_figures():
        return Figure.FIGURES
    ```
   Доступні поширені значення: `function`, `class`, `module`, `session`.
2. Маркери дозволяють об'єднати тести за призначенням:
    ```python
    @pytest.mark.unit
    def test_triangle_type():
        assert Figure("трикутник", 4).type == "трикутник"
    ```
   Запуск тестів із маркером:
    ```bash
    pytest -m unit -v
    ```
3. Щоб pytest знав про власний маркер, додайте його до `pyproject.toml`:
    ```toml
    [tool.pytest.ini_options]
    markers = [
        "unit: швидкі юніт-тести",
        "slow: повільні тести"
    ]
    ```
4. Корисні команди для пошуку проблем:
    ```bash
    pytest --collect-only
    pytest -x
    pytest --tb=short
    ```
   `--collect-only` показує знайдені тести, `-x` зупиняє запуск після першої помилки, а `--tb=short` скорочує traceback.
5. :star: Додайте маркер `unit` до двох тестів і запустіть лише їх.
6. :star: Створіть fixture зі `scope="module"` та перевірте, що її можна використовувати у двох тестах.
7. :fire: Навмисно зламайте один тест, запустіть `pytest -x --tb=short` і поясніть результат.

## Організація тестів
- назви файлів мають відповідати шаблонам `test_*.py` або `*_test.py`;
- назви функцій тестів мають починатися з `test_`;
- спільні fixtures можна зберігати у файлі `conftest.py`;
- кожен тест повинен перевіряти одну зрозумілу поведінку;
- не використовуйте випадкові дані без фіксованого seed, інакше результат може змінюватися.

### Звіт
- наведіть команду встановлення `pytest`;
- додайте результат запуску з `-v`;
- поясніть різницю між тестом `unittest.TestCase` та функцією `pytest`;
- додайте приклад використання параметризації, fixture або маркера.