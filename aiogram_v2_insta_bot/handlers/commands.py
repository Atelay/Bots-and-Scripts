from aiogram import Dispatcher, types


async def process_start_command(message: types.Message):
    await message.reply('Привет!\n'
                         'Я бот, который поможет тебе получить контент из Instagram. '
                         'Просто отправь мне ссылку на пост, '
                         'и я пришлю тебе его содержимое вместе с подписью.\n'
                         'Попробуй сейчас!')

def setup(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['help', 'start'])

