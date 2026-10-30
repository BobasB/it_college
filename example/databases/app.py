"""Навчальний приклад роботи з SQLite: CRUD для таблиці студентів."""
import sqlite3
from pathlib import Path


def connect(db_path: str | Path = ":memory:") -> sqlite3.Connection:
    """Створює підключення та вмикає доступ до колонок за іменем."""
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            grp TEXT NOT NULL,
            mark INTEGER CHECK (mark BETWEEN 0 AND 100)
        )
        """
    )
    connection.commit()


def add_student(connection: sqlite3.Connection, firstname: str, lastname: str, grp: str, mark: int | None = None) -> int:
    # Плейсхолдери ? захищають від SQL-ін'єкцій, на відміну від f-рядків
    cursor = connection.execute(
        "INSERT INTO students (firstname, lastname, grp, mark) VALUES (?, ?, ?, ?)",
        (firstname, lastname, grp, mark),
    )
    connection.commit()
    return cursor.lastrowid


def get_students(connection: sqlite3.Connection, grp: str | None = None) -> list[sqlite3.Row]:
    if grp is None:
        return connection.execute("SELECT * FROM students ORDER BY lastname, firstname").fetchall()
    return connection.execute(
        "SELECT * FROM students WHERE grp = ? ORDER BY lastname, firstname", (grp,)
    ).fetchall()


def update_mark(connection: sqlite3.Connection, student_id: int, mark: int) -> bool:
    cursor = connection.execute("UPDATE students SET mark = ? WHERE id = ?", (mark, student_id))
    connection.commit()
    return cursor.rowcount == 1


def delete_student(connection: sqlite3.Connection, student_id: int) -> bool:
    cursor = connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    return cursor.rowcount == 1


def average_mark_by_group(connection: sqlite3.Connection) -> dict[str, float]:
    rows = connection.execute(
        "SELECT grp, AVG(mark) AS average FROM students WHERE mark IS NOT NULL GROUP BY grp"
    ).fetchall()
    return {row["grp"]: round(row["average"], 2) for row in rows}


if __name__ == "__main__":
    conn = connect("students.db")
    init_db(conn)
    add_student(conn, "Богдан", "Бугіль", "ІПЗ-21", 95)
    for student in get_students(conn):
        print(dict(student))
    conn.close()
