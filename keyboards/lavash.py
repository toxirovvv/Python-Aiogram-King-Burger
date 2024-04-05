from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

lavashes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Lavash extra🌯", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Lavash oddiy🌯", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Lavash Mini🌯", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Lavash Go'shtli🌯", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Lavash Tovuqli🌯", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Lavash Sirli🌯", callback_data="Tanlandi")
            
        ]
    ]
)