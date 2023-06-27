from aiogram.utils.markdown import hbold, hlink


def format_card(item):
    card = (
        f"{hlink(item.get('item_name'), item.get('item_3d'))}\n"
        f"{hbold('Скидка: ')}{item.get('item_discount')}\n"
        f"{hbold('Цена: ')}{item.get('item_price')}"
    )
    return card
