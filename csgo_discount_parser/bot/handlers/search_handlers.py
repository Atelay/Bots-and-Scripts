from time import sleep

from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from bot.utils.csgo_parser import csgo_parser
from bot.utils.format_card import format_card
from bot.config import config
from bot.utils.bot_logger import logger


bot = config.bot
router: Router = Router()


# Этот хэндлер будет срабатывать на ответ "Ножи" и удалять клавиатуру
@router.message(Text(text="Ножи", ignore_case=True))
async def knives_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=2,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")


# Этот хэндлер будет срабатывать на ответ "Перчатки" и удалять клавиатуру
@router.message(Text(text="Перчатки", ignore_case=True))
async def gloves_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=13,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")


# Этот хэндлер будет срабатывать на ответ "Снайперские винтовки" и удалять клавиатуру
@router.message(Text(text="Снайперские винтовки", ignore_case=True))
async def guns_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=4,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")


# Этот хэндлер будет срабатывать на ответ "Пистолеты" и удалять клавиатуру
@router.message(Text(text="Пистолеты", ignore_case=True))
async def guns_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=5,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")


# Этот хэндлер будет срабатывать на ответ "Штурмовые винтовки" и удалять клавиатуру
@router.message(Text(text="Штурмовые винтовки", ignore_case=True))
async def guns_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=3,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")


# Этот хэндлер будет срабатывать на ответ "Пистолеты-пулемёты" и удалять клавиатуру
@router.message(Text(text="Пистолеты-пулемёты", ignore_case=True))
async def guns_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=6,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")


# Этот хэндлер будет срабатывать на ответ "Дробовики" и удалять клавиатуру
@router.message(Text(text="Дробовики", ignore_case=True))
async def guns_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=7,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")


# Этот хэндлер будет срабатывать на ответ "Пулемёты" и удалять клавиатуру
@router.message(Text(text="Пулемёты", ignore_case=True))
async def guns_answer_handler(message: Message):
    try:
        await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
        data = await csgo_parser(
            category=8,
            discount=config.current_discount,
            min=config.min_price,
            max=config.max_price,
        )
        for index, item in enumerate(data):
            card = format_card(item)
            if index % 20 == 0:
                sleep(3)
            await message.answer(card, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.warning(f"Target [ID:{message.from_user.id}]: {e}")
