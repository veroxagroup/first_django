from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


library_inlines = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(callback_data='7', text="7"),
            InlineKeyboardButton(callback_data='8', text="8"),
            InlineKeyboardButton(callback_data='9', text="9"),
            InlineKeyboardButton(callback_data='+', text="+"),


        ],
        [
            InlineKeyboardButton(callback_data='4', text="4"),
            InlineKeyboardButton(callback_data='5', text="5"),
            InlineKeyboardButton(callback_data='6', text="6"),
            InlineKeyboardButton(callback_data='-', text="-"),


        ],
        [
            InlineKeyboardButton(callback_data='1', text="1"),
            InlineKeyboardButton(callback_data='2', text="2"),
            InlineKeyboardButton(callback_data='3', text="3"),
            InlineKeyboardButton(callback_data='*', text="*"),


        ],
        [
            InlineKeyboardButton(callback_data='0', text="0"),
            InlineKeyboardButton(callback_data='.', text="."),
            InlineKeyboardButton(callback_data='/', text="/"),
            InlineKeyboardButton(callback_data='=', text="="),


        ],
        [
            InlineKeyboardButton(callback_data='C', text="C"),
            InlineKeyboardButton(callback_data='<', text="<"),


        ],

    ]
)