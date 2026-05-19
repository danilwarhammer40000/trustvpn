from sqlalchemy import (
    Integer,
    String,
    Boolean,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.base import Base


class Plan(Base):

    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )

    duration_days: Mapped[int] = mapped_column(
        Integer,
    )

    price: Mapped[int] = mapped_column(
        Integer,
    )

    discount_percent: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    is_unlimited: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
