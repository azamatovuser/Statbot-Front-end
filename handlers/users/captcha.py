from aiogram import types
from loader import dp, bot
from keyboards.inline.captcha_button import captcha_button
from .my_bots import bot_id
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards.inline.set_captcha_button import set_captcha_button
from keyboards.inline.captcha_button_off import captcha_button_off
import requests
from data.config import BASE_URL


# rs = requests.get(url=f"{BASE_URL}bot/captcha/")
# data = rs.json()


@dp.callback_query_handler(text="captcha")
async def get_captcha_setting(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Капча ✅\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button)


@dp.callback_query_handler(text="back_captcha")
async def process_callback_query(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f'{bot_id[0]}\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21', reply_markup=detail_information_about_bot)


@dp.callback_query_handler(text="set_captcha")
async def process_callback_query(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Нажми на кнопку слева для выбора типа каптчи, '
                                        'а затем на кнопку справа для более индивидуальной'
                                        'настройки', reply_markup=set_captcha_button)


@dp.callback_query_handler(text="back_to_set_captcha")
async def back_captcha(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='Капча ✅\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button)


@dp.callback_query_handler(text="turn_off_captcha")
async def back_captcha(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='Капча ⛔️\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button_off)


@dp.callback_query_handler(text="turn_on_captcha")
async def back_captcha(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='Капча ✅\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button)