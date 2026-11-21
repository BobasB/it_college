"""Симуляція роботи бібліотеки ІТ коледжу протягом 30 днів.

Запуск (з папки example/library): python main.py
"""
import random

from books import Book
from library import Library
from stats import Statistics
from student import Student

DAYS = 30
BOOK_TITLES = [
    "Вступ до Python",
    "Алгоритми та структури даних",
    "Об'єктно-орієнтоване програмування",
    "Бази даних",
    "Кобзар",
    "Лісова пісня",
]


def run_simulation(days: int = DAYS, seed: int = 1) -> Library:
    # Фіксований seed робить симуляцію повторюваною, а отже придатною для тестів
    rng = random.Random(seed)
    library = Library()
    for number, title in enumerate(BOOK_TITLES, start=1):
        library.add_book(Book(title, "Різні автори", 2020 + number, f"978-0-00-{number:06d}-0"))
    for name in ["Богдан", "Марта", "Олег"]:
        library.register_student(Student(name))

    for day in range(1, days + 1):
        for student in library.students:
            # Студент або повертає одну з книг, або береться за нову
            if student.borrowed_books and rng.random() < 0.4:
                library.return_book(rng.choice(student.borrowed_books), student, day)
            elif library.list_available_books and rng.random() < 0.5:
                library.lend_book(rng.choice(library.list_available_books), student, day)
    return library


if __name__ == "__main__":
    result = run_simulation()
    Statistics(result, DAYS).print_full_statistics()
