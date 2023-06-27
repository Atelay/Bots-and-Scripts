from aiogram.fsm.state import default_state
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text, Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove

from bot.config import config
from bot.lexicon.lexicon import LEXICON, HANDLERS
from bot.keyboards.keyboards import (
    max_price_keyboard,
    min_price_keyboard,
    max_price_info_keyboard,
    min_price_info_keyboard,
    discount_change_keyboard,
    discount_menu_keyboard,
    category_menu_keyboard,
)


router: Router = Router()
fsm_form = config.Form


# Этот хэндлер будет срабатывать на команду "/find" и предлогать категории для поиска.
@router.message(
    Text(text=HANDLERS["find"], ignore_case=True), StateFilter(default_state)
)
async def start_command_handler(message: Message):
    await message.answer(
        text=LEXICON["category"], reply_markup=category_menu_keyboard()
    )


# Этот хэндлер будет срабатывать на команду "/help" и показывать список доступных команд.
@router.message(Text(text=HANDLERS["help"], ignore_case=True))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON["/help"], reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях, кроме состояния по умолчанию, и отключать машину состояний
@router.message(
    Text(text=HANDLERS["cancel"], ignore_case=True), ~StateFilter(default_state)
)
async def cancel_command_handler(message: Message, state: FSMContext):
    await message.answer(text=LEXICON["fsm_cancel"], reply_markup=ReplyKeyboardRemove())
    await state.clear()


# Этот хэндлер будет срабатывать на команду "/cancel" в состоянии по умолчанию и сообщать, что эта команда доступна в машине состояний
@router.message(
    Text(text=HANDLERS["cancel"], ignore_case=True), StateFilter(default_state)
)
async def non_fsm_cancel_handler(message: Message):
    await message.answer(text=LEXICON["non_fsm_cancel"])


# Этот хэндлер будет срабатывать на команду "/discount" и предлогать изменить или показать текущую скидку
@router.message(Text(text=HANDLERS["discount"], ignore_case=True))
async def discount_command_handler(message: Message):
    await message.answer(text=LEXICON["action"], reply_markup=discount_menu_keyboard())


# Этот хэндлер будет срабатывать на текст 'Текущая скидка' и показывать текущую скидку
@router.message(Text(text=HANDLERS["current_disc"], ignore_case=True))
async def current_discount_handler(message: Message):
    await message.answer(
        text=LEXICON["current_disc"].format(config.current_discount),
        reply_markup=ReplyKeyboardRemove(),
    )


# Этот хэндлер будет срабатывать на текст 'Изменить скидку' и предлогать выбрать новое значение из предложенных
@router.message(Text(text=HANDLERS["change_disc"], ignore_case=True))
async def change_discount_handler(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON["prompt_text"], reply_markup=discount_change_keyboard()
    )
    await state.set_state(fsm_form.DiscountInputState)


# Этот хэндлер будет срабатывать на числа 5-25 и изменять текущий минимальный размер скидки
@router.message(
    StateFilter(fsm_form.DiscountInputState),
    lambda x: x.text.isdigit() and 5 <= int(x.text) <= 25,
)
async def update_discount_handler(message: Message, state: FSMContext):
    config.current_discount = int(message.text)
    await message.answer(
        text=LEXICON["min_discount"].format(config.current_discount),
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()


# Этот хэндлер будет срабатывать, если во время ввода скидки будет введено что-то некорректное
@router.message(StateFilter(fsm_form.DiscountInputState))
async def discount_value_invalid_handler(message: Message):
    await message.answer(
        text=LEXICON["disc_change_error"], reply_markup=discount_change_keyboard()
    )


# Этот хэндлер будет срабатывать на команду "/min" и предлогать показать либо изменить минимальный порог цены
@router.message(Command(commands=["min"]))
async def min_price_command_handler(message: Message):
    await message.answer(text=LEXICON["action"], reply_markup=min_price_info_keyboard())


# Этот хэндлер будет срабатывать на текст 'Текущая минимальная цена' и показывать текущее значение
@router.message(Text(text=HANDLERS["current_min_price"], ignore_case=True))
async def current_min_price_handler(message: Message):
    await message.answer(
        text=LEXICON["min_price"].format(config.min_price),
        reply_markup=ReplyKeyboardRemove(),
    )


# Этот хэндлер будет срабатывать на текст 'Изменить минимальную цену' и предлогать выбор из 5 новых значений
@router.message(Text(text=HANDLERS["change_min_price"], ignore_case=True))
async def change_min_price_handler(message: Message, state: FSMContext):
    await message.answer(text=LEXICON["prompt_text"], reply_markup=min_price_keyboard())
    await state.set_state(fsm_form.MinPriceInputState)


# Этот хэндлер будет срабатывать на числа от 1 до 4000 и устанавливать их как нижний порог
@router.message(
    StateFilter(fsm_form.MinPriceInputState),
    lambda x: x.text.isdigit() and 1 <= int(x.text) <= 4000,
)
async def update_min_price_handler(message: Message, state: FSMContext):
    config.min_price = int(message.text)
    await message.answer(
        text=LEXICON["change_min_price"].format(config.min_price),
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()


# Этот хэндлер будет срабатывать, если будет введена некорректная минимальная цена.
@router.message(StateFilter(fsm_form.MinPriceInputState))
async def min_amount_invalid_handler(message: Message):
    await message.answer(
        text=LEXICON["min_amount_invalid"], reply_markup=min_price_keyboard()
    )


# Этот хэндлер будет срабатывать на команду "/max" и предлогать показать либо изменить максимальный порог цены
@router.message(Command(commands=["max"]))
async def max_price_command_handler(message: Message):
    await message.answer(text=LEXICON["action"], reply_markup=max_price_info_keyboard())


# Этот хэндлер будет срабатывать на текст 'Текущая максимальная цена' и показывать текущее значение
@router.message(Text(text=HANDLERS["current_max_price"], ignore_case=True))
async def current_max_price_handler(message: Message):
    await message.answer(
        text=LEXICON["max_price"].format(config.max_price),
        reply_markup=ReplyKeyboardRemove(),
    )


# Этот хэндлер будет срабатывать на текст 'Изменить максимальную цену' и предлогать выбор из 5 новых значений
@router.message(Text(text=HANDLERS["change_max_price"], ignore_case=True))
async def change_max_price_handler(message: Message, state: FSMContext):
    await message.answer(text=LEXICON["prompt_text"], reply_markup=max_price_keyboard())
    await state.set_state(fsm_form.MaxPriceInputState)


# Этот хэндлер будет срабатывать на числа от 5000 до 25000 и устанавливать их как верхний порог
@router.message(
    StateFilter(fsm_form.MaxPriceInputState),
    lambda x: x.text.isdigit() and 5000 <= int(x.text) <= 25000,
)
async def update_max_price_handler(message: Message, state: FSMContext):
    config.max_price = int(message.text)
    await message.answer(
        text=LEXICON["change_max_price"].format(config.max_price),
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()


# Этот хэндлер будет срабатывать, если будет введена некорректная максимальная цена.
@router.message(StateFilter(fsm_form.MaxPriceInputState))
async def max_amount_invalid_handler(message: Message):
    await message.answer(
        text=LEXICON["max_amount_invalid"], reply_markup=max_price_keyboard()
    )


# Это хендлер перехватывающий все остальные сообщения
@router.message()
async def send_echo_handler(message: Message):
    await message.reply(text=LEXICON["echo"])
