from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from apps.public_bot.keyboards import main_keyboard

from database.session import async_session

from core.subscriptions.profile import (
    build_profile,
)

from core.subscriptions.card import (
    build_profile_card,
)

router = Router()


@router.message(
    CommandStart()
)
async def start(
    message: Message
):

    await message.answer(
        "TrustVPN\n\nВыберите действие",
        reply_markup=main_keyboard,
    )


@router.message(
    lambda m: m.text == "👤 Профиль"
)
async def profile_handler(
    message: Message
):

    async with async_session() as session:

        profile = await build_profile(
            session,
            message.from_user.id,
        )

        if not profile:

            await message.answer(
                "Профиль не найден"
            )

            return

        text = build_profile_card(
            profile
        )

        await message.answer(
            text
        )
