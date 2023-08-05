import logging # Импортируем логику

from aiogram import Dispatcher # Импортируем диспетчер

from data.config import admins # Импортируем список администраторов бота которых мы добавили в config.py

# Создаём асинхронную функцию которая отправляет сообщение всем администраторам бота которых мы добавили в config.py
async def on_startup_notify(dp: Dispatcher):
    for admin in admins: # Получаем каждого администратора из списка администраторов
        try: # Пытаемся отправить сообщение администратору
            await dp.bot.send_message(admin, "Бот запущен!") # Отправляем сообщение

        except Exception as err: # Если не получилось отправить сообщение
            logging.exception(err)