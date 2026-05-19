from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🔌 Подключиться"
            )
        ],
        [
            KeyboardButton(
                text="🎁 Триал"
            ),
            KeyboardButton(
                text="👤 Профиль"
            )
        ],
        [
            KeyboardButton(
                text="💳 Продлить"
            )
        ],
        [
            KeyboardButton(
                text="☕ Донат админу"
            )
        ],
        [
            KeyboardButton(
                text="✉ Сообщение админу"
            )
        ]
    ],
    resize_keyboard=True,
)
