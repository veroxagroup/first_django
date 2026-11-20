from aiogram.types import CallbackQuery

from inline_buttons import library_inlines


async def calc_working(callback: CallbackQuery):
    matn = callback.message.text
    current_data = callback.data
    eskison = matn.split('>')[-1].strip()
    yangison = eskison+str(current_data)



    goal = eval(yangison)
    matn = "Misol ishlang\n\n>" + str(goal)


    await callback.message.edit_text(matn,reply_markup=library_inlines)
