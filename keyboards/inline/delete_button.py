from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


delete_button = InlineKeyboardMarkup(row_width=1)
one = InlineKeyboardButton("Ой ошибочка", callback_data="back_delete")
two = InlineKeyboardButton("Нет", callback_data="back_delete")
three = InlineKeyboardButton("Да, я на 100% уверен!", callback_data="delete_group")
four = InlineKeyboardButton("Назад", callback_data="back_delete")
delete_button.add(one, two, three, four)