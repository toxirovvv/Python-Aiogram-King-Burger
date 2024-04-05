from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsSuperGroup(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'supergroup'

class IsGroup(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'group'
    
    
class IsPrivate(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'private'