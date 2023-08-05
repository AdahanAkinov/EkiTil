from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware

# Функция которая выполняет установку мидльварь
def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware()) # Выполняем установку ThrottlingMiddleware (Антиспам мидлварь)