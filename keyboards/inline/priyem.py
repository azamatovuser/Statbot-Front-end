from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

priyem = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Выключить', callback_data='turn_off')
two = InlineKeyboardButton('Сразу ✅️', callback_data='right_away')
three = InlineKeyboardButton('10 сек', callback_data='10_seconds')
four = InlineKeyboardButton('30 сек', callback_data='30_seconds')
five = InlineKeyboardButton('1 мин', callback_data='1_minutes')
six = InlineKeyboardButton('3 мин', callback_data='3_minutes')
seven = InlineKeyboardButton('1 час', callback_data='1_hours')
eight = InlineKeyboardButton('3 час', callback_data='3_hours')
nine = InlineKeyboardButton('Назад', callback_data='back_requests')
priyem.add(one, two, three, four, five, six, seven, eight, nine)