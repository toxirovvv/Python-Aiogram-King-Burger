from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 

menular = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Hot doglar🌭", callback_data="hot-dog🌭"),
            InlineKeyboardButton(text="Burgerlar🍔", callback_data="burger🍔")
            
        ],
        [
            InlineKeyboardButton(text="Lavashlar🌯", callback_data="lavash🌯"),
            InlineKeyboardButton(text="Kaboblar🍗", callback_data="kabob🍗")
            
        ],
        [
            InlineKeyboardButton(text="Setlar🍱", callback_data="setlar🍱"),
            InlineKeyboardButton(text="salatlar🥗", callback_data="salatlar🥗")
            
        ],
        [
            InlineKeyboardButton(text="Coffe ☕️", callback_data="coffe"),
            InlineKeyboardButton(text="Ichimliklar🍾", callback_data="suv")   
        ]
    ]
)