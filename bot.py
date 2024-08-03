import asyncio
from aiogram import Bot, Dispatcher
from bot_token import TOKEN
from handlers import commands, language
async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_routers(commands.c_router, language.lang_router)
    await bot.delete_webhook(drop_pending_updates=True) #deleting all gathered incoming messages
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())