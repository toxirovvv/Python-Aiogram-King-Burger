from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.til import lang

start = Router()

@start.message(Command("start"))
async def start_command(message:Message):
    await message.answer(f"🇺🇿:  Assalomu alaykum {message.from_user.full_name}👋, King Food ga Xushkelibsiz \n \n 🇺🇸:  Hello {message.from_user.full_name}👋, Welcome to King Food ☺️", reply_markup=lang)
    
    
