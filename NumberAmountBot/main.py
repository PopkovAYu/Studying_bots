from aiogram.filters import BaseFilter, CommandStart, Command
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Filter for positive numbers in string and
# transfer them to handler
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Split message by spaces, normalize each part deleting
        # extra punctuation and invisible symbols, checking
        # that there are only numbers, making them integer and
        # adding in list
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # If there are numbers in list - return dictionary with numbers by 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False

# Start command handler
@dp.message(CommandStart())
async def process_strat_command(message: Message):
    await message.answer(
        'Привет! Напиши сообщение, которое будет\n'
        'начинаться c "найди числа" и я найду все числа\n'
        'в этом сообщении')

# Handler to find numbers in message with "Найди числа" and it has numbers in it
@dp.message(F.text.lower().startswith('найди числа'),
            NumbersInMessage())
# Getting list of numbers for handler
async def process_if_numbers(message: Message, numbers: list[int]):
    print(message)
    await message.answer(
        text=f'Нашел: {", ".join(str(num) for num in numbers)}')

# Handler to find numbers in message with "Найди числа" and it has NOT numbers in it
@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(
        text='Не нашел что-то:(')

if __name__ == '__main__':
    dp.run_polling(bot)
