"""Функції, залежні від зовнішнього світу: мережа та введення користувача."""


def fetch_status() -> dict:
    """Імітація виклику зовнішнього API. У тестах її підміняють (mock)."""
    raise ConnectionError("Немає доступу до зовнішньої системи")


def build_report() -> str:
    """Формує звіт зі статусу зовнішньої системи."""
    status = fetch_status()
    return f"Статус: {status['status']}, даних: {len(status['data'])}"


def ask_name() -> str:
    """Запитує ім'я та повертає його з великої літери."""
    return input("Введіть ім'я: ").strip().title()
