from sqlalchemy import select

from database.models.user import User


async def can_use_trial(
    session,
    tg_id: int,
):

    query = select(
        User
    ).where(
        User.tg_id == tg_id
    )

    result = await session.execute(
        query
    )

    user = result.scalar_one_or_none()

    if not user:
        return True

    return not user.is_trial_used


async def mark_trial_used(
    session,
    tg_id: int,
):

    query = select(
        User
    ).where(
        User.tg_id == tg_id
    )

    result = await session.execute(
        query
    )

    user = result.scalar_one()

    user.is_trial_used = True

    await session.commit()
