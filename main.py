import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Botingiz tokini
TOKEN = "7547141380:AAEqS-3mC_8e_UoU6JbL6YvQ0eY7hO-I6-U" 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(f"Salom! TOSHKENTOVUZ botiga xush kelibsiz.\nBu bot 24/7 rejimida Railway-da ishlayapti!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
