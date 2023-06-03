from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

list_of_my_bots = InlineKeyboardMarkup(row_width=2)
bot1 = InlineKeyboardButton('bot1', callback_data='bot1')
bot2 = InlineKeyboardButton('bot2', callback_data='bot2')
next_page = InlineKeyboardButton('Далее', callback_data='next_page')
add_bot = InlineKeyboardButton('Добавить бота', callback_data='add_bot')
list_of_my_bots.add(bot1, bot2)
list_of_my_bots.add(next_page)
list_of_my_bots.add(add_bot)