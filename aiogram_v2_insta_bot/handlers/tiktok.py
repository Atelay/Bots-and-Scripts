import aiohttp
from aiogram import Dispatcher, types, filters

from utils.bot_logger import logger
from utils.tiktok_download import download


async def handle_tiktok_video(message: types.Message):
    logger.info(f"Handling message from @{message.from_user.username} with link: {message.text}")
    try:
        async with aiohttp.ClientSession() as session:
            media = await download(message.text, session)
            await message.reply_video(video=media[0], caption=f"{media[-1]}\n\nPosted by: {media[1]}")
    except Exception as e:
        logger.exception("An error occurred while handling TikTok video")
        await message.reply("An error occurred while handling the TikTok video. Please try again later.")
    logger.info("TikTok media handling complete")

def setup(dp: Dispatcher):
    dp.register_message_handler(handle_tiktok_video, filters.Regexp('^https?://www\.tiktok\.com/@[a-zA-Z0-9_]+/video/[0-9]+'))
