from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

Salat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oddiy salat🥗", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Mix salat🥗", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Roka salat🥗", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Quymoqli Salat🥗", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Bahor Salat🥗", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Mevsim Salat🥗", callback_data="Tanlandi")
            
        ]
    ]
)