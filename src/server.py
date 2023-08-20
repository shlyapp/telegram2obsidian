import os

from aiogram import Bot, Dispatcher, executor, types

from middlewares import AccesMiddleware
from config import ACCESS_ID


TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccesMiddleware(ACCESS_ID))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Это бот для быстрых заметок в Obsidian. \n"
                         "Чтобы узнать команды отправь /help")


@dp.message_handler(commands=['help'])
async def send_commands_list(message: types.Message):
    await message.answer("Что я умею: \n"
                         "/new - Создать новую заметку и отправить")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
