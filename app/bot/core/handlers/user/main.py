from aiogram import Dispatcher

from bot.core.states import UserRegister
from .commands import (
    cmd_register_start,
    register_comlete,
)


def register_user_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(cmd_register_start, commands="register")
    dispatcher.register_message_handler(register_comlete, state=UserRegister.password)
