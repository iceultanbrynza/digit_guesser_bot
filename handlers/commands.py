from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import *
from lexicon import *
from copy import deepcopy
import random

random_number = lambda: random.randint(0,100)
c_router = Router()
@c_router.message(CommandStart())
async def start(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = deepcopy(user_info)
        if message.from_user.language_code == 'ru':
            users_lan[message.from_user.id] = 0
        else:
            users_lan[message.from_user.id] == 1
    await message.answer(answers["start"][users_lan[message.from_user.id]].format(name=message.from_user.first_name))
@c_router.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer(answers["help"][users_lan[message.from_user.id]])
@c_router.message(Command(commands=['cancel']))
async def cancel(message: Message):
    if users[message.from_user.id]["status"]:
        await message.answer(answers["cancel"][users_lan[message.from_user.id]]["on"])
        users[message.from_user.id]["status"] = False
    else:
        await message.answer(answers["cancel"][users_lan[message.from_user.id]]["off"])
@c_router.message(Command(commands=['stat']))
async def stat(message: Message):
    if users[message.from_user.id]["games"]>0:
        await message.answer(answers["stat"]['>0'][users_lan[message.from_user.id]].format(name=message.from_user.first_name,
                                                                                games=users[message.from_user.id]["games"],
                                                                                wins=users[message.from_user.id]["wins"],
                                                                                win_rate=users[message.from_user.id]["games"]/users[message.from_user.id]["wins"]))
    else:
        await message.answer(answers["stat"]['<0'][users_lan[message.from_user.id]])
@c_router.message(F.text.lower().in_(['да', 'давай', 'играть','игра', 'play', 'game']))
async def game(message: Message):
    if not users[message.from_user.id]["status"]:
        await message.answer(answers["go_game"][users_lan[message.from_user.id]]['off'])
        users[message.from_user.id]["status"] = True
        users[message.from_user.id]["secret_number"] = random_number()
        users[message.from_user.id]["attempts"] = 5
        users[message.from_user.id]["games"] +=1
    else:
        await message.answer(answers["go_game"][users_lan[message.from_user.id]]['on'])
@c_router.message(F.text.lower().in_(['не', 'нет', 'стоп','stop']))
async def refuse(message: Message):
    if not users[message.from_user.id]["status"]:
        await message.answer(answers["refuse_game"][users_lan[message.from_user.id]]['off'])
    else:
        await message.answer(answers["refuse_game"][users_lan[message.from_user.id]]['on'])
@c_router.message(lambda x: x.text and x.text.isdigit() and 1<=int(x.text)<=100)
async def input_digits(message: Message):
    if users[message.from_user.id]['status']:
        if int(message.text) == users[message.from_user.id]["secret_number"]:
            await message.answer(answers["digit_input"][users_lan[message.from_user.id]]['on']["guessed"].format(tries=5-users[message.from_user.id]["attempts"]))
            users[message.from_user.id]['wins']+=1
            users[message.from_user.id]['status'] = False
        elif int(message.text) > users[message.from_user.id]["secret_number"]:
            await message.answer(answers["digit_input"][users_lan[message.from_user.id]]['on']["smaller"])
            users[message.from_user.id]['attempts'] -=1
        elif int(message.text) < users[message.from_user.id]["secret_number"]:
            await message.answer(answers["digit_input"][users_lan[message.from_user.id]]['on']["bigger"])
            users[message.from_user.id]['attempts'] -=1
        if users[message.from_user.id]['attempts'] == 0:
            await message.answer(answers["digit_input"][users_lan[message.from_user.id]]['on']["loose"].format(secret_number=users[message.from_user.id]["secret_number"]))
            users[message.from_user.id]['status'] = False
    else:
        await message.answer(answers["digit_input"][users_lan[message.from_user.id]]['off'])
