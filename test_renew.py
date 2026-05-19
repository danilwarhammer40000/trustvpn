import asyncio

from database.session import async_session

from core.subscriptions.renew import (
    renew_subscription,
)


async def main():

    async with async_session() as session:

        sub = await renew_subscription(
            session=session,
            user_id=1,
            days=60,
        )

        print(
            sub.duration_days,
            sub.expires_at,
        )


asyncio.run(main())
