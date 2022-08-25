from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils import Config


class SilhouetteBot:

    storage = MemoryStorage()

    bot = Bot(
        token=Config.BOT_TOKEN,
        validate_token=True,
        timeout=60,
    )

    dispatcher = Dispatcher(
        bot=bot,
        storage=storage,
    )

    Bot.set_current(bot)
    Dispatcher.set_current(dispatcher)

    @classmethod
    def run(cls):
        executor.start_polling(
            cls.dispatcher,
            skip_updates=True,
            on_startup=cls.on_startup,
            on_shutdown=cls.on_shutdown,
        )

    @staticmethod
    async def on_startup(dispatcher: Dispatcher):
        pass

    @staticmethod
    async def on_shutdown(dispatcher: Dispatcher):
        pass
