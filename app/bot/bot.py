from aiogram import Bot, Dispatcher, executor
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .plugins import register_handlers

from utils import Config


class SilhouetteBot:

    storage = MemoryStorage()

    bot = Bot(
        token=Config.BOT_TOKEN,
        validate_token=True,
        timeout=30,
    )

    dispatcher = Dispatcher(
        bot=bot,
        storage=storage
    )

    Bot.set_current(bot)
    Dispatcher.set_current(dispatcher)

    @staticmethod
    async def on_startup(dispatcher: Dispatcher) -> None:
        register_handlers(dispatcher)

    @staticmethod
    async def on_shutdown(dispatcher: Dispatcher) -> None:
        dispatcher.stop_polling()
        # await dispatcher.storage.close()
        # await dispatcher.storage.wait_closed()

    @classmethod
    def run(cls):
        executor.start_polling(
            cls.dispatcher,
            timeout=30,
            skip_updates=True,
            on_startup=cls.on_startup,
            on_shutdown=cls.on_shutdown,
        )
