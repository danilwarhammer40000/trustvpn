from aiogram import Router
from aiogram.types import Message
from sqlalchemy import select

from database.session import async_session

from database.models.user import User

from core.subscriptions.create_user import (
    create_client,
)

from core.subscriptions.profile import (
    build_profile,
)

from core.subscriptions.card import (
    build_profile_card,
)

router = Router()


@router.message(
    lambda m: m.text == "🔌 Подключиться"
)
async def connect_handler(
    message: Message
):

    tg_id = message.from_user.id

    async with async_session() as session:

        result = await session.execute(
            select(User).where(
                User.tg_id == tg_id
            )
        )

        user = result.scalar_one_or_none()

        if not user:

            await create_client(
                session=session,

                tg_id=tg_id,

                username=message.from_user.username,

                full_name=message.from_user.full_name,

                vpn_login=str(tg_id),

                vpn_password="auto123",

                days=30,
            )

        profile = await build_profile(
            session,
            tg_id,
        )

        text = build_profile_card(
            profile
        )

        await message.answer(
            text
        )
