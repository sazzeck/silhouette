from aiogram import Dispatcher

from .commands import (
    cmd_start,
    cmd_help,
)


def register_other_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_message_handler(cmd_start, commands="start")
    dispatcher.register_message_handler(cmd_help, commands="help")
