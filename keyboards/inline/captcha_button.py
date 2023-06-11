from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


captcha_button = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Выключить', callback_data='turn_off_captcha')
two = InlineKeyboardButton('Настроить', callback_data='set_captcha')
three = InlineKeyboardButton('Назад', callback_data='back_captcha')
captcha_button.add(one, two, three)