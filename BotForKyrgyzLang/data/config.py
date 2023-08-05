import os # Импортируем библиотеку функций для работы с операционной системой

from dotenv import load_dotenv # Импортируем функцию load_dotenv

load_dotenv() # Запускаем функцию которая загружает переменное окружение из файла .env

# Получаем токен бота
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# Получаем токен ИИ openAI gpt 3.5
AI_GPT_TOKEN = str(os.getenv("AI_GPT_TOKEN"))

#получаем токен админа
ADMIN_ID = str(os.getenv('ADMIN_ID'))

# Список администраторов бота
admins = [
    ADMIN_ID
]

for admin in admins:
    print(type(admin))


