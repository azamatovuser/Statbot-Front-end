from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


rassilka_button = InlineKeyboardMarkup(row_width=1)
one = InlineKeyboardButton('Статистика рассылок 📊', callback_data='rassilka_1')
two = InlineKeyboardButton('Отложенные рассылки 🧭', callback_data='rassilka_2')
three = InlineKeyboardButton('Вернуться', callback_data='rassilka_3')
rassilka_button.add(one, two, three)