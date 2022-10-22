import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from api import SilhouetteUser
from bot.core.states import UserRegister
from bot.core.context_utils import purge_message


user = SilhouetteUser()


async def cmd_register_start(
    message: types.Message,
    state: FSMContext,
) -> None:
    await message.delete()
    user_id = message.from_user.id
    if not await user.is_exists(user_id):
        msg = await message.answer(
            """<b>You only need to enter a password.</b>
Think and write the password to me.""",
        )
        await UserRegister.password.set()
    else:
        await message.answer(
            f"""<b>{message.from_user.first_name}</b>, you are already registered!
Date of registration: <code>{await user.fetch_date_registration(user_id)}</code>""",
        )

    await asyncio.sleep(120)
    if not await user.is_exists(user_id):
        await state.finish()
        await purge_message(msg)
        await message.answer("<b>Registration time out!</b>")


async def register_comlete(
    message: types.Message,
    state: FSMContext,
) -> None:
    await message.delete()
    if message.text.startswith("/"):
        msg = await message.answer(
            """<b>Invalid character!</b>
Enter your password again."""
        )
        await purge_message(msg, 5)
    else:
        async with state.proxy() as data:
            data.update(
                user_id=message.from_user.id,
                username=message.from_user.username,
                password=message.text,
            )
            await user.create_user(
                data.get("user_id"),
                data.get("username"),
                data.get("password"),
            )
            await message.answer(
                f"""<b>You have successfully registered!</b>
id: <code>{data.get("user_id")}</code>
username: <code>{data.get("username")}</code>
password: <code>{data.get("password")}</code>"""
            )

        await state.finish()
