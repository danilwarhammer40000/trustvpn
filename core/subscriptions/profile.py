from sqlalchemy import select

from database.models.user import User
from database.models.subscription import Subscription


async def build_profile(
    session,
    tg_id: int,
):

    user_query = select(User).where(
        User.tg_id == tg_id
    )

    user_result = await session.execute(
        user_query
    )

    user = user_result.scalar_one()

    sub_query = select(
        Subscription
    ).where(
        Subscription.user_id == user.id,
        Subscription.active == True,
    )

    sub_result = await session.execute(
        sub_query
    )

    subscription = sub_result.scalar_one()

    return {
        "tg_id": user.tg_id,
        "login": user.vpn_login,
        "password": user.vpn_password,
        "tariff": subscription.tariff,
        "expire": subscription.expires_at,
        "active": subscription.active,
    }
