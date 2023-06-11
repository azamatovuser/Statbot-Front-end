from aiogram import types
from loader import dp, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from random import shuffle
import requests
from data.config import BASE_URL
from .my_bots import bot_id


@dp.callback_query_handler(text='back_delete')
async def back(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f'{bot_id[0]}\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21',
                           reply_markup=detail_information_about_bot)


@dp.callback_query_handler(text="9")
async def del_chat(call: types.CallbackQuery):
    buttons = [InlineKeyboardButton("Ой, ошибочка", callback_data="back_delete"),
               InlineKeyboardButton("Нет!", callback_data="back_delete"),
               InlineKeyboardButton("Да, я на 100% уверен!", callback_data="del")]

    shuffle(buttons)

    markup = InlineKeyboardMarkup()

    for button in buttons:
        markup.row(button)
    else:
        markup.row(InlineKeyboardButton("Назад", callback_data="back_delete"))

    await call.message.edit_text("Вы <b>ТОЧНО</b> хотите удалить группу?", reply_markup=markup, parse_mode="HTML")


@dp.callback_query_handler(text='del')
async def delete_def(callback_query:types.CallbackQuery):
    requests.delete(url=f"{BASE_URL}bot/delete/{bot_id[0]}/")
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Успешно удалено!")