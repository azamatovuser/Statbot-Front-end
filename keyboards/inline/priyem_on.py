from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

priyem_on = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Включить', callback_data='turn_on')
nine = InlineKeyboardButton('Назад', callback_data='back_requests')
priyem_on.add(one, nine)