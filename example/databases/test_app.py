import sqlite3

import pytest

from app import (
    add_student,
    average_mark_by_group,
    connect,
    delete_student,
    get_students,
    init_db,
    update_mark,
)


@pytest.fixture
def conn():
    connection = connect()
    init_db(connection)
    yield connection
    connection.close()


def test_add_and_get_student(conn):
    student_id = add_student(conn, "Марта", "Іванюк", "ІПЗ-21", 90)

    students = get_students(conn)

    assert len(students) == 1
    assert students[0]["id"] == student_id
    assert students[0]["firstname"] == "Марта"


def test_filter_by_group(conn):
    add_student(conn, "Марта", "Іванюк", "ІПЗ-21")
    add_student(conn, "Олег", "Петрук", "ІПЗ-22")

    assert [s["firstname"] for s in get_students(conn, "ІПЗ-22")] == ["Олег"]


def test_update_and_delete(conn):
    student_id = add_student(conn, "Марта", "Іванюк", "ІПЗ-21", 70)

    assert update_mark(conn, student_id, 85)
    assert get_students(conn)[0]["mark"] == 85
    assert delete_student(conn, student_id)
    assert get_students(conn) == []
    assert not delete_student(conn, student_id)


def test_mark_constraint(conn):
    with pytest.raises(sqlite3.IntegrityError):
        add_student(conn, "Марта", "Іванюк", "ІПЗ-21", 150)


def test_average_by_group(conn):
    add_student(conn, "А", "А", "ІПЗ-21", 80)
    add_student(conn, "Б", "Б", "ІПЗ-21", 90)
    add_student(conn, "В", "В", "ІПЗ-21")

    assert average_mark_by_group(conn) == {"ІПЗ-21": 85.0}


def test_sql_injection_is_harmless(conn):
    add_student(conn, "Марта", "Іванюк", "ІПЗ-21")

    assert get_students(conn, "x' OR '1'='1") == []
