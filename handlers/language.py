from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import *
lang_router = Router()

@lang_router.message(Command(commands=['language']))
async def lang(message: Message):
    if message.from_user.language_code == "ru":
        await message.answer(
            '/ru - русский язык, '
            '/en - английский язык'
        )
    else:
        await message.answer(
            '/ru - Russian, '
            '/en - English'
        )
@lang_router.message(Command(commands=['ru']), F.text.startswith('/'))
async def ru(message: Message):
    if users[message.from_user.id]:
        users_lan[message.from_user.id] = 0
        await message.answer('Вы поменяли язык')
@lang_router.message(Command(commands=['en']), F.text.startswith('/'))
async def ru(message: Message):
    if users[message.from_user.id]:
        users_lan[message.from_user.id] = 1
        await message.answer('You have changed the language')