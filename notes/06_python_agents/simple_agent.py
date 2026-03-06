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
