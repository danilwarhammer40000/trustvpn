import os

from dotenv import load_dotenv


load_dotenv()


# -------------------
# Telegram
# -------------------

PUBLIC_BOT_TOKEN = os.getenv(
    "PUBLIC_BOT_TOKEN"
)

ADMIN_BOT_TOKEN = os.getenv(
    "ADMIN_BOT_TOKEN"
)

ADMIN_TG_ID = os.getenv(
    "ADMIN_TG_ID"
)


# -------------------
# PostgreSQL
# -------------------

DB_HOST = os.getenv(
    "DB_HOST",
    "localhost"
)

DB_PORT = os.getenv(
    "DB_PORT",
    "5432"
)

DB_NAME = os.getenv(
    "DB_NAME",
    "trustvpn"
)

DB_USER = os.getenv(
    "DB_USER",
    "trustvpn"
)

DB_PASSWORD = os.getenv(
    "DB_PASSWORD",
    "trustvpn"
)


DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{DB_USER}:"
    f"{DB_PASSWORD}@"
    f"{DB_HOST}:"
    f"{DB_PORT}/"
    f"{DB_NAME}"
)


# -------------------
# Redis
# -------------------

REDIS_HOST = os.getenv(
    "REDIS_HOST",
    "localhost"
)

REDIS_PORT = os.getenv(
    "REDIS_PORT",
    "6379"
)


REDIS_URL = (
    f"redis://"
    f"{REDIS_HOST}:"
    f"{REDIS_PORT}"
)


# -------------------
# YooKassa
# -------------------

YOOKASSA_SHOP_ID = os.getenv(
    "YOOKASSA_SHOP_ID"
)

YOOKASSA_SECRET = os.getenv(
    "YOOKASSA_SECRET"
)


# -------------------
# TrustTunnel
# -------------------

VPN_DOMAIN = os.getenv(
    "VPN_DOMAIN"
)

TRUSTTUNNEL_PATH = os.getenv(
    "TRUSTTUNNEL_PATH",
    "/opt/trusttunnel"
)

TRUSTTUNNEL_ENDPOINT_BIN = os.getenv(
    "TRUSTTUNNEL_ENDPOINT_BIN"
)


# -------------------
# Webhook
# -------------------

WEBHOOK_HOST = os.getenv(
    "WEBHOOK_HOST"
)

WEBHOOK_SECRET = os.getenv(
    "WEBHOOK_SECRET"
)


# -------------------
# Discounts
# -------------------

DISCOUNT_30 = 0

DISCOUNT_60 = 5

DISCOUNT_90 = 10

DISCOUNT_UNLIMITED = 20


# -------------------
# Trial
# -------------------

TRIAL_DAYS = 3


# -------------------
# Plans
# -------------------

PLAN_30_PRICE = 200

PLAN_60_PRICE = 360

PLAN_90_PRICE = 480

PLAN_UNLIMITED_PRICE = 3600
