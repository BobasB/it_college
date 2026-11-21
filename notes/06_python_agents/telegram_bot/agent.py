from datetime import datetime

from google.adk.agents.llm_agent import Agent


def get_current_time() -> dict:
    """Повертає поточні дату та час.

    Returns:
        dict: ключ "time" у форматі "YYYY-MM-DD HH:MM:SS".
    """
    return {"status": "success", "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


root_agent = Agent(
    model="gemini-2.5-flash",
    name="telegram_assistant",
    description="Помічник студентів у Telegram.",
    instruction="""
    Ти помічник студентів, відповідаєш короткими повідомленнями у Telegram.
    Відповідай українською мовою, не більше 200 символів.
    Щоб дізнатись дату або час, використовуй інструмент get_current_time.
    """,
    tools=[get_current_time],
)
