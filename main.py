import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

import funktions
from callback import calc_working

dp = Dispatcher()

TOKEN = "8885556083:AAGDfbSkf8ZNfX0AlPnAV4vozYQVnD7zTQI"


async def main():

    dp.startup.register(funktions.bot_ishlaganda)
    dp.message.register(funktions.start_bosganda,CommandStart())
    dp.shutdown.register(funktions.bot_toxtaganda)
    dp.callback_query.register(calc_working)

    bot = Bot(TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


asyncio.run(main())