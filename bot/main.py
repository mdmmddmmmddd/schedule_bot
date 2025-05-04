# bot/main.py

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

# 📥 Импортируем все роутеры
from bot.handlers.start import router as start_router
from bot.handlers.waiter import router as waiter_router
from bot.handlers.manager import router as manager_router
from bot.handlers.director import router as director_router
from bot.handlers.schedule import router as schedule_router

# === Настройки логирования ===
logging.basicConfig(level=logging.INFO)

# === Инициализация бота и диспетчера ===
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# === Подключение роутеров ===
dp.include_routers(
    start_router,
    waiter_router,
    manager_router,
    director_router,
    schedule_router
)

# === Точка входа ===
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
