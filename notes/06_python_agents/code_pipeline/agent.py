from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.llm_agent import LlmAgent

MODEL = "gemini-2.5-flash"

# Агент 1: Пише код
code_writer = LlmAgent(
    name="CodeWriterAgent",
    model=MODEL,
    instruction="""
    Ти Python Code Generator.
    На основі запиту користувача, напиши Python код який виконує вимогу.
    Виводь ТІЛЬКИ блок коду у форматі ```python ... ```.
    Не додавай жодного іншого тексту.
    """,
    description="Пише початковий Python код за специфікацією.",
    output_key="generated_code"
)

# Агент 2: Рев'ює код
code_reviewer = LlmAgent(
    name="CodeReviewerAgent",
    model=MODEL,
    instruction="""
    Ти експерт Python Code Reviewer.
    Твоє завдання - надати конструктивний відгук на код.
    
    **Код для перегляду:**
    ```python
    {generated_code}
    ```
    
    **Критерії перевірки:**
    1. Правильність: чи код працює як задумано?
    2. Читабельність: чи код зрозумілий? Дотримання PEP 8?
    3. Ефективність: чи код достатньо оптимальний?
    4. Обробка помилок: чи обробляються крайні випадки?
    
    Надай відгук як стислий список. Якщо код відмінний, напиши: "Проблем не знайдено."
    Виводь українською мовою ТІЛЬКИ коментарі рев'ю.
    """,
    description="Переглядає код та надає відгук.",
    output_key="review_comments"
)

# Агент 3: Рефакторить код
code_refactorer = LlmAgent(
    name="CodeRefactorerAgent",
    model=MODEL,
    instruction="""
    Ти Python Code Refactoring AI.
    Покращ код на основі коментарів рев'ю.
    
    **Оригінальний код:**
    ```python
    {generated_code}
    ```
    
    **Коментарі рев'ю:**
    {review_comments}
    
    Застосуй пропозиції з рев'ю для поліпшення коду.
    Якщо рев'ю каже "Проблем не знайдено", поверни оригінальний код без змін.
    
    Виводь ТІЛЬКИ остаточний рефакторений код у форматі Markdown (блок коду```python ... ```).
    """,
    description="Рефакторить код на основі коментарів рев'ю.",
    output_key="refactored_code"
)

# Створюємо Sequential агента
root_agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[code_writer, code_reviewer, code_refactorer],
    description="Виконує послідовність: написання, рев'ю та рефакторинг коду.",
)
