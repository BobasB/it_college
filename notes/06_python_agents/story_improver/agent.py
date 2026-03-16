from google.adk.agents import LoopAgent, SequentialAgent
from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext

MODEL = "gemini-2.5-flash"

# Ключі для збереження стану
STATE_STORY = "current_story"
STATE_CRITIQUE = "critique"
COMPLETION_PHRASE = "Історія готова."
   

# Інструмент для виходу з циклу
def exit_loop(tool_context: ToolContext):
    """Викликається коли історія готова і цикл треба завершити."""
    print(f"[exit_loop] Цикл завершено агентом {tool_context.agent_name}")
    tool_context.actions.escalate = True
    tool_context.actions.skip_summarization = True
    return {}
   

# Агент 1: Початкове написання
initial_writer = Agent(
    name="InitialWriter",
    model=MODEL,
    instruction="""
    Ти письменник. Напиши початковий варіант короткої історії (1-2 речення).
    Зроби її дуже базовою, без деталей.
    Тема: {topic}
    
    Виводь ТІЛЬКИ текст історії українською мовою.
    """,
    description="Пише початковий варіант історії.",
    output_key=STATE_STORY
)
   

# Агент 2: Критик (всередині циклу)
critic = Agent(
    name="CriticAgent",
    model=MODEL,
    instruction=f"""
    Ти літературний критик. Переглянь історію:
    
    **Історія:**
    {{current_story}}
    
    **Критерії завершення (ВСІ мають виконатись):**
    1. Мінімум 4 речення
    2. Має початок, середину і кінець
    3. Містить хоча б одну описову деталь
    
    ЯКЩО будь-який критерій НЕ виконано - дай конкретні поради щодо покращення.
    ЯКЩО ВСІ критерії виконано - відповідай ТОЧНО: "{COMPLETION_PHRASE}"
    
    Виводь українською мовою.
    """,
    description="Критикує історію або сигналізує про завершення.",
    output_key=STATE_CRITIQUE
)
   

# Агент 3: Покращувач (всередині циклу)
improver = Agent(
    name="ImproverAgent",
    model=MODEL,
    instruction=f"""
    Ти редактор історій. Маєш покращити історію або завершити цикл.
    
    **Поточна історія:**
    {{current_story}}
    
    **Критика:**
    {{critique}}
    
    ЯКЩО критика точно "{COMPLETION_PHRASE}":
    - Викликай функцію exit_loop. НЕ виводь текст.
    
    ІНАКШЕ (є поради):
    - Застосуй поради для покращення історії.
    - Виводь ТІЛЬКИ покращену історію українською мовою.
    """,
    description="Покращує історію або викликає exit_loop.",
    tools=[exit_loop],
    output_key=STATE_STORY
)
   

# Loop агент (цикл покращення)
improvement_loop = LoopAgent(
    name="ImprovementLoop",
    sub_agents=[critic, improver],
    max_iterations=5  # Максимум 5 ітерацій
)
   

# Sequential агент (загальний контроль)
root_agent = SequentialAgent(
    name="StoryImprovementPipeline",
    sub_agents=[initial_writer, improvement_loop],
    description="Пише початкову історію та покращує її ітеративно."
)
