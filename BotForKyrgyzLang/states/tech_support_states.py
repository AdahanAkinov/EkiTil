from aiogram.dispatcher.filters.state import StatesGroup, State


class TechSupport(StatesGroup):
    waiting_for_title = State()
    waiting_for_description = State()
    sender_chat_id = State()
    sender_user_id = State()
