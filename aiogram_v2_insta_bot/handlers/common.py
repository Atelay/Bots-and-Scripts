from aiogram import Dispatcher, types

from utils.bot_logger import logger


async def handle_invalid_link(message: types.Message):
    logger.warning(f"The message: {message.text} isn`t link.")
    await message.reply(text="Пожалуйста, проверьте ссылку.")

def setup(dp: Dispatcher):
    dp.register_message_handler(handle_invalid_link)
