"""Студент бібліотеки."""
from collections import Counter
from itertools import count

from books import Book, BookStatus


class Student:
    """Студент, який бере та повертає книги."""

    # Змінна класу: єдиний лічильник для всіх студентів, тому ID унікальні й передбачувані
    _next_id = count(1)

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = next(Student._next_id)
        self.college_name = "ІТ коледж"
        self.borrowed_books: list[Book] = []
        self.books_taken_history: list[Book] = []
        self.book_reading_days: dict[Book, int] = {}
        self._borrow_dates: dict[Book, int] = {}

    def __str__(self) -> str:
        return f"Студент {self.name} (ID {self.id})"

    @property
    def student_id_card(self) -> str:
        return f"Студент коледжу <<{self.college_name}>>\nІм'я: {self.name},\nID: {self.id}"

    @property
    def total_books_taken(self) -> int:
        return len(self.books_taken_history)

    @property
    def favorite_books(self) -> list[str]:
        """Назви книг, які студент брав найчастіше."""
        counter = Counter(book.title for book in self.books_taken_history)
        if not counter:
            return []
        top = max(counter.values())
        return [title for title, amount in counter.items() if amount == top]

    def borrow_book(self, book: Book, current_day: int | None = None) -> bool:
        """Бере книгу, якщо вона в наявності. Повертає True у разі успіху."""
        if book.status != BookStatus.AVAILABLE:
            return False
        book.status = BookStatus.BORROWED
        book.taken_by = self.name
        self.borrowed_books.append(book)
        self.books_taken_history.append(book)
        if current_day is not None:
            self._borrow_dates[book] = current_day
        return True

    def return_book(self, book: Book, current_day: int | None = None) -> bool:
        """Повертає книгу. Якщо відомий день, зберігає кількість днів читання."""
        if book not in self.borrowed_books:
            return False
        book.status = BookStatus.AVAILABLE
        book.taken_by = None
        self.borrowed_books.remove(book)
        if current_day is not None and book in self._borrow_dates:
            self.book_reading_days[book] = current_day - self._borrow_dates.pop(book)
        return True
