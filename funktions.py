from aiogram.types import Message
from aiogram import Bot
from inline_buttons import library_inlines


async def bot_ishlaganda(bot:Bot):
    await bot.send_message(chat_id=8819927088,text="Bot ishga tushdi...")


async def bot_toxtaganda(bot:Bot):
    await bot.send_message(chat_id=8819927088,text="Bot ishdan toxtadi...")

async def start_bosganda(message:Message):
    await message.answer("Misol ishlang\n\n>",reply_markup=library_inlines)