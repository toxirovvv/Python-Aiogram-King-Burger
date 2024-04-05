from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.filters import command
from aiogram.types import Message, CallbackQuery
from keyboards.menu import menular
from keyboards.hot import Hot
from keyboards.burger import burger
from keyboards.lavash import lavashes
from keyboards.kabob import kabob
from keyboards.set import Set
from keyboards.salat import Salat
from keyboards.coffe import coffe
from keyboards.suv_s import suvs

menu_uz = Router()

@menu_uz.callback_query(F.data == 'hot-dog🌭')
async def hot_dog(query: CallbackQuery):
    await query.message.edit_text('Siz Hot-dogni tanladingiz', reply_markup=Hot)
    
@menu_uz.callback_query(F.data == 'burger🍔')
async def burgers(query: CallbackQuery):
    await query.message.edit_text('Siz Burgerni tanladingiz', reply_markup=burger)   
    
  
@menu_uz.callback_query(F.data == 'lavash🌯')
async def lavash(query: CallbackQuery):
    await query.message.edit_text('Siz Lavashni tanladingiz', reply_markup=lavashes)       
    
    
@menu_uz.callback_query(F.data == 'kabob🍗')
async def kabobs(query: CallbackQuery):
    await query.message.edit_text('Siz Kaboblarni tanladingiz', reply_markup=kabob)      
    
@menu_uz.callback_query(F.data == 'setlar🍱')
async def set_s(query: CallbackQuery):
    await query.message.edit_text('Siz Setlarni tanladingiz', reply_markup=Set)   
     
@menu_uz.callback_query(F.data == 'salatlar🥗')
async def salat_s(query: CallbackQuery):
    await query.message.edit_text('Siz Salatlarni tanladingiz', reply_markup=Salat)     
    
     
@menu_uz.callback_query(F.data == 'coffe')
async def salat_s(query: CallbackQuery):
    await query.message.edit_text('Siz Coffe ichmoqchimisiz unda tanlang.', reply_markup=coffe)  
    
   
@menu_uz.callback_query(F.data == 'suv')
async def salat_s(query: CallbackQuery):
    await query.message.edit_text('Siz Ichimlik ichmoqchimisiz unda tanlang.', reply_markup=suvs)                        