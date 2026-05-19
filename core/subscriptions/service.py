from datetime import datetime, timedelta


def calculate_expire(
    current_expire: datetime | None,
    days: int,
    is_active: bool,
) -> datetime:

    now = datetime.utcnow()

    if current_expire and is_active and current_expire > now:
        return current_expire + timedelta(days=days)

    return now + timedelta(days=days)


def unlimited_expire() -> datetime:
    return datetime(
        2099,
        12,
        31,
        23,
        59,
        59,
    )
