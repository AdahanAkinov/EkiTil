from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_for_all = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='/menu')
            ]
        ], 
    resize_keyboard=True
)