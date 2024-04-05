from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.filters import command
from aiogram.types import Message, CallbackQuery
from keyboards.til import lang
from keyboards.menu import menular

Vip = Router()

@Vip.callback_query(F.data == '🇺🇿')
async def uzb(query: CallbackQuery):
    await query.message.edit_text('siz Uzbek tilini tanladingiz, endi menyulardan foydalaning.', reply_markup=menular)
    

@Vip.callback_query(F.data == 'en')
async def uzb(query: CallbackQuery):
    await query.message.edit_text('siz ingliz tilini tanladingiz, endi menyulardan foydalaning.', reply_markup=menular)    