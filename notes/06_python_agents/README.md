# AI Агенти з Google ADK
> AI агенти - це автономні програмні системи, здатні сприймати своє середовище, приймати рішення та виконувати дії для досягнення певних цілей. Google Agent Development Kit (ADK) - це набір інструментів для створення інтелектуальних агентів на основі великих мовних моделей.

## Мета роботи: __Навчитись створювати AI агентів з використанням Python, Google ADK та Poetry для управління залежностями проекту__

---
### Підготовка робочого середовища
1. Для роботи з AI агентами нам потрібен ключ API від Google. Перейдіть на [Google AI Studio](https://aistudio.google.com/app/apikey) та створіть новий API ключ.
   
2. :star: Збережіть отриманий API ключ у безпечному місці. Він знадобиться для роботи з агентами.

3. :fire: **ВАЖЛИВО**: Ніколи не комітьте API ключі в Git репозиторій! Для їх зберігання використовуйте файл `.env` та додайте його до `.gitignore`.

4. У цьому проекті застосовується [Poetry](https://python-poetry.org/) - сучасний інструмент для управління залежностями та пакетами Python. Встановіть Poetry якщо його ще немає:
   ```bash
   pip install poetry
   # Після успішного виконання перевірте
   poetry --version
   ```

5. :star: Вкажіть у звіті версію Poetry яка встановлена у вашій системі.

---
### Структура проекту та конфігурація
1. Проект вже має файл `pyproject.toml` який містить основні налаштування та залежності. Ознайомтесь з його вмістом:
   ```toml
   [project]
   name = "06-python-agents"
   version = "0.1.0"
   description = "Google ADK to create agents"
   requires-python = ">=3.13,<4.0.0"
   dependencies = [
       "python-dotenv (>=1.2.2,<2.0.0)",
       "google-adk (>=1.26.0,<2.0.0)"
   ]
   ```

2. Встановіть всі залежності проекту:
   ```bash
   cd notes/06_python_agents
   poetry install
   ```

3. :star: Переконайтесь що створився файл `poetry.lock`. Поясніть у звіті для чого потрібен цей файл.

4. Створіть файл `.env` у папці проекту для зберігання API ключа:
   ```bash
   echo "GOOGLE_API_KEY=ваш_api_ключ_тут" > .env
   ```

5. :star: Переконайтесь що файл `.env` доданий до `.gitignore` у кореневій папці репозиторію.

---
### Створення першого AI агента
1. Створіть файл `simple_agent.py` у папці проекту. Це буде наш перший простий агент який може відповідати на запитання:
   ```python
   import os
   from dotenv import load_dotenv
   from google import genai
   from google.genai import types

   # Завантажуємо змінні середовища з файлу .env
   load_dotenv()

   # Ініціалізуємо клієнта Google AI
   client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

   def simple_chat(user_prompt: str) -> str:
       """
       Проста функція для взаємодії з AI моделлю
       
       Args:
           user_prompt: запитання або команда від користувача
       
       Returns:
           str: відповідь моделі
       """
       response = client.models.generate_content(
           model='gemini-2.0-flash-exp',
           contents=user_prompt
       )
       return response.text

   if __name__ == "__main__":
       # Тестуємо агента
       question = "Що таке AI агент? Дай коротку відповідь українською."
       print(f"Запитання: {question}")
       answer = simple_chat(question)
       print(f"\nВідповідь агента:\n{answer}")
   ```

2. :star: Запустіть агента через Poetry:
   ```bash
   poetry run python simple_agent.py
   ```

3. :star: Вставте у звіт результат виконання програми.

4. :star: Змініть запитання у коді та поставте агенту 2-3 власних запитання. Вкажіть у звіті які запитання Ви поставили та які відповіді отримали.

---
### Створення агента з історією діалогу
1. Простий агент з попереднього завдання не пам'ятає попередні повідомлення. Створимо агента який зберігає історію розмови. Створіть файл `chat_agent.py`:
   ```python
   import os
   from dotenv import load_dotenv
   from google import genai
   from google.genai import types

   load_dotenv()
   client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

   class ChatAgent:
       """AI агент з підтримкою історії діалогу"""
       
       def __init__(self, model: str = 'gemini-2.0-flash-exp'):
           self.model = model
           self.history = []
       
       def send_message(self, message: str) -> str:
           """
           Відправляє повідомлення агенту та отримує відповідь
           
           Args:
               message: повідомлення від користувача
           
           Returns:
               str: відповідь агента
           """
           # Додаємо повідомлення користувача до історії
           self.history.append({
               'role': 'user',
               'parts': [{'text': message}]
           })
           
           # Отримуємо відповідь від моделі
           response = client.models.generate_content(
               model=self.model,
               contents=self.history
           )
           
           # Додаємо відповідь до історії
           self.history.append({
               'role': 'model',
               'parts': [{'text': response.text}]
           })
           
           return response.text
       
       def get_history_length(self) -> int:
           """Повертає кількість повідомлень в історії"""
           return len(self.history)
       
       def clear_history(self):
           """Очищає історію діалогу"""
           self.history = []
           print("Історія діалогу очищена.")

   if __name__ == "__main__":
       # Створюємо агента
       agent = ChatAgent()
       
       # Ведемо діалог
       print("=== Розмова з AI агентом ===\n")
       
       msg1 = "Привіт! Мене звати Студент. Як справи?"
       print(f"Користувач: {msg1}")
       response1 = agent.send_message(msg1)
       print(f"Агент: {response1}\n")
       
       msg2 = "А як мене звати?"
       print(f"Користувач: {msg2}")
       response2 = agent.send_message(msg2)
       print(f"Агент: {response2}\n")
       
       print(f"Кількість повідомлень в історії: {agent.get_history_length()}")
   ```

2. :star: Запустіть агента та вставте у звіт результат виконання програми.

3. :star: Розширте діалог власними запитаннями (додайте ще 2-3 повідомлення) та перевірте чи агент пам'ятає контекст розмови.

4. :star: Додайте у клас `ChatAgent` метод `save_history(filename: str)` який зберігає історію діалогу у JSON файл, та метод `load_history(filename: str)` який завантажує історію з файлу. Підказка: використайте модуль `json`.

---
### Створення агента з інструментами (Tools)
1. AI агенти можуть використовувати зовнішні інструменти (функції) для виконання специфічних завдань. Створимо агента який вміє виконувати математичні обчислення. Створіть файл `tool_agent.py`:
   ```python
   import os
   from dotenv import load_dotenv
   from google import genai
   from google.genai import types

   load_dotenv()
   client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

   # Визначаємо функції-інструменти
   def calculate_area_rectangle(width: float, height: float) -> float:
       """
       Обчислює площу прямокутника
       
       Args:
           width: ширина прямокутника
           height: висота прямокутника
       
       Returns:
           float: площа прямокутника
       """
       return width * height

   def calculate_area_circle(radius: float) -> float:
       """
       Обчислює площу кола
       
       Args:
           radius: радіус кола
       
       Returns:
           float: площа кола
       """
       import math
       return math.pi * radius ** 2

   # Реєструємо інструменти для моделі
   tools = [calculate_area_rectangle, calculate_area_circle]

   def agent_with_tools(user_query: str):
       """
       Агент який може використовувати математичні інструменти
       
       Args:
           user_query: запит користувача
       """
       print(f"Запит: {user_query}\n")
       
       # Відправляємо запит з доступними інструментами
       response = client.models.generate_content(
           model='gemini-2.0-flash-exp',
           contents=user_query,
           config=types.GenerateContentConfig(
               tools=tools,
               temperature=0.1
           )
       )
       
       # Виводимо відповідь
       for part in response.candidates[0].content.parts:
           if part.text:
               print(f"Відповідь агента: {part.text}")
           elif part.function_call:
               print(f"Виклик функції: {part.function_call.name}")
               print(f"Аргументи: {dict(part.function_call.args)}")

   if __name__ == "__main__":
       print("=== AI Агент з інструментами ===\n")
       
       # Тестуємо агента
       agent_with_tools("Обчисли площу прямокутника зі сторонами 5 та 10")
       print("\n" + "="*50 + "\n")
       agent_with_tools("Яка площа кола з радіусом 7?")
   ```

2. :star: Запустіть агента та вставте у звіт результат виконання.

3. :star: Додайте власну функцію-інструмент для обчислення об'єму куба (приймає довжину ребра). Зареєструйте її у списку `tools` та протестуйте.

4. :star: Додайте ще один інструмент на ваш вибір (наприклад, конвертер температури з Цельсія у Фаренгейта, або калькулятор ІМТ). Протестуйте роботу агента з новим інструментом.

---
### Створення інтерактивного агента
1. Створимо агента з яким можна спілкуватись у режимі реального часу через консоль. Створіть файл `interactive_agent.py`:
   ```python
   import os
   from dotenv import load_dotenv
   from google import genai

   load_dotenv()
   client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

   class InteractiveAgent:
       """Інтерактивний AI агент для консольного чату"""
       
       def __init__(self, system_instruction: str = None):
           self.model = 'gemini-2.0-flash-exp'
           self.history = []
           self.system_instruction = system_instruction or "Ти - корисний асистент який відповідає українською мовою."
       
       def chat(self, message: str) -> str:
           """Відправляє повідомлення та повертає відповідь"""
           self.history.append({'role': 'user', 'parts': [{'text': message}]})
           
           # Створюємо промпт з системною інструкцією
           full_contents = [{'role': 'user', 'parts': [{'text': self.system_instruction}]}] + self.history
           
           response = client.models.generate_content(
               model=self.model,
               contents=full_contents
           )
           
           self.history.append({'role': 'model', 'parts': [{'text': response.text}]})
           return response.text
       
       def run(self):
           """Запускає інтерактивну консольну сесію"""
           print("=" * 60)
           print("Інтерактивний AI Агент")
           print("Введіть 'вихід' або 'exit' для завершення")
           print("Введіть 'очистити' для очищення історії")
           print("=" * 60)
           print()
           
           while True:
               try:
                   user_input = input("Ви: ").strip()
                   
                   if not user_input:
                       continue
                   
                   if user_input.lower() in ['вихід', 'exit', 'quit']:
                       print("До побачення!")
                       break
                   
                   if user_input.lower() in ['очистити', 'clear']:
                       self.history = []
                       print("Історію очищено.\n")
                       continue
                   
                   # Отримуємо відповідь
                   response = self.chat(user_input)
                   print(f"\nАгент: {response}\n")
                   
               except KeyboardInterrupt:
                   print("\n\nРоботу завершено.")
                   break
               except Exception as e:
                   print(f"\nПомилка: {e}\n")

   if __name__ == "__main__":
       # Створюємо агента з кастомною системною інструкцією
       system_instruction = """
       Ти - досвідчений викладач програмування який допомагає студентам вивчати Python.
       Відповідай українською мовою, будь терплячим та наводь приклади коду коли це доречно.
       """
       
       agent = InteractiveAgent(system_instruction=system_instruction)
       agent.run()
   ```

2. :star: Запустіть інтерактивного агента та проведіть з ним діалог на тему Python (поставте мінімум 3-5 запитань). Зробіть скріншот або скопіюйте діалог у звіт.

3. :star: Змініть системну інструкцію (`system_instruction`) щоб агент поводився як експерт у іншій області (наприклад, математики, історії, або музики). Протестуйте нову поведінку агента.

---
### Робота з файлами та контекстом
1. AI агенти можуть обробляти великі обсяги тексту з файлів. Створимо агента який аналізує вміст файлів. Створіть файл `file_agent.py`:
   ```python
   import os
   from pathlib import Path
   from dotenv import load_dotenv
   from google import genai

   load_dotenv()
   client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

   class FileAnalyzerAgent:
       """Агент для аналізу текстових файлів"""
       
       def __init__(self):
           self.model = 'gemini-2.0-flash-exp'
       
       def read_file(self, filepath: str) -> str:
           """Читає вміст файлу"""
           try:
               with open(filepath, 'r', encoding='utf-8') as f:
                   return f.read()
           except Exception as e:
               return f"Помилка читання файлу: {e}"
       
       def analyze_code(self, code: str, task: str) -> str:
           """
           Аналізує код згідно з заданим завданням
           
           Args:
               code: вихідний код для аналізу
               task: що потрібно зробити з кодом
           
           Returns:
               str: результат аналізу
           """
           prompt = f"""
           Завдання: {task}
           
           Код для аналізу:
           ```python
           {code}
           ```
           
           Дай детальну відповідь українською мовою.
           """
           
           response = client.models.generate_content(
               model=self.model,
               contents=prompt
           )
           
           return response.text
       
       def analyze_file(self, filepath: str, task: str):
           """Аналізує файл"""
           print(f"Аналіз файлу: {filepath}")
           print(f"Завдання: {task}")
           print("-" * 60)
           
           code = self.read_file(filepath)
           if code.startswith("Помилка"):
               print(code)
               return
           
           result = self.analyze_code(code, task)
           print(result)

   if __name__ == "__main__":
       agent = FileAnalyzerAgent()
       
       # Аналізуємо файл simple_agent.py
       agent.analyze_file(
           "simple_agent.py",
           "Поясни що робить цей код та як він працює. Вкажи основні функції та їх призначення."
       )
   ```

2. :star: Запустіть агента та вставте у звіт результат аналізу файлу `simple_agent.py`.

3. :star: Використайте агента для аналізу файлу `chat_agent.py` з завданням "Знайди можливі покращення в цьому коді та запропонуй оптимізації". Вкажіть результат у звіті.

4. :star: Створіть простий Python файл з навмисною помилкою та використайте агента з завданням "Знайди помилки в цьому коді та запропонуй виправлення". Додайте у звіт ваш код з помилкою та відповідь агента.

---
### Додаткові завдання (на вибір)
1. :star: **Агент-перекладач**: Створіть агента який перекладає текст між мовами (наприклад, українська ↔ англійська). Агент повинен автоматично визначати мову вхідного тексту.

2. :star: **Агент-генератор коду**: Створіть агента який генерує Python код за описом задачі. Наприклад, "створи функцію яка сортує список словників за певним ключем".

3. :star: **Агент з температурою**: Поексперементуйте з параметром `temperature` (0.0 - 2.0) у конфігурації моделі. Створіть агента який генерує креативні історії та порівняйте результати при різних значеннях temperature.

4. :star: **Агент-помічник для лабораторних**: Створіть агента який допомагає виконувати лабораторні роботи - пояснює концепції, наводить приклади, перевіряє код.

---
### Тестування агентів
1. Створіть файл `test_agents.py` для простого тестування створених агентів:
   ```python
   import unittest
   from simple_agent import simple_chat
   from chat_agent import ChatAgent

   class TestAgents(unittest.TestCase):
       """Тести для AI агентів"""
       
       def test_simple_agent_response(self):
           """Перевіряємо що простий агент повертає відповідь"""
           response = simple_chat("Привіт")
           self.assertIsNotNone(response)
           self.assertIsInstance(response, str)
           self.assertGreater(len(response), 0)
       
       def test_chat_agent_history(self):
           """Перевіряємо що агент зберігає історію"""
           agent = ChatAgent()
           self.assertEqual(agent.get_history_length(), 0)
           
           agent.send_message("Тест 1")
           self.assertEqual(agent.get_history_length(), 2)  # user + model
           
           agent.send_message("Тест 2")
           self.assertEqual(agent.get_history_length(), 4)  # +2 повідомлення
           
           agent.clear_history()
           self.assertEqual(agent.get_history_length(), 0)
       
       def test_chat_agent_context(self):
           """Перевіряємо що агент памʼятає контекст"""
           agent = ChatAgent()
           agent.send_message("Моє улюблене число - 42")
           response = agent.send_message("Яке моє улюблене число?")
           
           # Перевіряємо що у відповіді є число 42
           self.assertIn("42", response)

   if __name__ == "__main__":
       unittest.main()
   ```

2. :star: Запустіть тести командою:
   ```bash
   poetry run python -m unittest test_agents.py -v
   ```

3. :star: Вставте у звіт результат виконання тестів.

4. :star: Додайте ще 2-3 власних тести для перевірки функціональності агентів.

---
### Робота з Poetry - додаткові можливості
1. Poetry дозволяє легко додавати нові залежності до проекту:
   ```bash
   poetry add requests  # додати нову бібліотеку
   poetry remove requests  # видалити бібліотеку
   poetry show  # показати всі встановлені пакети
   poetry show --tree  # показати дерево залежностей
   ```

2. :star: Виконайте команду `poetry show --tree` та вставте результат у звіт. Поясніть які пакети встановлені та для чого вони потрібні.

3. Poetry може створювати віртуальне середовище автоматично. Перевірте де знаходиться віртуальне середовище:
   ```bash
   poetry env info
   poetry env list
   ```

4. :star: Вкажіть у звіті шлях до віртуального середовища створеного Poetry.

---
### Здача роботи
- :star: Переконайтесь що всі створені Python файли знаходяться у папці `notes/06_python_agents/`;
- :star: Переконайтесь що файл `.env` **НЕ** доданий до репозиторію (має бути у `.gitignore`);
- :star: Переконайтесь що файли `poetry.lock` та `pyproject.toml` додані до репозиторію;
- :star: Коли робота завершена та всі файли завантажено до репозиторію, перейдіть у веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: Відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: Після того як викладач перевірить роботу, ви отримаєте оцінку у Google Classroom;

---
### Корисні посилання
- [Google AI Studio](https://aistudio.google.com/) - платформа для роботи з моделями Google
- [Google ADK Documentation](https://ai.google.dev/gemini-api/docs) - документація Google AI Development Kit
- [Poetry Documentation](https://python-poetry.org/docs/) - документація Poetry
- [Python dotenv](https://pypi.org/project/python-dotenv/) - робота зі змінними середовища

---