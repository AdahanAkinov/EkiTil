from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

# Создаём переменную бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

# Создаём диспетчер
dp = Dispatcher(bot, storage=storage)


__all__ = ['bot', 'storage', 'dp', 'db']