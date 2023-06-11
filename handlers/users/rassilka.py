from aiogram import types
from loader import dp, bot
from keyboards.inline.rassilka_button import rassilka_button
from keyboards.inline.list_of_my_bots import list_of_my_bots
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards import inline
from data.config import ADMINS
import requests
from data.config import BASE_URL
from .my_bots import bot_id


rs = requests.get(url=f"{BASE_URL}bot/statistic/")
data = rs.json()


@dp.callback_query_handler(text='rassilka_3')
async def back(call:types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f'{bot_id[0]}\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21', reply_markup=detail_information_about_bot)


@dp.callback_query_handler(text='4')
async def rassilka(call:types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='Отправьте сообщение, '
                                  'которое будет разослано '
                                  'вашим пользователям.\n\n→ '
                                  'тэг {username} добавит юзернейм'
                                  ' пользователя\n→ тэг {bot1}'
                                  ' добавит ссылку на канал\n→ тэг '
                                  '{today} добавит сегодняшнюю дату', reply_markup=inline.rassilka_button.rassilka_button)


@dp.message_handler(commands='stats')
async def rassilka(message:types.Message):
    stats_button = types.InlineKeyboardMarkup(row_width=1)
    one = types.InlineKeyboardButton('Рассылка', callback_data='4')
    stats_button.add(one)
    msg = f'Статистика Holus 💎\n\nПользователей: {data[0]}\nПодключенных ботов: {data[1]}\nПользователей в их ботах: 7472\nПодключенных к ботам каналов: 731'
    await bot.send_message(chat_id=ADMINS[0], text=msg, reply_markup=stats_button)