# Швидкий старт

## Початок роботи
1. Отримайте API ключ на [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Скопіюйте `.env.example` у `.env` та вставте ваш API ключ
3. Встановіть залежності:
   ```bash
   cd notes/06_python_agents
   poetry install
   ```

## Запуск простого агента
```bash
poetry run python simple_agent.py
```

## Структура проекту
```
06_python_agents/
├── README.md           # Повна лабораторна робота
├── QUICKSTART.md       # Цей файл
├── pyproject.toml      # Конфігурація Poetry
├── .env.example        # Приклад файлу зі змінними середовища
├── .env               # Ваші API ключі (НЕ комітити!)
└── simple_agent.py    # Приклад простого агента
```

## Що далі?
Читайте повну лабораторну роботу у [README.md](README.md) для детальних інструкцій та завдань.
