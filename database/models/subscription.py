from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Boolean,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.base import Base


class Subscription(Base):

    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        )
    )

    tariff: Mapped[str] = mapped_column(
        String(50),
    )

    duration_days: Mapped[int] = mapped_column(
        Integer,
    )

    is_unlimited: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )
