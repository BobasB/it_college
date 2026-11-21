"""Telegram-бот, який відповідає через AI-агента ADK.

Запуск з папки notes/06_python_agents:  poetry run python -m telegram_bot
Потрібен файл .env зі змінними GOOGLE_API_KEY та TELEGRAM_TOKEN (див. .env.example).
"""
import logging
import os

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from .agent import root_agent

load_dotenv()
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger("telegram_bot")

APP_NAME = "telegram_bot"

# Один сервіс сесій та один runner на весь бот: тоді агент пам'ятає попередні повідомлення чату
session_service = InMemorySessionService()
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)


async def ask_agent(user_id: str, session_id: str, text: str) -> str:
    """Передає повідомлення агенту та повертає його фінальну відповідь."""
    session = await session_service.get_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)
    if session is None:
        await session_service.create_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)

    message = types.Content(role="user", parts=[types.Part(text=text)])
    answer = "Не вдалося отримати відповідь."
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=message):
        if event.is_final_response() and event.content and event.content.parts:
            answer = event.content.parts[0].text or answer
    return answer


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info("Користувач %s розпочав діалог", user.username)
    await update.message.reply_html(f"Привіт, {user.mention_html()}! Постав мені запитання.")


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.message.from_user.id)
    session_id = str(update.message.chat_id)
    logger.info("Повідомлення від %s: %s", user_id, update.message.text)
    await update.message.reply_text(await ask_agent(user_id, session_id, update.message.text))


def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise SystemExit("Задайте TELEGRAM_TOKEN у файлі .env")
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    logger.info("Бот запущено. Очікую на повідомлення...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
