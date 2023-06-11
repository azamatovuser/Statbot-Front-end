from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


set_captcha_button = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('🔘', callback_data='white_grey_captcha')
two = InlineKeyboardButton('Войти', callback_data='sign_in_captcha')
three = InlineKeyboardButton('⚪️', callback_data='white_captcha')
four = InlineKeyboardButton('🌭🍔🍕', callback_data='food_captcha')
five = InlineKeyboardButton('Назад', callback_data='back_to_set_captcha')
set_captcha_button.add(one, two, three, four, five)