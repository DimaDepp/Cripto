import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command
from config import TELEGRAM_TOKEN

bot = Bot(
    token=TELEGRAM_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("✅ Бот работает! Команда /ping для теста.")

@dp.message(Command("ping"))
async def ping_cmd(message: types.Message):
    await message.answer("🏓 Понг!")

async def main():
    print("🚀 Бот запущен, жду команды в Telegram...")
    await dp.start_polling(bot)
