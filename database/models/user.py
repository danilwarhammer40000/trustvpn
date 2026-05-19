from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.base import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    tg_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        index=True,
    )

    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    full_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    vpn_login: Mapped[str] = mapped_column(
        String(255),
    )

    vpn_password: Mapped[str] = mapped_column(
        String(255),
    )

    is_trial_used: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="inactive",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
