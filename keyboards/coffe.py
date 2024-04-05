from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

coffe = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oddiy Coffe ☕️", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Capucino ☕️", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Caramel ☕️", callback_data="Tanlandi"),
            InlineKeyboardButton(text="White Coffe ☕️", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Black Coffe ☕️", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Late ☕️", callback_data="Tanlandi")
            
        ]
    ]
)