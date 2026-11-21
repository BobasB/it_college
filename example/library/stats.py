"""Статистика використання бібліотеки."""
from collections import Counter

from library import Library
from student import Student


class Statistics:
    def __init__(self, library: Library, simulation_days: int = 90) -> None:
        self.library = library
        self.simulation_days = simulation_days

    def get_total_books_borrowed(self) -> int:
        return sum(student.total_books_taken for student in self.library.students)

    def get_most_active_student(self) -> Student | None:
        if not self.library.students:
            return None
        return max(self.library.students, key=lambda student: student.total_books_taken)

    def get_most_popular_books(self) -> list[str]:
        """Назви книг, які брали найчастіше серед усіх студентів."""
        counter = Counter(
            book.title for student in self.library.students for book in student.books_taken_history
        )
        if not counter:
            return []
        top = max(counter.values())
        return [title for title, amount in counter.items() if amount == top]

    def print_student_statistics(self, student: Student) -> None:
        print(student.student_id_card)
        print(f"Взято книг: {student.total_books_taken}")
        print(f"Зараз на руках: {[book.title for book in student.borrowed_books]}")
        print(f"Улюблені книги: {student.favorite_books}")
        for book, days in student.book_reading_days.items():
            print(f"  '{book.title}' читав {days} дн.")

    def print_full_statistics(self) -> None:
        print(f"\n=== Статистика за {self.simulation_days} днів ===")
        print(f"Усього видач: {self.get_total_books_borrowed()}")
        print(f"На полиці зараз: {len(self.library.books_shelf)} з {len(self.library.books)} книг")
        active = self.get_most_active_student()
        if active:
            print(f"Найактивніший студент: {active.name} ({active.total_books_taken} книг)")
        print(f"Найпопулярніші книги: {self.get_most_popular_books()}")
        for student in self.library.students:
            print()
            self.print_student_statistics(student)
