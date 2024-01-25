from aiogram import Bot, Dispatcher
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def my_start_filter(message: Message) -> bool:
    return message.text == '/start'

# Same but with lambda:
# start_check = lambda msg: msg.text == '/start'

# Handler for start command
@dp.message(my_start_filter)
async def process_start_command(message: Message):
    print(message)
    await message.answer(text='This is /start command')

if __name__ == '__main__':
    dp.run_polling(bot)
