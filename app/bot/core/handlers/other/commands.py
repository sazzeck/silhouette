from aiogram import types

from api import SilhouetteUser


user = SilhouetteUser()


async def cmd_start(
    message: types.Message,
) -> None:
    await message.delete()
    user_id = message.from_user.id
    user_firstname = message.from_user.first_name
    if not await user.is_exists(user_id):
        await message.answer(
            f"""<b>Hello, {user_firstname}</b>!
To continue you need to register.
Use this command: /register""",
        )
    else:
        await message.answer(
            f"""<b>Hello, {user_firstname}</b>!
Glad you're back!
Use /help to see all available commands.""",
        )


async def cmd_help(
    message: types.Message,
) -> None:
    pass
