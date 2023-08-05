from aiogram import Dispatcher

# from .database_user import IsDatabaseUser
# from .group_admin import IsAdmin
from .private_chat import IsPrivate
# Функция которая выполняет установку кастомных фильтров
def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate) # Устанавливаем кастомный фильтр на приватный чат с ботом
    # dp.filters_factory.bind(IsGroup)
    # dp.filters_factory.bind(IsSubscriber)
    # dp.filters_factory.bind(IsAdmin)
    # dp.filters_factory.bind(IsDatabaseUser)