from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#клавиатура отмены регистрации
cancel_reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отменить регистрацию ❌')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

#клава появляется в тот момент когда нужно выбрать группы ДЛЯ ПЕРВОГО КУРСА
course_of_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='SEST-1-22'),
            KeyboardButton(text='SEST-2-22'),
            KeyboardButton(text='SEST-3-22')
        ],
        [
            KeyboardButton(text='MIX-1-22'),
            KeyboardButton(text='MIX-2-22'),
            KeyboardButton(text='MIX-3-22')
        ],
        [
            KeyboardButton(text='ETSI-1-22'),
            KeyboardButton(text='EHI-1-22'),
            KeyboardButton(text='DHT-1-22')
        ],
        [
            KeyboardButton(text='Отменить регистрацию ❌')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
#для второго курса
course_of_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='SEST-1-21'),
            KeyboardButton(text='SEST-2-21'),
            KeyboardButton(text='SEST-3-21')
        ],
        [
            KeyboardButton(text='SFHT-1-21'),
            KeyboardButton(text='ECOL-1-21'),
            KeyboardButton(text='DMDT-1-21')
        ],
        [
            KeyboardButton(text='DHT-1-21'),
            KeyboardButton(text='DHT-2-21')
        ],
        [
            KeyboardButton(text='Отменить регистрацию ❌')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
# для третьего курса
course_of_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='SEST-1-20'),
            KeyboardButton(text='SFHT-1-20'),
            KeyboardButton(text='EHI-1-20')
        ],
        [
            KeyboardButton(text='ECOL-1-20'),
            KeyboardButton(text='DHT-1-20'),
            KeyboardButton(text='DHT-2-20')
        ],
        [
            KeyboardButton(text='DMDT-1-20'),
            KeyboardButton(text='Отменить регистрацию ❌')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# клавиатура с командой register 
reg_user_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/Register')
        ]
    ],
    resize_keyboard=True
)



