from datetime import datetime

from core.subscriptions.service import (
    calculate_expire,
)

result = calculate_expire(
    current_expire=None,
    days=30,
    is_active=False,
)

print(result)
