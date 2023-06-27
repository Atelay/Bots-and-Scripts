from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def max_price_info_keyboard():
    button_1 = KeyboardButton(text="Максимальная цена")
    button_2 = KeyboardButton(text="Изменить максимальную цену")
    return ReplyKeyboardMarkup(
        keyboard=[[button_1, button_2]], resize_keyboard=True, one_time_keyboard=True
    )


def min_price_info_keyboard():
    button_1 = KeyboardButton(text="Минимальная цена")
    button_2 = KeyboardButton(text="Изменить минимальную цену")
    return ReplyKeyboardMarkup(
        keyboard=[[button_1, button_2]], resize_keyboard=True, one_time_keyboard=True
    )


def min_price_keyboard():
    button_1 = KeyboardButton(text="500")
    button_2 = KeyboardButton(text="1500")
    button_3 = KeyboardButton(text="2000")
    button_4 = KeyboardButton(text="3000")
    button_5 = KeyboardButton(text="4000")
    button_6 = KeyboardButton(text="cancel")
    return ReplyKeyboardMarkup(
        keyboard=[[button_1, button_2, button_3, button_4, button_5], [button_6]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def max_price_keyboard():
    button_1 = KeyboardButton(text="5000")
    button_2 = KeyboardButton(text="7500")
    button_3 = KeyboardButton(text="10000")
    button_4 = KeyboardButton(text="15000")
    button_5 = KeyboardButton(text="20000")
    button_6 = KeyboardButton(text="cancel")
    return ReplyKeyboardMarkup(
        keyboard=[[button_1, button_2, button_3, button_4, button_5], [button_6]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def discount_change_keyboard():
    button_5 = KeyboardButton(text="5")
    button_10 = KeyboardButton(text="10")
    button_15 = KeyboardButton(text="15")
    button_20 = KeyboardButton(text="20")
    button_25 = KeyboardButton(text="25")
    button_6 = KeyboardButton(text="cancel")
    return ReplyKeyboardMarkup(
        keyboard=[[button_5, button_10, button_15, button_20, button_25], [button_6]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def discount_menu_keyboard():
    button_1 = KeyboardButton(text="Текущая скидка")
    button_2 = KeyboardButton(text="Изменить скидку")
    return ReplyKeyboardMarkup(
        keyboard=[[button_1, button_2]], resize_keyboard=True, one_time_keyboard=True
    )


def category_menu_keyboard():
    button_1 = KeyboardButton(text="Ножи")
    button_2 = KeyboardButton(text="Перчатки")
    button_3 = KeyboardButton(text="Снайперские винтовки")
    button_4 = KeyboardButton(text="Пистолеты")
    button_5 = KeyboardButton(text="Штурмовые винтовки")
    button_6 = KeyboardButton(text="Пистолеты-пулемёты")
    button_7 = KeyboardButton(text="Дробовики")
    button_8 = KeyboardButton(text="Пулемёты")

    return ReplyKeyboardMarkup(
        keyboard=[
            [button_1, button_2, button_4],
            [button_7, button_8],
            [button_5, button_6],
            [button_3],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
