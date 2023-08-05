from aiogram import types
from loader import dp

import random 

list_of_answer = ['Такой команды нет...',
                  'Не могу Вас понять, Вы ведь все правильно написали? 😬']

@dp.message_handler() # Этот хендлер ловит все текстовые сообщения
async def command_error(message: types.Message): # Создаём асинхронную функцию
    list_random_answer = random.choice(list_of_answer)
    # Отправляем сообщение пользователю
    await message.answer(f'{list_random_answer}',
                         parse_mode='HTML') 
    # В поле '{message.text}' попадает текст который отправил пользователья