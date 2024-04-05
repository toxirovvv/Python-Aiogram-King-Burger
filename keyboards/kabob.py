from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

kabob = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Qiyma Kabob🍗", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Burda Kabob🍗", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Sho'r Kabob🍗", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Tovuqli Kabob🍗", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Donar Kabob🍗", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Big Kabob🍗", callback_data="Tanlandi")
            
        ]
    ]
)