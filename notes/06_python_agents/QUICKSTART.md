# Швидкий старт - Google ADK

## Початок роботи
1. Отримайте API ключ на [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Встановіть залежності:
   ```bash
   cd notes/06_python_agents
   poetry install
   ```

## Створення першого агента
```bash
# Створення проекту агента
poetry run adk create my_first_agent

# Налаштування API ключа
echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > my_first_agent/.env

# Запуск агента через CLI
poetry run adk run my_first_agent

# Запуск веб-інтерфейсу (з батьківської папки)
poetry run adk web --port 8000
```

## Структура проекту
```
06_python_agents/
├── my_first_agent/      # Ваш перший агент
│   ├── agent.py         # Код агента з root_agent
│   ├── .env             # API ключі (НЕ комітити!)
│   └── __init__.py
├── README.md            # Повна лабораторна робота
├── QUICKSTART.md        # Цей файл
├── pyproject.toml       # Конфігурація Poetry
└── .env.example         # Приклад файлу зі змінними середовища
```

## Основні команди ADK
- `adk create <name>` - створити новий про ект агента
- `adk run <name>` - запустити агента через CLI
- `adk web --port 8000` - запустити веб-інтерфейс
- `adk --help` - показати допомогу

## Що далі?
Читайте повну лабораторну роботу у [README.md](README.md) для детальних інструкцій та завдань.

## Корисні посилання
- [Офіційна документація ADK](https://google.github.io/adk-docs/)
- [Python Quickstart](https://google.github.io/adk-docs/get-started/python/)

