from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .core import process_command_dependencies
from utils import Config


class SilhouetteBot:

    storage: MemoryStorage = MemoryStorage()

    bot: Bot = Bot(
        token=Config.BOT_TOKEN,
        parse_mode="HTML",
        validate_token=True,
        timeout=30,
    )

    dispatcher: Dispatcher = Dispatcher(
        bot=bot,
        storage=storage,
    )

    Bot.set_current(bot)
    Dispatcher.set_current(dispatcher)

    @staticmethod
    async def on_startup(dispatcher: Dispatcher) -> None:
        process_command_dependencies(dispatcher)

    @staticmethod
    async def on_shutdown(dispatcher: Dispatcher) -> None:
        dispatcher.stop_polling()

    @classmethod
    def run(cls) -> None:
        executor.start_polling(
            cls.dispatcher,
            timeout=30,
            skip_updates=True,
            on_startup=cls.on_startup,
            on_shutdown=cls.on_shutdown,
        )
