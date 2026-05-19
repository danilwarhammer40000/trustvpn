from sqlalchemy import select

from database.models.user import User
from database.models.subscription import Subscription


async def get_user_by_tg(
    session,
    tg_id: int,
):

    query = select(User).where(
        User.tg_id == tg_id
    )

    result = await session.execute(
        query
    )

    return result.scalar_one_or_none()


async def get_active_subscription(
    session,
    user_id: int,
):

    query = select(
        Subscription
    ).where(

        Subscription.user_id == user_id,

        Subscription.active == True,
    )

    result = await session.execute(
        query
    )

    return result.scalar_one_or_none()
