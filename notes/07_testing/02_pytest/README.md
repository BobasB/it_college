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
2. Fixture підготовлює потрібні тесту дані або ресурси:
    ```python
    @pytest.fixture
    def square():
        return Figure("квадрат", 5)
    ```

### Детальніше про fixtures
Тест запитує fixture через аргумент із такою самою назвою. Pytest сам викликає її та передає результат у тест:
```python
def test_square_length(square):
    assert square.get_figure_length == 5
```
За замовчуванням fixture має область дії `function`: pytest створює її окремо для кожного тесту. Це допомагає тестам не змінювати спільні дані та не залежати один від одного.

Fixtures можуть залежати від інших fixtures. Залежності також вказують аргументами, а pytest сам визначає порядок їх підготовки:
```python
@pytest.fixture
def length():
    return 10

@pytest.fixture
def square(length):
    return Figure("квадрат", length)

def test_square_length(square):
    assert square.get_figure_length == 10
```
Якщо одна fixture потрібна кілька разів у межах одного тесту, pytest використовує її результат повторно, а не створює новий об'єкт.

Якщо після тесту потрібно звільнити ресурс або прибрати створені дані, використовуйте `yield`. Код після `yield` виконається під час очищення, навіть якщо тест завершився помилкою:
```python
@pytest.fixture
def text_file(tmp_path):
    path = tmp_path / "result.txt"
    path.write_text("готово", encoding="utf-8")
    yield path
    path.unlink()

def test_text_file(text_file):
    assert text_file.read_text(encoding="utf-8") == "готово"
```
`tmp_path` — вбудована fixture pytest для окремої тимчасової папки кожного тесту. Також корисні `monkeypatch` для тимчасової заміни атрибутів і змінних середовища та `capsys` для перевірки виводу в консоль.

- :star: Додайте параметризований тест для всіх дозволених фігур.
- :star: Створіть fixture, яка повертає фігуру з довжиною 10, і перевірте її властивості.
- :fire: Додайте тест для кожного неправильного типу та кожного неправильного значення довжини.

## Розширені можливості pytest
1. Параметр `scope` задає, як довго pytest повторно використовує результат fixture:
    ```python
    @pytest.fixture(scope="module")
    def allowed_figures():
        return Figure.FIGURES
    ```
   Доступні значення: `function` (один тест, типове), `class`, `module`, `package` та `session` (увесь запуск тестів). Ширшу область дії варто обирати для дорогих у створенні ресурсів; змінюваний спільний стан може зробити тести залежними один від одного.
2. Fixtures можна позначити `autouse=True`, щоб pytest запускав їх автоматично для відповідної області видимості, навіть якщо тест не вказує fixture аргументом. Використовуйте це лише для справді спільної підготовки: приховані залежності складніше помітити.
3. Спільні fixtures можна розмістити у `conftest.py`. Pytest знаходить цей файл для тестів у відповідній папці та її підпапках, тож імпортувати fixtures у тести не потрібно.
4. Маркери дозволяють об'єднати тести за призначенням:
    ```python
    @pytest.mark.unit
    def test_triangle_type():
        assert Figure("трикутник", 4).type == "трикутник"
    ```
   Запуск тестів із маркером:
    ```bash
    pytest -m unit -v
    ```
5. Щоб pytest знав про власний маркер, додайте його до `pyproject.toml`:
    ```toml
    [tool.pytest.ini_options]
    markers = [
        "unit: швидкі юніт-тести",
        "slow: повільні тести"
    ]
    ```
6. Корисні команди для пошуку проблем:
    ```bash
    pytest --collect-only
    pytest -x
    pytest --tb=short
    ```
   `--collect-only` показує знайдені тести, `-x` зупиняє запуск після першої помилки, а `--tb=short` скорочує traceback.
7. :star: Додайте маркер `unit` до двох тестів і запустіть лише їх.
8. :star: Створіть fixture зі `scope="module"` та перевірте, що її можна використовувати у двох тестах.
9. :fire: Навмисно зламайте один тест, запустіть `pytest -x --tb=short` і поясніть результат.

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