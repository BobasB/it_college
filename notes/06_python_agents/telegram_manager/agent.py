"""Sequential-агент: план поста -> текст поста -> збереження у файл."""
from pathlib import Path

from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent

MODEL = "gemini-2.5-flash"

# Папка, куди зберігаються пости; не залежить від того, звідки запущено агента
POSTS_DIR = Path(__file__).parent / "posts"


def save_post_to_file(post_content: str, file_name: str = "post.md") -> dict:
    """Зберігає готовий пост у Markdown-файл.

    Args:
        post_content: повний текст поста.
        file_name: ім'я файлу (лише ім'я, без папок), наприклад "post.md".

    Returns:
        dict: статус збереження та шлях до файлу.
    """
    # Path(...).name відкидає папки з імені, щоб агент не міг записати файл за межі POSTS_DIR
    safe_name = Path(file_name).name or "post.md"
    POSTS_DIR.mkdir(exist_ok=True)
    path = POSTS_DIR / safe_name
    path.write_text(post_content, encoding="utf-8")
    return {"status": "success", "file_path": str(path)}


planner_agent = Agent(
    model=MODEL,
    name="planner_agent",
    description="Планує тематику та структуру поста в Telegram за ідеєю користувача.",
    instruction="""
    Ти AI-планувальник контенту для Telegram.
    Перетвори ідею користувача на короткий план поста:
    - робоча назва та цільова аудиторія;
    - 3 варіанти заголовка;
    - 3-4 основні тези;
    - висновок та заклик до дії (питання до читачів).
    Виводь тільки план українською мовою, без вступів.
    """,
    output_key="post_plan",
)

post_creator_agent = Agent(
    model=MODEL,
    name="post_creator_agent",
    description="Пише готовий пост у Telegram за планом.",
    instruction="""
    Ти AI-копірайтер. Напиши готовий пост за планом:

    {post_plan}

    Вимоги: короткі абзаци, **жирний** для акцентів, емодзі як маркери списків,
    не більше 4096 символів. Виводь тільки текст поста.
    """,
    output_key="post_content",
)

publisher_agent = Agent(
    model=MODEL,
    name="publisher_agent",
    description="Зберігає готовий пост у файл.",
    instruction="""
    Збережи цей пост у файл "post.md" інструментом save_post_to_file
    і напиши, куди саме його збережено.

    Пост:
    {post_content}
    """,
    tools=[save_post_to_file],
)

root_agent = SequentialAgent(
    name="telegram_manager",
    description="Створює та зберігає пост для Telegram за ідеєю користувача.",
    sub_agents=[planner_agent, post_creator_agent, publisher_agent],
)
