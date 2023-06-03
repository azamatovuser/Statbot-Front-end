from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


requests_button = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Автоматический приём', callback_data='avto_priem')
two = InlineKeyboardButton('Фильтрация', callback_data='filter')
three = InlineKeyboardButton('Очередь', callback_data='order')
four = InlineKeyboardButton('Назад', callback_data='back')
requests_button.add(one)
requests_button.add(two, three)
requests_button.add(four)