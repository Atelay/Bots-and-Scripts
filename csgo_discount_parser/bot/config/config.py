import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup


load_dotenv()


class Form(StatesGroup):
    DiscountInputState = State()
    MinPriceInputState = State()
    MaxPriceInputState = State()


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="/find", description="Show category menu"),
        BotCommand(command="/help", description="about bot and comand"),
        BotCommand(command="/discount", description="change discount"),
        BotCommand(command="/min", description="Change min price"),
        BotCommand(command="/max", description="Change max price"),
    ]
    await bot.set_my_commands(main_menu_commands)


token = os.getenv("TOKEN")
current_discount = 10
min_price = 2_000
max_price = 10_000
storage: MemoryStorage = MemoryStorage()
bot = Bot(token=token, parse_mode="HTML")
dp: Dispatcher = Dispatcher(storage=storage)
