from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

burger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Big Burger🍔", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Double Burger🍔", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Cheese Burger🍔", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Chicken Burger🍔", callback_data="Tanlandi")
            
        ],
        [
            InlineKeyboardButton(text="Chizburger🍔", callback_data="Tanlandi"),
            InlineKeyboardButton(text="Gamburger🍔", callback_data="Tanlandi")
            
        ]
    ]
)