from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.burger import burger
from keyboards.hot import Hot
from keyboards.lavash import lavashes
from keyboards.kabob import kabob
from keyboards.set import Set
from keyboards.salat import Salat
from keyboards.coffe import coffe
from keyboards.suv_s import suvs
from keyboards.menu import menular

tanlandi = Router()

@tanlandi.callback_query(F.data == 'Tanlandi')
async def uzb(query: CallbackQuery):
    await query.message.edit_text('siz tanlagan mahsulot savatga tushdi. sizga 30daqiqa ichida yetkazib berishadi, Yana Buyurtma berish uchun /buyurtma ni bosing')

@tanlandi.callback_query(F.data == 'Tanlandi')
async def uzb(query: CallbackQuery):
    await query.message.edit_text('siz tanlagan mahsulot savatga tushdi. sizga 30daqiqa ichida yetkazib berishadi, Yana Buyurtma berish uchun /buyurtma ni bosing')
    
@tanlandi.callback_query(F.data == 'Tanlandi')
async def uzb(query: CallbackQuery):
    await query.message.edit_text('siz tanlagan mahsulot savatga tushdi. sizga 30daqiqa ichida yetkazib berishadi, Yana Buyurtma berish uchun /buyurtma ni bosing')

@tanlandi.callback_query(F.data == 'Tanlandi')
async def uzb(query: CallbackQuery):
    await query.message.edit_text('siz tanlagan mahsulot savatga tushdi. sizga 30daqiqa ichida yetkazib berishadi, Yana Buyurtma berish uchun /buyurtma ni bosing')

@tanlandi.message(Command('buyurtma'))
async def end(message: Message):
    await message.answer('Yaxshi, Mana Menu', reply_markup=menular)    
