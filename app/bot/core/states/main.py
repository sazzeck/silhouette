from aiogram.dispatcher.filters.state import State, StatesGroup


class UserRegister(StatesGroup):
    user_id = State()
    username = State()
    password = State()
