import asyncio


from aiogram import types


async def purge_message(message: types.Message, timeout: int = 0) -> None:
    await asyncio.sleep(timeout)
    await message.delete()
