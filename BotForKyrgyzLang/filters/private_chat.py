from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


# Кастомный фильтр на приватный чат с ботом
class IsPrivate(BoundFilter): # Только текстовые сообщения
    async def check(self, message: types.Message):
        # Сравниваем тип чата пользователя с типом чата ПРИВАТНЫЙ
        return message.chat.type == types.ChatType.PRIVATE # Если тип чата пользователя - ПРИВАТНЫЙ, то хендлер выполняеться
    
    