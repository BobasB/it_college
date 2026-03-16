from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

MODEL = "gemini-2.5-flash"

# Дослідник 1: Python
python_researcher = Agent(
    name="PythonResearcher",
    model=MODEL,
    instruction="""
    Ти експерт з Python.
    Досліди останні нововведення в Python (версії 3.13-3.14).
    Надай короткий огляд (2-3 речення) найважливіших змін.
    Виводь ТІЛЬКИ огляд українською мовою.
    """,
    description="Досліджує новини Python.",
    output_key="python_research",
    tools=[google_search]
)

# Дослідник 2: AI/ML
ai_researcher = Agent(
    name="AIResearcher",
    model=MODEL,
    instruction="""
    Ти експерт зі штучного інтелекту.
    Досліди останні тренди в AI та машинному навчанні.
    Надай короткий огляд (2-3 речення) ключових тенденцій.
    Виводь ТІЛЬКИ огляд українською мовою.
    """,
    description="Досліджує тренди AI/ML.",
    output_key="ai_research",
    tools=[google_search]
)

# Дослідник 3: Web розробка
web_researcher = Agent(
    name="WebResearcher",
    model=MODEL,
    instruction="""
    Ти експерт з веб-розробки.
    Досліди сучасні фреймворки та технології веб-розробки.
    Надай короткий огляд (2-3 речення) популярних інструментів.
    Виводь ТІЛЬКИ огляд українською мовою.
    """,
    description="Досліджує веб-технології.",
    output_key="web_research",
    tools=[google_search]
)

# Parallel агент (всі дослідники працюють одночасно)
parallel_research = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[python_researcher, ai_researcher, web_researcher],
    description="Виконує паралельні дослідження за трьома напрямками."
)

# Синтезатор (об'єднує результати)
synthesizer = Agent(
    name="SynthesizerAgent",
    model=MODEL,
    instruction="""
    Ти аналітик який об'єднує результати досліджень.
    
    **Дослідження Python:**
    {python_research}
    
    **Дослідження AI/ML:**
    {ai_research}
    
    **Дослідження Web:**
    {web_research}
    
    Створи структурований звіт з трьох розділів:
    ## Огляд технологічних тенденцій
    
    ### Python
    [Узагальни дослідження Python]
    
    ### Штучний інтелект
    [Узагальни дослідження AI]
    
    ### Веб-розробка
    [Узагальни дослідження Web]
    
    ### Висновок
    [1-2 речення загального висновку]
    
    Виводь ТІЛЬКИ звіт українською мовою.
    """,
    description="Об'єднує результати паралельних досліджень у звіт."
)

# Sequential агент (спочатку паралельні дослідження, потім синтез)
root_agent = SequentialAgent(
    name="ResearchPipeline",
    sub_agents=[parallel_research, synthesizer],
    description="Координує паралельні дослідження та синтезує результати."
)
