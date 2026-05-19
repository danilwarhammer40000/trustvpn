def build_profile_card(
    profile: dict,
):

    text = f"""
🔐 VPN профиль

🆔 TG:
{profile['tg_id']}

👤 Логин:
{profile['login']}

🔑 Пароль:
{profile['password']}

📦 Тариф:
{profile['tariff']}

📅 Активно до:
{profile['expire']}

🟢 Статус:
{'Активен' if profile['active'] else 'Неактивен'}

💳 Продлить подписку
"""

    return text.strip()
