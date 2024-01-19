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

# Handler for photos
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

# Handler for stickers
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)

# Handler for any other text messages
async def send_echo(message: Message):
    await message.reply(message.text)

# Handler registration
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
