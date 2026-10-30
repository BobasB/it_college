# Робота з базами даних
> База даних — це сукупність організованих/структурованих даних відповідно до концепції, яка описує характеристику цих даних і взаємозв'язки між їх елементами. У цій роботі використовується `SQLite` — база в одному файлі, що вбудована в стандартну бібліотеку Python (`sqlite3`), тож встановлювати нічого не потрібно.

## Мета роботи
Навчитись створювати базу SQLite з Python, описувати таблиці мовою SQL, виконувати CRUD-операції (створення, читання, оновлення, видалення), безпечно передавати параметри в запити та покривати код тестами.

## Що потрібно знати / підготувати
- виконані роботи про [Python](../04_python_basics/README.md) та [тестування](../07_testing/README.md) (бажано частини 1-2);
- робочий приклад: [example/databases](../../example/databases) — `app.py` та `test_app.py`;
- за бажанням — розширення VS Code `SQLite Viewer` для перегляду файлу `.db`;

---
## Теоретичні відомості
| Термін | Пояснення |
| --- | --- |
| Таблиця | набір рядків (записів) з однаковими колонками |
| Первинний ключ (`PRIMARY KEY`) | унікальний ідентифікатор запису |
| Зовнішній ключ (`FOREIGN KEY`) | посилання на запис в іншій таблиці |
| CRUD | Create / Read / Update / Delete — `INSERT` / `SELECT` / `UPDATE` / `DELETE` |
| Транзакція | група операцій, що виконується повністю або не виконується зовсім (`commit` / `rollback`) |

Python є лише інструментом доступу до бази, всі операції виконуються через мову запитів SQL ([SQL Wiki](https://uk.wikipedia.org/wiki/SQL), [документація sqlite3](https://docs.python.org/3/library/sqlite3.html)).

---
## Хід роботи

### 1. Підключення та створення таблиці
1. Створіть у папці роботи файл `db_basics.py` (або ноутбук) та виконайте:
    ```python
    import sqlite3

    # Створює файл my_database.db, якщо його немає, або підключається до існуючого
    conn = sqlite3.connect("my_database.db")
    c = conn.cursor()

    c.execute(
        "CREATE TABLE IF NOT EXISTS students ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "firstname TEXT NOT NULL, "
        "lastname TEXT NOT NULL)"
    )
    conn.commit()

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())
    conn.close()
    ```
1. :star: Вкажіть у звіті результат виконання (список таблиць; службова таблиця `sqlite_sequence` з'являється через `AUTOINCREMENT` — це нормально).

> [!WARNING]
> Файл `my_database.db` — результат запуску програми. Додайте `*.db` до `.gitignore` та не комітьте його.

### 2. Додавання та читання даних
1. Додайте записи та прочитайте їх. **Завжди** передавайте значення через плейсхолдери `?`, а не через f-рядки:
    ```python
    import sqlite3

    conn = sqlite3.connect("my_database.db")
    c = conn.cursor()

    students = [("Богдан", "Бугіль"), ("Марта", "Іванюк")]
    c.executemany("INSERT INTO students (firstname, lastname) VALUES (?, ?)", students)
    conn.commit()

    for row in c.execute("SELECT id, firstname, lastname FROM students ORDER BY lastname"):
        print(row)
    conn.close()
    ```
1. :star: Вкажіть у звіті вивід програми. Запустіть її двічі та поясніть, чому записи дублюються (що було б, якби `firstname` та `lastname` були унікальними — `UNIQUE (firstname, lastname)`?).

### 3. Оновлення та видалення
1. Виконайте запити:
    ```sql
    UPDATE students SET lastname = ? WHERE id = ?
    DELETE FROM students WHERE id = ?
    ```
    Перед цими запитами знову відкрийте `conn = sqlite3.connect("my_database.db")` та створіть `c = conn.cursor()` (попередній блок закрив з'єднання). Передавайте параметри кортежем, наприклад `c.execute("DELETE FROM students WHERE id = ?", (1,))`, і збережіть зміни через `conn.commit()`. Залиште з'єднання відкритим для кроку 4 та закрийте його через `conn.close()` після завершення цього кроку;
1. Перевірте `c.rowcount` після `UPDATE`/`DELETE` — скільки рядків змінено;
1. :star: Покажіть у звіті таблицю до та після змін.

### 4. Безпека: SQL-ін'єкції
1. Порівняйте два способи (виконайте на тестовій базі!):
    ```python
    user_input = "x' OR '1'='1"
    # НЕБЕЗПЕЧНО: значення вставляється прямо в текст запиту
    c.execute(f"SELECT * FROM students WHERE lastname = '{user_input}'")
    print(c.fetchall())
    # БЕЗПЕЧНО: значення передається окремо
    c.execute("SELECT * FROM students WHERE lastname = ?", (user_input,))
    print(c.fetchall())
    ```
1. :star: Поясніть у звіті, чому перший запит повертає всі записи, а другий — жодного.

### 5. Робочий приклад: `example/databases`
1. Ознайомтесь з [app.py](../../example/databases/app.py): функції `add_student`, `get_students`, `update_mark`, `delete_student`, `average_mark_by_group`;
1. Запустіть тести:
    ```bash
    cd example/databases
    python -m pytest -v
    ```
1. Зверніть увагу: тести використовують базу в пам'яті (`":memory:"`) та fixture із `yield`, тож вони не змінюють реальні дані.
1. :star: Додайте до проєкту:
    - колонку `email` та тест, що перевіряє її збереження;
    - функцію `find_by_lastname(connection, lastname)` та два тести (знайдено / не знайдено);
    - функцію `top_students(connection, limit=3)` (`ORDER BY mark DESC LIMIT ?`) та тест.

### 6. Зв'язані таблиці (додатково)
1. :fire: Створіть таблицю `groups (id, name)` та змініть `students` так, щоб вона посилалась на групу через `group_id INTEGER REFERENCES groups(id)`. Увімкніть перевірку зовнішніх ключів: `conn.execute("PRAGMA foreign_keys = ON")`.
1. :fire: Напишіть запит `JOIN`, що виводить прізвище студента та назву групи, і тест до нього.
1. :fire: Експортуйте результат запиту в CSV за допомогою модуля `csv`.

---
## Що має бути у звіті
- код і результат кроків 1-4 (скріншоти або текст виводу);
- відповіді на питання про дублікати та SQL-ін'єкції;
- результат `pytest -v` для `example/databases` та код доданих вами функцій і тестів;
- висновок за [шаблоном](../../reports/README.md).

## Критерії оцінювання
| Рівень | Що потрібно виконати |
| --- | --- |
| Достатній | кроки 1-3, результати у звіті |
| Високий | + крок 4 та крок 5 (доповнення проєкту з тестами) |
| Відмінний | + крок 6 (:fire:), коректні обмеження (`CHECK`, `UNIQUE`, `FOREIGN KEY`) |

## Контрольні питання
1. Чим SQLite відрізняється від серверних СУБД (PostgreSQL, MySQL)?
1. Для чого потрібен `commit()` і що станеться без нього?
1. Що таке SQL-ін'єкція і як від неї захищатись?
1. Що означає `PRIMARY KEY`, `NOT NULL`, `CHECK`?
1. Чому в тестах краще використовувати `:memory:`?

---
## Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію (без `*.db`), скопіюйте URL папки з роботою у браузері;
- :star: надішліть URL як відповідь на завдання у Google Classroom;
- :star: після перевірки викладачем оцінка з'явиться у Google Classroom.

---
