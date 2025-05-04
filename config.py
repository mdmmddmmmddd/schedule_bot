
from datetime import time

# === Telegram ===
BOT_TOKEN = "7945647615:AAFh3NFDGJDyzx8VdyFrziHz3Wy_EeHfg44"  # Токен Telegram-бота 

# === База данных ===
DATABASE_URL = "sqlite:///./schedule.db"  # SQLite для простоты, можно заменить на PostgreSQL

# === Настройки оплаты ===
DEFAULT_HOURLY_RATE = 100     # Базовая ставка для официанта
SENIOR_HOURLY_RATE = 110      # Ставка для наставника (старшего официанта)

# === Ограничения и параметры графика ===
MAX_SHIFT_HOURS_PER_WEEK = 60         # Ограничение на часы в неделю
SHIFT_OVERHEAD_LIMIT = 1.10           # Допустимое превышение планового ФОТ (например, 10%)

# === Описание смен ===
# Смены подстраиваются под день недели (будни/выходные)
SHIFT_TYPES = {
    "full": {
        "base_hours": 12,             # Будни
        "weekend_hours": 14,          # Пт/Сб
        "start": time(10, 0),         # 10:00
        "roles": ["наставник", "официант"]
    },
    "evening": {
        "base_hours": 7,
        "weekend_hours": 9,
        "start": time(17, 0),         # 17:00
        "roles": ["наставник", "официант"]
    },
    "day_only": {
        "base_hours": 7,
        "weekend_hours": 7,
        "start": time(10, 0),
        "roles": ["наставник", "официант", "стажер"]
    }
}

# === Роли в системе ===
ROLES = ["официант", "наставник", "стажер", "менеджер", "управляющая"]
