"""Книги бібліотеки та їх статуси."""
from enum import Enum


class BookStatus(Enum):
    """Можливі статуси книги."""

    AVAILABLE = "в наявності"
    BORROWED = "взята"
    RESERVED = "зарезервована"


class Book:
    """Книга: назва, автор, рік, ISBN, статус та ім'я студента, який її взяв."""

    def __init__(self, title: str, author: str, year: int, isbn: str) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.status = BookStatus.AVAILABLE
        self.taken_by: str | None = None

    def __str__(self) -> str:
        return f"'{self.title}' ({self.author}, {self.year}) - {self.status.value}"

    @property
    def description(self) -> str:
        return (
            f"Назва: {self.title}. Автор: {self.author}. "
            f"Видання: {self.year}, ISBN: {self.isbn}. Статус: {self.status.value}."
        )

    @property
    def info(self) -> str:
        who = f"взята студентом {self.taken_by}" if self.taken_by else "доступна для позики"
        return f"Книга '{self.title}' зараз {self.status.value} та {who}."
