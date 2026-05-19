from datetime import datetime

from database.models.user import User
from database.models.subscription import Subscription

from core.subscriptions.service import (
    calculate_expire,
)


async def create_client(
    session,
    tg_id: int,
    username: str | None,
    full_name: str | None,
    vpn_login: str,
    vpn_password: str,
    days: int,
):

    user = User(
        tg_id=tg_id,
        username=username,
        full_name=full_name,
        vpn_login=vpn_login,
        vpn_password=vpn_password,
        status="active",
    )

    session.add(user)

    await session.flush()

    expire = calculate_expire(
        current_expire=None,
        days=days,
        is_active=False,
    )

    subscription = Subscription(
        user_id=user.id,
        tariff=f"D{days}",
        duration_days=days,
        is_unlimited=False,
        started_at=datetime.utcnow(),
        expires_at=expire,
        active=True,
    )

    session.add(subscription)

    await session.commit()

    return user
