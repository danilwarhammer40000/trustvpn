from sqlalchemy import select

from database.models.user import User
from database.models.subscription import Subscription


async def build_profile(
    session,
    tg_id: int,
):

    user_result = await session.execute(
        select(User).where(
            User.tg_id == tg_id
        )
    )

    user = user_result.scalar_one_or_none()

    if not user:
        return None

    sub_result = await session.execute(
        select(
            Subscription
        ).where(
            Subscription.user_id == user.id,
            Subscription.active == True,
        )
    )

    subscription = sub_result.scalar_one_or_none()

    if not subscription:
        return None

    return {
        "tg_id": user.tg_id,
        "login": user.vpn_login,
        "password": user.vpn_password,
        "tariff": subscription.tariff,
        "expire": subscription.expires_at,
        "active": subscription.active,
    }
