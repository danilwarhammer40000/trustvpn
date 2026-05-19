import asyncio

from database.session import async_session
from core.subscriptions.profile import build_profile


async def main():

    async with async_session() as session:

        profile = await build_profile(
            session,
            111111111
        )

        print(profile)


asyncio.run(main())
