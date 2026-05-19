from datetime import datetime

from sqlalchemy import select

from database.models.subscription import Subscription

from core.subscriptions.service import (
    calculate_expire,
)


async def renew_subscription(
    session,
    user_id: int,
    days: int,
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

    subscription = result.scalar_one()

    now = datetime.utcnow()

    is_active = (
        subscription.expires_at > now
    )

    new_expire = calculate_expire(
        current_expire=subscription.expires_at,
        days=days,
        is_active=is_active,
    )

    subscription.expires_at = new_expire

    subscription.duration_days += days

    await session.commit()

    return subscription
