import asyncio

from database.base import Base
from database.session import engine

from database.models import *


async def create():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )


if __name__ == "__main__":
    asyncio.run(create())
