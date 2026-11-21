"""Бібліотека: каталог книг, полиця та зареєстровані студенти."""
from books import Book, BookStatus
from student import Student


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []  # повний каталог
        self.books_shelf: list[Book] = []  # книги, які зараз на полиці
        self.students: list[Student] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        self.books_shelf.append(book)

    def register_student(self, student: Student) -> None:
        self.students.append(student)

    @property
    def list_available_books(self) -> list[Book]:
        return [book for book in self.books_shelf if book.status == BookStatus.AVAILABLE]

    def lend_book(self, book: Book, student: Student, current_day: int | None = None) -> bool:
        """Видає книгу студенту, якщо вона на полиці та студент зареєстрований."""
        if book not in self.books_shelf or student not in self.students:
            return False
        if not student.borrow_book(book, current_day):
            return False
        self.books_shelf.remove(book)
        return True

    def return_book(self, book: Book, student: Student, current_day: int | None = None) -> bool:
        """Приймає книгу від студента та повертає її на полицю."""
        if not student.return_book(book, current_day):
            return False
        self.books_shelf.append(book)
        return True
