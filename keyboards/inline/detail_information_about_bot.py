from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


detail_information_about_bot = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Вступительные заявки 📫', callback_data='1')
two = InlineKeyboardButton('Сообщения 💭', callback_data='2')
three = InlineKeyboardButton('Розыгрыши 🎁', callback_data='3')
four = InlineKeyboardButton('Рассылка 📣', callback_data='4')
five = InlineKeyboardButton('Капча 👾', callback_data='5')
six = InlineKeyboardButton('Передать доступ 🔑', callback_data='6')
seven = InlineKeyboardButton('Избранное', callback_data='7')
eight = InlineKeyboardButton('Назад', callback_data='8')
nine = InlineKeyboardButton('Удалить', callback_data='9')
detail_information_about_bot.add(one)
detail_information_about_bot.add(two)
detail_information_about_bot.add(three, four)
detail_information_about_bot.add(five)
detail_information_about_bot.add(six)
detail_information_about_bot.add(seven)
detail_information_about_bot.add(eight, nine)