from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

order_requests = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Принять все', callback_data='accept')
two = InlineKeyboardButton('Отклонить все️', callback_data='decline')
three = InlineKeyboardButton('Назад', callback_data='back_request')
order_requests.add(one, two, three)