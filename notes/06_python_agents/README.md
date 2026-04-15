# AI Агенти з Google ADK
> AI агенти - це автономні програмні системи, здатні сприймати своє середовище, приймати рішення та виконувати дії для досягнення певних цілей. Google Agent Development Kit (ADK) - це набір інструментів для створення інтелектуальних агентів на основі великих мовних моделей.

## Мета роботи: __Навчитись створювати AI агентів з використанням Google ADK (Python) та Poetry для управління залежностями проекту__

---
### Підготовка робочого середовища
1. Для роботи з AI агентами нам потрібен ключ API від Google. Перейдіть на [Google AI Studio](https://aistudio.google.com/app/apikey) та створіть новий API ключ. Використовуйте власний Google акаунт для цього (`@gmail.com`). Даний акаунт дозволить користуватись безкоштовними квотами для розробки та тестування агентів.
   
2. :star: Збережіть отриманий API ключ у безпечному місці. Він знадобиться для роботи з агентами.

3. :fire: **ВАЖЛИВО**: Ніколи не комітьте API ключі в Git репозиторій! Для їх зберігання використовуйте файл `.env` та додайте його до `.gitignore`.

4. У цьому проекті застосовується [Poetry](https://python-poetry.org/) - сучасний інструмент для управління залежностями та пакетами Python. Poetry вже має бути встановлений у вашій системі після виконання роботи про віртуальні середовища.

5. Перевірте чи Python 3.13+ та Poetry встановлені:
    ```bash
    python --version
    poetry --version
    ```

6. :star: Вкажіть у звіті версію Poetry та Python яка встановлена у вашій системі.

---
### Встановлення Google ADK
1. Перейдіть до папки лабораторної роботи та встановіть залежності:
   ```bash
   cd notes/06_python_agents
   poetry init
   poetry add google-adk python-dotenv
   ```
    1. Через вимого `google-adk` додайте у pyproject.toml наступні рядки для сумісності з Python 3.13:
    ```toml
    requires-python = ">=3.13,<4.0.0"
    ```
2. :star: Переконайтесь що створився файл `poetry.lock`. Поясніть у звіті для чого потрібен цей файл.

3. Перевірте що ADK встановлено коректно:
   ```bash
   poetry run adk --version
   ```

4. :star: Вкажіть у звіті версію ADK яка встановлена.

5. Подивіться які команди доступні в ADK:
   ```bash
   poetry run adk --help
   ```

6. :star: Вкажіть у звіті основні команди ADK (create, run, web).

---
### Створення першого проекту з агентом
1. ADK надає команду `adk create` для автоматичного створення структури проекту. Створимо наш перший проект агента:
   ```bash
   poetry run adk create my_first_agent
   ```
   - тут у інтерактивному режимі пройдіть всі кроки для ініціалізації Агента.

> [!WARNING]
> Не комітьте API ключі в Git репозиторій! Додайте файл `.env` до `.gitignore`.

2. :star: Перегляньте структуру створеного проекту:
   ```bash
   ls -la my_first_agent/
   ```
   
   Ви побачите наступну структуру:
   ```
   my_first_agent/
       agent.py      # основний код агента
       .env          # API ключі
       __init__.py   # ініціалізація модуля
   ```

3. Відкрийте файл `my_first_agent/agent.py` та перегляньте згенерований код. За замовчуванням ADK створює базовий шаблон агента.
4. Для агента можна використовувати різні моделі. За замовчуванням використовується `gemini-2.5-flash`, але ви можете змінити її на інші:
    - `gemini-2.5-flash` - збалансована модель для більшості завдань
    - `gemini-2.5-flash-lite` - легка модель для швидких відповідей та тестування
    - `gemini-3.1-flash-lite-preview` - легка модель для швидких відповідей та тестування
    - `gemini-3-flash-preview` - потужна модель для складних завдань (може бути недоступною)

---
### Створення простого агента з інструментом
1. Тепер оновимо код агента щоб він міг використовувати інструменти (tools). Відкрийте файл `my_first_agent/agent.py` та замініть його вміст на наступний код:
   ```python
   from google.adk.agents.llm_agent import Agent
   
   # Визначаємо функцію-інструмент
   def get_current_time(city: str) -> dict:
       """
       Повертає поточний час у вказаному місті.
       
       Args:
           city: назва міста
       
       Returns:
           dict: інформація про час у вказаному місті
       """
       # Це mock-реалізація для демонстрації
       import datetime
       current_time = datetime.datetime.now().strftime("%H:%M:%S")
       return {
           "status": "success",
           "city": city,
           "time": current_time
       }
   
   # Створюємо агента
   root_agent = Agent(
       model='gemini-2.5-flash',
       name='time_agent',
       description="Повідомляє поточний час у вказаному місті.",
       instruction="Ти корисний асистент, який повідомляє поточний час у містах. Використовуй функцію 'get_current_time' для цього. Відповідай українською мовою та використовуй подачу дати/часу у форматі HH:MM:SS.",
       tools=[get_current_time],
   )
   ```

2. :star: Збережіть файл та поясніть у звіті що робить кожна частина коду:
   - Що таке `Agent` клас?
   - Для чого потрібен параметр `tools`?
   - Що робить функція `get_current_time`?

---
### Запуск агента через командний рядок
1. Запустіть агента використовуючи команду `adk run`:
   ```bash
   poetry run adk run my_first_agent
   ```

2. :star: У інтерактивному режимі поставте агенту запитання:
   ```
   Який зараз час у Львові?
   ```

3. :star: Зробіть скріншот або скопіюйте діалог з агентом у звіт. Агент повинен викликати функцію `get_current_time` та повернути результат.

4. :star: Поставте агенту ще 2-3 запитання про час у різних містах. Додайте результати у звіт.

5. Вийдіть з агента натиснувши `Ctrl+C` або ввівши `exit`.

---
### Запуск агента через веб-інтерфейс
1. ADK надає зручний веб-інтерфейс для тестування агентів. Запустіть веб-сервер:
   ```bash
   poetry run adk web --port 8000
   ```

2. :fire: **ВАЖЛИВО**: Команду `adk web` потрібно запускати з батьківської папки, яка містить папку вашого агента, тобто кореневої папки де міститься файл `pyproject.toml`.

3. :star: Відкрийте браузер та перейдіть на адресу [http://localhost:8000](http://localhost:8000).

4. :star: Виберіть агента `my_first_agent` у верхньому лівому кутку інтерфейсу.

5. :star: Протестуйте агента через веб-інтерфейс, поставивши йому кілька запитань. Зробіть скріншот веб-інтерфейсу та додайте до звіту.

6. :fire: **ЗАУВАЖТЕ**: ADK Web призначено лише для розробки та налагодження. Не використовуйте його у production середовищі.

---
### Створення агента з математичними інструментами  
1. Створіть проект агента та налаштуйте API ключ:
   ```bash
   poetry run adk create math_agent
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > math_agent/.env
   ```

2. Відкрийте `math_agent/agent.py` та замініть код на наступний:
   ```python
   from google.adk.agents.llm_agent import Agent
   
   def calculate_rectangle_area(width: float, height: float) -> float:
       """
       Обчислює площу прямокутника.
       
       Args:
           width: ширина прямокутника
           height: висота прямокутника
       
       Returns:
           float: площа прямокутника
       """
       return width * height
   
   def calculate_circle_area(radius: float) -> float:
       """
       Обчислює площу кола.
       
       Args:
           radius: радіус кола
       
       Returns:
           float: площа кола
       """
       import math
       return math.pi * radius ** 2
   
   def calculate_cube_volume(side: float) -> float:
       """
       Обчислює об'єм куба.
       
       Args:
           side: довжина ребра куба
       
       Returns:
           float: об'єм куба
       """
       return side ** 3
   
   # Створюємо математичного агента
   root_agent = Agent(
       model='gemini-2.5-flash',
       name='math_agent',
       description="Виконує математичні обчислення геометричних фігур.",
       instruction="""
       Ти експертний математичний асистент який допомагає з обчисленнями.
       У тебе є інструменти для обчислення площі прямокутника, площі кола та об'єму куба.
       Використовуй ці інструменти коли потрібно виконати розрахунки.
       Відповідай українською мовою та поясни хід обчислень.
       """,
       tools=[calculate_rectangle_area, calculate_circle_area, calculate_cube_volume],
   )
   ```

4. :star: Запустіть математичного агента:
   ```bash
   poetry run adk web --port 8000
   ```

5. :star: Протестуйте агента з наступними запитаннями та додайте результати у звіт:
   - "Обчисли площу прямокутника зі сторонами 5 та 10"
   - "Яка площа кола з радіусом 7?"
   - "Який об'єм куба з ребром 3?"

6. :star: Додайте до агента ще один математичний інструмент на ваш вибір (наприклад, обчислення об'єму циліндра, площі трикутника, або периметру). Протестуйте новий інструмент.

---
### Створення агента-помічника для студентів
1. Створіть проект агента та налаштуйте API ключ:
   ```bash
   poetry run adk create student_helper
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > student_helper/.env
   ```

2. Відкрийте `student_helper/agent.py` та створіть агента з кастомною інструкцією:
   ```python
   from google.adk.agents.llm_agent import Agent
   
   def explain_concept(concept: str, level: str = "beginner") -> dict:
       """
       Пояснює концепцію програмування.
       
       Args:
           concept: назва концепції для пояснення
           level: рівень складності (beginner, intermediate, advanced)
       
       Returns:
           dict: пояснення та приклади
       """
       explanations = {
           "beginner": f"Базове пояснення концепції {concept}",
           "intermediate": f"Поглиблене пояснення концепції {concept}",
           "advanced": f"Експертне пояснення концепції {concept}"
       }
       return {
            "status": "success",
            "concept": concept,
            "level": level,
            "explanation": explanations.get(level, "Невідомий рівень")
       }
   
   def check_syntax(code: str, language: str = "python") -> dict:
       """
       Перевіряє синтаксис коду (базова перевірка).
       
       Args:
           code: код для перевірки
           language: мова програмування
       
       Returns:
           dict: результат перевірки
       """
       # Проста перевірка для демонстрації
       if not code.strip():
           return {"status": "error", "message": "Код порожній"}
       return {"status": "success", "message": "Синтаксис виглядає коректно", "language": language}
   
   root_agent = Agent(
       model='gemini-2.5-flash',
       name='student_helper',
       description="Помічник для студентів які вивчають програмування.",
       instruction="""
       Ти досвідчений викладач з ООП програмування який допомагає студентам.
       
       Твої обов'язки:
       - Пояснювати складні концепції простими словами
       - Наводити приклади коду
       - Перевіряти синтаксис коду
       - Давати поради щодо best practices
       - Бути терплячим та підтримуючим
       - За замовчуванням використовувати Python для прикладів, якщо не вказано іншу мову
       
       Завжди відповідай українською мовою.
       Використовуй форматування Markdown для коду.
       """,
       tools=[explain_concept, check_syntax],
   )
   ```

4. :star: Запустіть агента та поставте йому запитання про Python:
   ```bash
   poetry run adk run student_helper
   ```

5. :star: Протестуйте агента з наступними запитаннями:
   - "Поясни що таке декоратори в Python"
   - "Як працює list comprehension?"
   - "Перевір синтаксис: print('Hello World')"

6. :star: Додайте результати діалогу у звіт.

---
### Робота з конфігурацією агента
1. Створіть проект агента та налаштуйте API ключ:
   ```bash
   poetry run adk create creative_writer
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > creative_writer/.env
   ```

2. Відкрийте `creative_writer/agent.py` та створіть агента з налаштуваннями для креативного письма:
   ```python
   from google.adk.agents.llm_agent import Agent
   from google.genai.types import GenerateContentConfig
   
   def generate_story_prompt(theme: str, characters: int = 2) -> str:
       """
       Генерує промпт для історії.
       
       Args:
           theme: тема історії
           characters: кількість персонажів
       
       Returns:
           str: промпт для генерації історії
       """
       return f"Створи цікаву історію на тему '{theme}' з {characters} персонажами."
   
   root_agent = Agent(
       model='gemini-2.5-flash',
       name='creative_writer',
       description="Креативний письменник історій.",
       instruction="""
       Ти талановитий письменник який створює захоплюючі історії.
       Твої історії мають бути:
       - Цікавими та захоплюючими
       - З несподіваними поворотами сюжету
       - З яскравими персонажами
       - Написаними українською мовою
       
       Використовуй багатий словниковий запас та літературні прийоми.
       """,
       tools=[generate_story_prompt],
       # Налаштування для більш креативних відповідей
       config=GenerateContentConfig(
           temperature=1.5,  # Висока температура для креативності
           top_k=40,
           top_p=0.95,
       )
   )
   ```

4. :star: Запустіть агента та попросіть його написати коротку історію:
   ```bash
   poetry run adk run creative_writer
   ```

5. :star: Протестуйте різні промпти:
   - "Напиши коротку історію про подорож у космосі"
   - "Створи казку про дружбу між роботом та людиною"

---
### Пояснення параметрів моделі
1. **temperature** (0.0 - 2.0):
> Параметр temperature контролює рівень креативності та випадковості у відповідях агента. Нижче наведено рекомендації щодо вибору значення temperature для різних типів завдань:
   - 0.0-0.3: Детерміністичні, точні відповіді (для фактів, розрахунків)
   - 0.4-0.7: Збалансовані відповіді (універсальне використання)
   - 0.8-1.5: Креативні відповіді (для історій, генерації ідей)
   - 1.6-2.0: Дуже креативні, непередбачувані відповіді

2. **top_k** (1-40):
> Параметр top_k обмежує кількість найімовірніших токенів для вибору.
   - Менше значення = більш фокусовані відповіді
   - Більше значення = більш різноманітні відповіді

3. **top_p** (0.0-1.0):
> Параметр top_p контролює вибір токенів на основі їх кумулятивної ймовірності. 
   - 0.9-0.95: збалансований вибір
   - Нижче 0.9: більш консервативні відповіді
   - Вище 0.95: більш різноманітні відповіді

4. :star: Створіть 3 агенти з різними налаштуваннями:
   - Агент-експерт (temperature=0.1)
   - Агент-асистент (temperature=0.7)
   - Агент-письменник (temperature=1.3)
   
   Поставте їм однакове запитання та порівняйте відповіді. Додайте результати у звіт.

---
### Створення агента з пам'яттю (збереження контексту)
1. Створіть проект агента та налаштуйте API ключ:
   ```bash
   poetry run adk create conversation_agent
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > conversation_agent/.env
   ```

2. Створіть простого розмовного агента у `conversation_agent/agent.py`:
    ```python
    from google.adk.agents.llm_agent import Agent
    from google.adk.tools.tool_context import ToolContext

    def save_user_preference(tool_context: ToolContext, preference_type: str, value: str) -> dict:
        """
        Зберігає вподобання користувача.

        Args:
            preference_type: тип вподобання (улюблений_колір, хобі, тощо)
            value: значення вподобання

        Returns:
            dict: підтвердження збереження
        """
        existing_state = tool_context.state.get(preference_type, [])
        tool_context.state[preference_type] = existing_state + [value]
        print(f"[Added to {preference_type}] {value}")
        return {
            "status": "success",
            "message": f"Збережено: {preference_type} = {value}"
        }

    def recall_preference(tool_context: ToolContext, preference_type: str) -> dict:
        """
        Згадує вподобання користувача.

        Args:
            preference_type: тип вподобання для пошуку

        Returns:
            dict: збережене вподобання або повідомлення про відсутність
        """
        # Примітка: історія зберігається автоматично в ADK
        preferences = tool_context.state.get(preference_type, [])
        if preferences:
            return {
                "status": "success",
                "message": f"Згадано: {preference_type} = {', '.join(preferences)}"
            }
        else:
            return {
                "status": "error",
                "message": f"Не знайдено вподобань типу: {preference_type}"
            }

    root_agent = Agent(
        model='gemini-2.5-flash',
        name='conversation_agent',
        description="Розмовний агент який памʼятає користувача.",
        instruction="""
        Ти дружелюбний асистент який веде розмову з користувачем.

        Важливо:
        - Памʼятай що користувач розповідає про себе та зберігай цю інформацію як вподобання за допомогою інструменту save_user_preference
        - Використовуй цю інформацію у подальшій розмові використовуючи інструмент recall_preference
        - Стався уважно до деталей, які користувач розповідає про себе, це допоможе тобі краще його розуміти та підтримувати цікаву розмову
        - Будь ввічливим та цікавим співрозмовником
        - Звертайся до користувача по імені, якщо він його назве, та намагайся запамʼятати його інтереси та вподобання для подальшого використання у розмові

        Відповідай українською мовою.
        """,
        tools=[save_user_preference, recall_preference],
    )

    ```

4. :star: Запустіть агента та проведіть розмову:
   ```bash
   poetry run adk web --port 8000
   ```

5. :star: Проведіть діалог де ви:
   - Представитеся агенту (назвіть своє імʼя)
   - Розкажіть про своє хобі
   - Згадайте улюблений колір
   - Потім запитайте "Як мене звати?" та "Яке моє хобі?"

6. :star: Агент повинен памʼятати контекст розмови. Додайте скріншот або текст діалогу у звіт.

---
### Налагодження та тестування агентів
1. ADK надає зручні інструменти для налагодження. Використовуйте verbose режим для детальної інформації:
   ```bash
   poetry run adk run my_first_agent --verbose
   ```

2. :star: Запустіть агента у verbose режимі щоб почала виводиться додаткова інформація. Вкажіть у звіті яку додаткову інформацію ви побачили.

3. Для логування можна використовувати вбудовані можливості Python. Додайте логування до вашого агента:
   ```python
   import logging
   from google.adk.agents.llm_agent import Agent
   
   # Налаштування логування
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   
   def logging_tool(param: str) -> dict:
       """Інструмент з логуванням подій"""
       logger.info(f"Виклик інструменту logging_tool з параметром: {param}")
       return {"result": "success", "processed_param": param}
   
   root_agent = Agent(
       model='gemini-2.5-flash',
       name='logging_agent',
       description="Агент з логуванням.",
       instruction="Використовуй інструмент logging_tool та логуй всі дії.",
       tools=[logging_tool],
   )
   ```

4. :star: Додайте логування до одного з ваших агентів та протестуйте. Вставте приклад логів у звіт.

---
### Робота зі структурою проекту
1. Рекомендована структура проекту з агентами:
   ```
   notes/06_python_agents/
   ├── my_first_agent/
   │   ├── agent.py
   │   ├── .env
   │   └── __init__.py
   ├── math_agent/
   │   ├── agent.py
   │   ├── .env
   │   └── __init__.py
   ├── student_helper/
   │   ├── agent.py
   │   ├── .env
   │   └── __init__.py
   ├── tools/
   │   ├── __init__.py
   │   └── common_tools.py
   ├── pyproject.toml
   ├── poetry.lock
   └── README.md
   ```

2. :star: Створіть мінімум 3 різних агенти у окремих папках. Додайте скріншот структури папок у звіт.

3. Для організації спільних інструментів створіть папку `tools/`:
   ```bash
   mkdir tools
   touch tools/__init__.py
   touch tools/common_tools.py
   ```

4. У файлі `tools/common_tools.py` можна зберігати спільні інструменти:
   ```python
   """Спільні інструменти для всіх агентів"""
   
   def format_text(text: str, style: str = "uppercase") -> str:
       """
       Форматує текст за вказаним стилем.
       
       Args:
           text: текст для форматування
           style: стиль (uppercase, lowercase, title)
       
       Returns:
           str: відформатований текст
       """
       if style == "uppercase":
           return text.upper()
       elif style == "lowercase":
           return text.lower()
       elif style == "title":
           return text.title()
       return text
   
   def count_words(text: str) -> dict:
       """
       Підраховує кількість слів у тексті.
       
       Args:
           text: текст для аналізу
       
       Returns:
           dict: статистика по тексту
       """
       words = text.split()
       return {
           "total_words": len(words),
           "total_chars": len(text),
           "unique_words": len(set(words))
       }
   ```

5. :star: Створіть файл зі спільними інструментами та використайте їх у декількох агентах. Імпортуйте інструменти так:
   ```python
   from tools.common_tools import format_text, count_words
   ```

---
### Поради щодо створення ефективних агентів
1. **Чіткі інструкції**:
   - Пишіть конкретні, детальні системні інструкції
   - Вказуйте формат відповіді, якщо потрібно
   - Визначайте мову відповіді

2. **Якісні інструменти (tools)**:
   - Пишіть докладні docstrings
   - Описуйте всі параметри
   - Обробляйте помилки в інструментах
   - Повертайте структуровані дані (dict, list)

3. **Валідація вводу**:
   ```python
   def safe_divide(a: float, b: float) -> dict:
       """Ділить два числа з перевіркою на нуль."""
       if b == 0:
           return {"error": "Ділення на нуль неможливе", "result": None}
       return {"result": a / b, "error": None}
   ```

4. :star: Напишіть власного агента дотримуючись цих порад. Додайте код агента та опис чому ви обрали саме такі інструкції та інструменти.

---
### Розширене завдання: Агент з збереженням стану
1. Створіть проект агента та налаштуйте API ключ:
   ```bash
   poetry run adk create stateful_agent
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > stateful_agent/.env
   ```

2. У файлі `stateful_agent/agent.py`:
   ```python
   import json
   from pathlib import Path
   from google.adk.agents.llm_agent import Agent
   
   STATE_FILE = Path("stateful_agent/user_state.json")
   
   def load_state() -> dict:
       """Завантажує стан з файлу"""
       if STATE_FILE.exists():
           with open(STATE_FILE, 'r', encoding='utf-8') as f:
               return json.load(f)
       return {}
   
   def save_state(data: dict) -> dict:
       """Зберігає стан у файл"""
       with open(STATE_FILE, 'w', encoding='utf-8') as f:
           json.dump(data, f, indent=2, ensure_ascii=False)
       return {"status": "saved", "data": data}
   
   def remember_fact(key: str, value: str) -> dict:
       """Запамʼятовує факт про користувача"""
       state = load_state()
       state[key] = value
       return save_state(state)
   
   def recall_fact(key: str) -> dict:
       """Згадує факт про користувача"""
       state = load_state()
       value = state.get(key)
       if value:
           return {"key": key, "value": value, "found": True}
       return {"key": key, "value": None, "found": False}
   
   root_agent = Agent(
       model='gemini-2.5-flash',
       name='stateful_agent',
       description="Агент який памʼятає користувача між сесіями.",
       instruction="""
       Ти персональний асистент який памʼятає інформацію про користувача.
       
       Коли користувач розповідає щось про себе, використовуй remember_fact.
       Коли потрібно згадати щось, використовуй recall_fact.
       
       Будь уважним та корисним. Відповідай українською мовою.
       """,
       tools=[remember_fact, recall_fact],
   )
   ```

3. :star: Запустіть агента, розкажіть йому щось про себе, вийдіть та запустіть знову. Перевірте чи агент памʼятає попередню інформацію. Додайте скріншоти обох сесій у звіт.

---
## Workflow Агенти - Sequential, Loop, Parallel

Workflow агенти - це спеціалізовані компоненти ADK, призначені для оркестрації виконання підагентів. На відміну від LLM агентів, workflow агенти працюють за заздалегідь визначеною логікою (детерміністично) і керують тим, як і коли інші агенти виконуються.

### Sequential Agent - Послідовне виконання
`SequentialAgent` виконує підагенти один за одним у строгому порядку. Використовуйте його коли потрібно виконати завдання у фіксованій послідовності.

1. Створіть проект агента та налаштуйте API ключ:
   ```bash
   poetry run adk create code_pipeline
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > code_pipeline/.env
   ```

2. Скопіюйте код з [`code_pipeline/agent.py`](code_pipeline/agent.py) та створіть pipeline для розробки коду.

3. :star: Запустіть Sequential агента:
   ```bash
   poetry run adk run code_pipeline
   ```

4. :star: Протестуйте з запитом: "Створи функцію для обчислення факторіалу числа". Агент послідовно виконає всі три етапи. Додайте результат у звіт.

5. :star: Поясніть у звіті переваги Sequential агента. Чому важливий порядок виконання підагентів?

---
### Loop Agent - Циклічне виконання
`LoopAgent` виконує підагенти у циклі до досягнення умови завершення. Використовуйте його для ітеративного покращення результату.

1. Створіть проект агента та налаштуйте API ключ:
   ```bash
   poetry run adk create story_improver
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > story_improver/.env
   ```

2. Скопіюйте код з [`story_improver/agent.py`](story_improver/agent.py) та створіть агента який покращує історію у циклі.

3. :star: Запустіть Loop агента:
   ```bash
   poetry run adk run story_improver
   ```

4. :star: При запуску введіть тему: "робот який навчився мріяти". Агент буде ітеративно покращувати історію. Додайте результат у звіт.

5. :star: Поясніть у звіті як працює механізм завершення циклу через `exit_loop` функцію.

---
### Parallel Agent - Паралельне виконання
`ParallelAgent` виконує підагенти одночасно (паралельно). Використовуйте для незалежних завдань, які можна виконувати конкурентно.

1. Створіть проект з Parallel агентом:
   ```bash
   poetry run adk create research_team
   echo 'GOOGLE_API_KEY="ваш_api_ключ_тут"' > research_team/.env
   ```

2. Скопіюйте код з [`research_team/agent.py`](research_team/agent.py). Цей агент виконує три дослідження паралельно та обʼєднує результати.

3. :star: Запустіть Parallel агента:
   ```bash
   poetry run adk run research_team
   ```

4. :star: Запитайте: "Які останні тренди у технологіях?". Агент виконає три дослідження паралельно та обʼєднає результати. Додайте звіт у ваш звіт.

5. :star: Поясніть у звіті переваги паралельного виконання. Чому це швидше ніж послідовне виконання трьох досліджень?

---
### Порівняння Workflow агентів

| Тип агента | Коли використовувати | Приклад |
|------------|---------------------|---------|
| **Sequential** | Завдання потрібно виконати у строгому порядку | Pipeline: код → рев'ю → рефакторинг |
| **Loop** | Потрібне ітеративне покращення до певної умови | Покращення тексту до досягнення якості |
| **Parallel** | Незалежні завдання можна виконати одночасно | Дослідження різних тем паралельно |

7. :star: Створіть власний workflow агент який комбінує всі три типи. Наприклад:
   - Parallel: збір даних з різних джерел
   - Sequential: обробка даних → аналіз → звіт
   - Loop: покращення звіту до досягнення якості
   
   Додайте код та результат у звіт.

---
### Здача роботи
- :star: Переконайтесь що всі створені агенти знаходяться у окремих папках всередині `notes/06_python_agents/`;
- :star: Переконайтесь що файли `.env` у кожній папці агента **НЕ** додані до репозиторію (мають бути у `.gitignore`);
- :star: Переконайтесь що файли `poetry.lock` та `pyproject.toml` додані до репозиторію;
- :star: Переконайтесь що всі `agent.py` файли мають коректний код з `root_agent`;
- :star: Коли робота завершена та всі файли завантажено до репозиторію, перейдіть у веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: Відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: Після того як викладач перевірить роботу, ви отримаєте оцінку у Google Classroom;

---
### Корисні посилання
- [Google AI Studio](https://aistudio.google.com/) - платформа для роботи з моделями Google
- [Google ADK Documentation](https://google.github.io/adk-docs/) - офіційна документація Google ADK
- [Google ADK Python Quickstart](https://google.github.io/adk-docs/get-started/python/) - швидкий старт для Python
- [Poetry Documentation](https://python-poetry.org/docs/) - документація Poetry
- [Gemini API](https://ai.google.dev/gemini-api/docs) - документація Gemini API

---
