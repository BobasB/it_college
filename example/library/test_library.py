import pytest

from books import Book, BookStatus
from library import Library
from main import run_simulation
from stats import Statistics
from student import Student


@pytest.fixture
def library():
    lib = Library()
    lib.add_book(Book("Python", "Автор", 2024, "111"))
    lib.add_book(Book("ООП", "Автор", 2023, "222"))
    lib.register_student(Student("Марта"))
    return lib


def test_new_book_is_available():
    assert Book("Python", "Автор", 2024, "111").status == BookStatus.AVAILABLE


def test_student_ids_are_unique():
    assert Student("А").id != Student("Б").id


def test_lend_book_changes_status_and_shelf(library):
    book, student = library.books[0], library.students[0]

    assert library.lend_book(book, student, current_day=1)

    assert book.status == BookStatus.BORROWED
    assert book.taken_by == "Марта"
    assert book not in library.books_shelf
    assert book in student.borrowed_books


def test_cannot_lend_same_book_twice(library):
    book, student = library.books[0], library.students[0]
    library.lend_book(book, student)

    assert not library.lend_book(book, student)


def test_return_book_counts_reading_days(library):
    book, student = library.books[0], library.students[0]
    library.lend_book(book, student, current_day=3)

    assert library.return_book(book, student, current_day=10)

    assert student.book_reading_days[book] == 7
    assert book.status == BookStatus.AVAILABLE
    assert book in library.books_shelf


def test_return_book_that_student_does_not_have(library):
    assert not library.return_book(library.books[0], library.students[0])


def test_unregistered_student_cannot_borrow(library):
    assert not library.lend_book(library.books[0], Student("Гість"))


def test_favorite_books(library):
    student = library.students[0]
    book = library.books[0]
    for day in (1, 5):
        library.lend_book(book, student, day)
        library.return_book(book, student, day + 1)

    assert student.favorite_books == ["Python"]


def test_statistics_on_empty_library():
    stats = Statistics(Library())

    assert stats.get_total_books_borrowed() == 0
    assert stats.get_most_active_student() is None
    assert stats.get_most_popular_books() == []


def test_simulation_is_repeatable():
    first = Statistics(run_simulation(seed=7)).get_total_books_borrowed()
    second = Statistics(run_simulation(seed=7)).get_total_books_borrowed()

    assert first == second > 0
