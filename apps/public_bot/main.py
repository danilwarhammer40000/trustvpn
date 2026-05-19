import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from config.settings import (
    PUBLIC_BOT_TOKEN,
)

from apps.public_bot.handlers import (
    router,
)


async def main():

    bot = Bot(
        token=PUBLIC_BOT_TOKEN
    )

    dp = Dispatcher()

    dp.include_router(
        router
    )

    await dp.start_polling(
        bot
    )


if __name__ == "__main__":
    asyncio.run(
        main()
    )
