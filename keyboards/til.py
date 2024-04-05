from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Uzbekcha 🇺🇿", callback_data="🇺🇿"),
            InlineKeyboardButton(text="English 🇺🇸", callback_data="en")
            
        ]
    ]
)

