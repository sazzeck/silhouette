# from aiogram import Dispatcher
from aiogram import Dispatcher
from aiogram.types import Message

from api import UsersAPI

users = UsersAPI()


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(cmd_start, commands=["start"])


async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    firstname = message.from_user.first_name
    lastname = message.from_user.last_name
    await users.create_user(
        user_id, username, firstname, lastname
    )
    await message.answer(f"{await users.fetch_user(user_id)}")
