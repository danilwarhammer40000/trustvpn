from core.subscriptions.card import (
    build_profile_card,
)

profile = {
    "tg_id":111111111,
    "login":"11111111",
    "password":"pass123",
    "tariff":"D30",
    "expire":"2026-08-17",
    "active":True,
}

print(
    build_profile_card(
        profile
    )
)
