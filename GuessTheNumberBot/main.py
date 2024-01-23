import random
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Attempts count
ATTEMPTS = 7

# Users dict
users = {}

# Randomizer
def get_random_number() -> int:
    return random.randint(1, 100)

# Start command handler
@dp.message(CommandStart())
async def process_strat_command(message: Message):
    await message.answer(
        'Hey!\nLet us play Guess the number game!\n'
        'Send /help to get rules'
    )
    # Add new user
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
        }

# Help command handler
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        f'Rules:\nI come up eith the number from to 100'
        f'You should guess it with {ATTEMPTS} attempts.'
        f'Available commands:\n/help - shows rules'
        f'/cancel - end the game\n/stat - shows stats'
        f'Wanna play?'
    )

# Stat command handler
@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    await message.answer(
        f'Total games played: {users[message.from_user.id]["total_games"]}\n'
        f'Wins: {users[message.from_user.id]["wins"]}'
    )

# Cancel command handler
@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]["in_game"]:
        users[message.from_user.id]["in_game"] = False
        await message.answer(
            'You just leave the game.'
            'If you wanna play again just ask for it'
        )
    else:
        await message.answer(
            'We are not in a game right now.'
            'Wanna play?'
        )

# Poaitive answer handler
@dp.message(F.text.lower().in_(['yes', 'agree', 'game', 'play', 'wanna play', 'yeah']))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]["in_game"]:
        users[message.from_user.id]["in_game"] = True
        users[message.from_user.id]["secret_number"] = get_random_number()
        users[message.from_user.id]["attempts"] = ATTEMPTS
        await message.answer(
            'Yoohoo!\nTry to guess the number from 1 to 100'
        )
    else:
        await message.answer(
            'While we are playing I am able to react on numbers'
            'from 1 to 100 and /cancel and /help commands'
        )

# Negative answer handler
@dp.message(F.text.lower().in_(['no', 'nah', 'do not want']))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]["in_game"]:
        await message.answer(
            'Too bad:(\n\nIf you wanna play just say it:)'
        )
    else:
        await message.answer(
            'We are in game right now. Send numbers from 1'
            'to 100, please.'
        )

# Numbers handler
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_number_answer(message: Message):
    if users[message.from_user.id]["in_game"]:
        if int(message.text) == users[message.from_user.id]["secret_number"]:
            users[message.from_user.id]["in_game"] = False
            users[message.from_user.id]["total_games"] += 1
            users[message.from_user.id]["wins"] += 1
            await message.answer(
                'Hoorraay! That is the number\n'
                'Wanna play more?'
            )
        elif int(message.text) > users[message.from_user.id]["secret_number"]:
            users[message.from_user.id]["attempts"] -= 1
            await message.answer('My number is lower')
        elif int(message.text) < users[message.from_user.id]["secret_number"]:
            users[message.from_user.id]["attempts"] -= 1
            await message.answer('My number is bigger')

        if users[message.from_user.id]["attempts"] == 0:
            users[message.from_user.id]["in_game"] = False
            users[message.from_user.id]["total_games"] += 1
            await message.answer(
                f'Unfortunately, you dont have attempts any more'
                f'You just lost the game.'
                f'The number was {users[message.from_user.id]["secret_number"]}.'
                f'Wanna play again?'
            )
    else:
        await message.answer(
            'We are not in the game. Wanna play?'
        )

# Handler for any other messages
@dp.message()
async def process_other_answer(message: Message):
    if users[message.from_user.id]["in_game"]:
        await message.answer(
            'We are in the game right now'
            'Send numbers from 1 to 100, please'
        )
    else:
        await message.answer(
            'My capabilities are limited. Maybe'
            'just play the game?'
        )

if __name__ == '__main__':
    dp.run_polling(bot)
