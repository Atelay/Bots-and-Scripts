import asyncio

from bot.config.config import bot, dp, set_main_menu
from bot.handlers import config_handlers, search_handlers
from bot.utils.bot_logger import logger


async def main():

    logger.info('Starting bot')
    await set_main_menu(bot)

    dp.startup.register(set_main_menu)
    dp.include_router(search_handlers.router)
    dp.include_router(config_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
