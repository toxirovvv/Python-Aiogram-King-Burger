from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

Set = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Iftar set🍱", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Max Box retro🍱", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Mini Box🍱", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Familiy Set🍱", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Junior Set🍱", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Chicky Set🍱", callback_data="Tanlandi")
            
        ]
    ]
)