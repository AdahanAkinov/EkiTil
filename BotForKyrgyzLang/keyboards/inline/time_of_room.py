from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# клавиатура для выбора времени
keyboard = [
    InlineKeyboardButton(text='8:00-9:20', callback_data='08:00-09:20'),
    InlineKeyboardButton(text='9:30-10:50', callback_data='09:30-10:50'),
    InlineKeyboardButton(text='11:40-13:00', callback_data='11:40-13:00'),
    InlineKeyboardButton(text='13:10-14:30', callback_data='13:10-14:30'),
    InlineKeyboardButton(text='14:40-16:00', callback_data='14:40-16:00'),
    InlineKeyboardButton(text='16:10-17:30', callback_data='16:10-17:30'),
    InlineKeyboardButton(text='17:40-19:00', callback_data='17:40-19:00'),
    InlineKeyboardButton(text='19:00-20:00', callback_data='19:00-20:00'),
    InlineKeyboardButton(text='Cancel❌', callback_data='cancelRoom'),
]

time_room_kb = InlineKeyboardMarkup(row_width=3).add(*keyboard)


