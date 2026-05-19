from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from apps.public_bot.keyboards import (
    main_keyboard,
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
