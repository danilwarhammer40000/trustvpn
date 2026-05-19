import asyncio

from database.session import async_session

from core.subscriptions.create_user import (
    create_client,
)


async def main():

    async with async_session() as session:

        user = await create_client(
            session=session,

            tg_id=111111111,

            username="test_user",

            full_name="Test Client",

            vpn_login="111111111",

            vpn_password="pass123",

            days=30,
        )

        print(
            user.id,
            user.tg_id,
        )


asyncio.run(main())
