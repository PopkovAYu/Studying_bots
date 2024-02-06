from aiogram.filters import BaseFilter
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Admin_ids list: admin_id - A.Yu. Popkov, 397982111 - A. Kim
admin_ids: list[int] = [admin_id, 397982111]

# Self-filter for admin check
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

# Handler for admins
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer('You are admin!')

# Handler for no admins
@dp.message()
async def answer_if_not_admins_update(message: Message):
    print(message)
    await message.answer('You are not admin!')

if __name__ == '__main__':
    dp.run_polling(bot)
