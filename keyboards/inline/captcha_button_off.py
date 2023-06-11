from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


captcha_button_off = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Включить', callback_data='turn_on_captcha')
three = InlineKeyboardButton('Назад', callback_data='back_captcha')
captcha_button_off.add(one, three)