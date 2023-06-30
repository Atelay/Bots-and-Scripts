from aiogram import Dispatcher, types, filters
import instaloader
import requests

from utils.bot_logger import logger


loader = instaloader.Instaloader()

async def handle_instagram_content(message: types.Message):
    logger.info(f"Handling message from @{message.from_user.username} with link: {message.text}")
    media_url = message.text.strip()
    try:
        post_id = media_url.split('/')[4]
        post = instaloader.Post.from_shortcode(loader.context, post_id)
        caption = f"{post.caption}\n\nPosted by: @{post.owner_username}" \
                  f"\n{'Location: ' + post.location if post.location else ''}"

        if post.typename == 'GraphVideo':  # Video
            try:
                await message.reply_video(video=post.video_url, caption=caption)
            except:
                response = requests.get(post.video_url, stream=True)
                await message.reply_video(video=response.content, caption=caption)
        elif post.typename == 'GraphImage':  # Photo
            await message.reply_photo(photo=post.url, caption=caption)
        elif post.typename == 'GraphSidecar':  # Carousel
            media_list = []
            first_item = True

            for item in post.get_sidecar_nodes():
                if item.is_video:
                    media = types.InputMediaVideo(media=item.video_url)
                else:
                    media = types.InputMediaPhoto(media=item.display_url)
                if first_item:
                    media.caption = caption
                    first_item = False
                media_list.append(media)

            await message.reply_media_group(media=media_list)
            logger.info("Instagram media handling complete")

    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        await message.answer(f'Не могу проверить ссылку, что-то пошло не так.\n{str(e)}')

def setup(dp: Dispatcher):
    dp.register_message_handler(handle_instagram_content, filters.Regexp("^https?://(www\.)?instagram\.com"))
