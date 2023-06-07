import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

delete_button = InlineKeyboardMarkup(row_width=1)

# Создайте список кнопок one, two и three
buttons = [
    InlineKeyboardButton("Ой ошибочка", callback_data="back_delete"),
    InlineKeyboardButton("Нет", callback_data="back_delete"),
    InlineKeyboardButton("Да, я на 100% уверен!", callback_data="delete_group")
]

# Перемешайте порядок кнопок one, two и three
random.shuffle(buttons)

# Добавьте перемешанные кнопки one, two и three в InlineKeyboardMarkup
for button in buttons:
    delete_button.add(button)

# Добавьте кнопку "Назад" (four)
delete_button.add(InlineKeyboardButton("Назад", callback_data="back_delete"))
