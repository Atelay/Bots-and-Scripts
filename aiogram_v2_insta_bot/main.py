import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

from utils.bot_logger import logger
from handlers import instagram, tiktok, common, commands


load_dotenv()
env = lambda variable: os.getenv(variable)

WEBHOOK_HOST = env("WEBHOOK_HOST")
WEBHOOK_PATH = env("WEBHOOK_PATH")
WEBAPP_HOST = env("WEBAPP_HOST")
WEBAPP_PORT = env("WEBAPP_PORT")
BOT_TOKEN = env("TOKEN")

def main():

    logger.info('Starting bot')

    bot: Bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    instagram.setup(dp)
    tiktok.setup(dp)
    commands.setup(dp)
    common.setup(dp)

    async def on_startup(dp):
        await bot.set_webhook(f"{WEBHOOK_HOST}{WEBHOOK_PATH}")

    async def on_shutdown(dp):
        await bot.delete_webhook()

    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

if __name__ == '__main__':
    main()
