from loader import dp
from aiogram import types

#import openai
from data.config import AI_GPT_TOKEN

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from filters.private_chat import IsPrivate
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default.keyboard_menu import kb_menu_for_all

#openai.api_key = AI_GPT_TOKEN

# class Message_for_AI(StatesGroup):
#     message = State()


# cancel_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='🚫Отмена')
#         ]
#     ],
#     resize_keyboard=True
# )

# again_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='/AI_TSI')
#         ]
#     ],
#     resize_keyboard=True
# )


# @dp.message_handler(IsPrivate(), commands=['AI_TSI'])
# async def process_wait(message: types.Message):
#     await message.answer('❔У Вас есть вопрос для ИИ❔\n\n💬Введите:', reply_markup=cancel_kb)
#     await Message_for_AI.message.set()

# def update(messages, role, content):
#     messages.append({'role': role, 'content': content})
#     return messages

# @dp.message_handler(IsPrivate(), state=Message_for_AI.message)
# async def process_request_message(message: types.Message, state: FSMContext):
#     await state.update_data(message=message.text)  # добавляем в state
#     data = await state.get_data() 
#     prompt = data.get('message')  # получаем данные из сообщения
#     if prompt == '🚫Отмена':
#         await state.finish()
#         await message.answer('Запрос отменен 🚫', reply_markup=kb_menu_for_all)
#         await message.delete()
#     else:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": "Меня зовут Eagl_AI. Я Ваш помощник по учебе"},
#                 {"role": "assistant", "content": "Привет! Меня зовут Eagl_AI. Я помощник ИИ для студентов"},
#                 {"role": "user", "content": "Что ты можешь делать?"},
#                 {"role": "assistant", "content": "Я могу помочь Вам решать задачки, писать код, а также помогать по учебе в целом."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         await message.reply(response['choices'][0]['message']['content'], reply_markup=again_kb)
#         await state.finish() 

# #обработчик для отмены
# @dp.message_handler(IsPrivate(), Text('🚫Отмена'))
# async def cancel_AI_process(message: types.Message):
#     await message.answer('Запрос отменен 🚫')
#     await message.delete()
