from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

# Adding bot token
load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

# Creating bot and dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Handler for /start command
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        'Hey! I am EchoBot! Write something'
    )

# Handler for /help command
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        'Write something and I send you your message'
    )

# Handler for any other messages
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
