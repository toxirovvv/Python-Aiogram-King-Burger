from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

suvs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Coca-Cola🍾", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Pepsi🍾", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Seven-up🍾", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Ark Tea🍾", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Aloe Vera🍾", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Flash🍾", callback_data="Tanlandi")
            
        ]
    ]
)