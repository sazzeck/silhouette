from aiogram import Dispatcher

from .handlers import setup_all_handlers


def process_command_dependencies(dispatcher: Dispatcher) -> None:

    dependencies = (
        setup_all_handlers,
    )

    for dependence in dependencies:
        dependence(dispatcher)
