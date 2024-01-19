from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from dotenv import load_dotenv
import os

# Adding bot token
load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

# Creating bot and dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Handler for /start command
async def process_start_command(message: Message):
    await message.answer(
        'Hey! I am EchoBot! Write something'
    )

# Handler for /help command
async def process_help_command(message: Message):
    await message.answer(
        'Write something and I send you your message'
    )

# Handler for any other messages
async def send_echo(message: Message):
    await message.reply(text=message.text)

# Handler registration
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_echo)
if __name__ == '__main__':
    dp.run_polling(bot)
