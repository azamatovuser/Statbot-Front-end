from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


rassilka_button = InlineKeyboardMarkup(row_width=1)
one = InlineKeyboardButton('Статистика рассылок 📊', callback_data='rassilka_1')
two = InlineKeyboardButton('Отложенные рассылки 🧭', callback_data='rassilka_2')
three = InlineKeyboardButton('Вернуться', callback_data='rassilka_3')
rassilka_button.add(one, two, three)


auto_delete = InlineKeyboardMarkup(row_width=2)
five = InlineKeyboardButton("Не удалять ✅️", callback_data='dont_delete')
six = InlineKeyboardButton("1 час", callback_data='1_hour')
seven = InlineKeyboardButton("3 часа", callback_data='3_hours')
eight = InlineKeyboardButton("6 часов", callback_data='6_hours')
nine = InlineKeyboardButton("12 часов", callback_data='12_hours')
ten = InlineKeyboardButton("24 часа", callback_data='24_hours')
eleven = InlineKeyboardButton("48 часов", callback_data='48_hours')
twelve = InlineKeyboardButton("Назад", callback_data='back_to_rassilka')
auto_delete.add(five)
auto_delete.add(six, seven, eight, nine, ten , eleven)
auto_delete.add(twelve)