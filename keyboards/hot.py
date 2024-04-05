from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

Hot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oddiy🌭", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Kanadiskiy🌭", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Kanada 2x🌭", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Dvaynoy🌭", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="King Dog🌭", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Chiz Dog🌭", callback_data="Tanlandi")
            
        ]
    ]
)