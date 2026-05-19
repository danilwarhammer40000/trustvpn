from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

DATABASE_URL = (
    "postgresql+asyncpg://"
    "trustvpn:"
    "change_me@"
    "localhost:5432/"
    "trustvpn"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
