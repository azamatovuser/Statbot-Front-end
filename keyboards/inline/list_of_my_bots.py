from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import BASE_URL
import requests

rs = requests.get(url=f"{BASE_URL}bot/")
data = rs.json()

list_of_my_bots = InlineKeyboardMarkup(row_width=2)
next_page = InlineKeyboardButton('Далее', callback_data='next_page')
add_bot = InlineKeyboardButton('Добавить бота', callback_data='add_bot')
for i in data:
    list_of_my_bots.add(InlineKeyboardButton(f"{i['name']}", callback_data=f"{i['name']}"))
list_of_my_bots.add(next_page)
list_of_my_bots.add(add_bot)