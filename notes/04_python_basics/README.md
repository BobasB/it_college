# Основи програмування на Python

## Мета роботи: __Навчитись застосовувати основні конструкції мови Python, виконати всі приклати та з використанням AI створити власні приклади які демонструють особливості кодових конструкцій Pyhton__

### Основні конструкції в Python
1. :star: виконайте приклади коду на Python представлені нижче та вставте їх у звіт;
1. :star: якщо важко придумати з чим попрацювати в кожному завданні (не знаєте який цикл написати, або яку змінну вивести) - запитайтесь у ChatGPT який би він приклад навів та вставте його відповідь у звіт (перед тим правильно відформутувавши її);
1. Створіть Python файл `*.py` або `.ipynb` в якому будете виконувати базові приклади. Застосовуючи команду `print` виконайте наступне:
    1. Познайомтесь з основними [типами даних](https://docs.python.org/3.12/library/stdtypes.html#numeric-types-int-float-complex). Попракитикуйтесь з простими змінними `str` та `int`, списками `list`, наборами `set` та словниками `dict`:
       ```python
       a = "змінна з текстом"
       b = 1 # числова Змінна
       b1 = 1.1 
       c = ["a", 1, 1.25, "Слово", a] # List
       d = {"a": "Слово", "b": 1, a: b} # Dict
       e = ("a", a) # Tuple
       f = {"ss", a + b} # Set
        ```
    1. Виведіть [вбудовані константи](https://docs.python.org/3.12/library/constants.html), (2-3 на вибір), та [зарезервовані слова Python](https://realpython.com/lessons/reserved-keywords/). Наприклад:
       ```python
       print("Перша константа: ", True)
       print(f"Як можна так робити вивід? {True}")
       import sys
       help("keywords")
       ```
    1. Виведіть результат роботи [вбудованих функцій](https://docs.python.org/3.12/library/functions.html#func-repr) (2-3 на вибір), наприклад:
       ```python
       print(abs(-12.5), f"є рівним {abs(12.5)}", "і якщо порівняти то: ", abs(-12.5) == abs(12.5))
       ``` 
    1. Познайомтесь з [циклами](https://docs.python.org/3.12/reference/compound_stmts.html#the-for-statement). Напишіть будь-який код який демонструє роботу циклів, (2-3 на вибір), наприклад:
        ```python
        letters = ["a", "b", "c"]
        for i in range(len(letters)):
            print(f"На позиції {i} знаходиться буква {letters[i]}")
        else:
            print("Ця конструкція безглузда!")
        ```
    1. Познайомтесь з [розгалуженнями](https://docs.python.org/3.12/reference/compound_stmts.html#the-if-statement). Напишіть будь-який код який демонструє роботу розгалужень, (2-3 на вибір), наприклад:
        ```python
        from random import randint
        A = randint(0, 1)
        print(f"Значить А={A}" if A else "Але може бути що А={}".format(A))
        ```
    1. Конструкція `try`->`except`->`finally`. У мові Python код не компілюється, а виконується відразу. Можливі помилки нам треба виловлювати самим. Напишіть свій варіант коду з помилкою. Наприклад:
        ```python
        A = 0
        try:
            print("Що буде якщо", 10/A, "?")
        except Exception as e:
            print("Невже це помилка > ", e)
        finally:
            print("О це так на тобі!")
        ```
    1. Контекст-менеджер `with`. Можете почитати [тут](https://python-scripts.com/contextlib). Напишіть свій код з контекст-менеджером, наприклад:
        ```python
        with open("README.md", "r") as f:
            for _, line in enumerate(f):
                print(f"{_})> ", line)
        ```
    1. Познайомтесь з Python [lambdas](https://docs.python.org/3.12/reference/expressions.html#lambda). Напишіть свій приклад коду та як Ви розумієте Лямбди, наприклад:
        ```python
        def a_b_func(a, b):
            return a, b

        this_is_lambda = lambda first, age: f'Цей код написав: {first}, Мені {age:10d} років'
        print("Це просто функція:", a_b_func, "\nА це лямбда:", this_is_lambda)
        print("Це її виклик:", this_is_lambda('Богдан', 1_00_000))
        print(this_is_lambda(*a_b_func("a", 1)))
        ```
1. :star: Запитайте у АІ як би він розписав про основи Python (задайте промпт вказавши що ви вивчаєте Python з використанням Jupyter Notebook). Спробуйте виконати приклади Python коду та вставте їх відповіді у звіт;

---
### Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію перейдіть у Веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;

---
