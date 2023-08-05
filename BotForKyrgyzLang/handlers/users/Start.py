import random

from aiogram import types

from loader import bot, dp
from filters import IsPrivate

from keyboards.default.keyboard_menu import kb_menu_for_all
from utils.misc import rate_limit


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start')
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text='Кыргызча уйронойлубу?😃', reply_markup=kb_menu_for_all)
