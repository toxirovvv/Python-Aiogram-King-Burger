import asyncio
import logging

from aiogram import  Dispatcher

from handlers.echo import router
from handlers.start import start
from handlers.menu_uz import menu_uz
from handlers.vip import Vip
from handlers.Tanla import tanlandi



from loader import bot,  db

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")


    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        start,
        Vip,
        menu_uz,
        tanlandi,
        router
    )



        
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
