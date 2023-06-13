from aiogram import types
from loader import dp, bot
from keyboards.inline.requests_button import requests_button
from keyboards.inline.priyem import priyem
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from .my_bots import bot_id
from keyboards import inline
from keyboards.inline.order_requests import order_requests
from keyboards.inline.requests_button import requests_button
from keyboards.inline.priyem_on import priyem_on

requests_list = []

count = len(requests_list)


@dp.callback_query_handler(text='1')
async def req(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Вступительные заявки 📫\n\n┣ '
                              'Принято: 0\n┣ Отклонено: 0\n┣ '
                              'В очереди: 0\nНастройка задержки:'
                              ' моментально\n\nМожно выключить '
                              'автоматическое принятие  или настроить '
                              'их фильтрацию с помощью кнопок ниже', reply_markup=inline.requests_button.requests_button)


async def process_requests():
    for user_id in requests_list:
        # Ваш код для принятия заявки пользователя с user_id
        # Например, можно использовать метод bot.send_message для отправки сообщения пользователю
        await bot.send_message(chat_id=user_id, text="Ваша заявка принята!")
    requests_list.clear()  # Очистка списка заявок после обработки


@dp.callback_query_handler(text='accept')
async def process_all_requests_handler(callback_query: types.CallbackQuery):
    await process_requests()
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Все заявки успешно приняты!")


@dp.callback_query_handler(text='decline')
async def process_all_requests_handler(callback_query: types.CallbackQuery):
    requests_list.clear()  # Очистка списка заявок
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Все заявки успешно отменены!")


@dp.callback_query_handler(text='avto_priem')
async def priem(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Автоматический приём ✅️\n\nНастройте '
                              'автоматический прием заявок и время, '
                              'через которое бот будет принимать '
                              'пользователя в канал', reply_markup=priyem)


@dp.callback_query_handler(text='turn_on')
async def priem(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Автоматический приём ✅️\n\nНастройте '
                              'автоматический прием заявок и время, '
                              'через которое бот будет принимать '
                              'пользователя в канал', reply_markup=priyem)


@dp.callback_query_handler(text='turn_off')
async def priem(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Автоматический приём ⛔️\n\nНастройте '
                              'автоматический прием заявок и время, '
                              'через которое бот будет принимать '
                              'пользователя в канал', reply_markup=priyem_on)


@dp.callback_query_handler(text='back')
async def back_def(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f'{bot_id[0]}\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21',
                           reply_markup=detail_information_about_bot)


@dp.callback_query_handler(text='back_requests')
async def back_request(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Вступительные заявки 📫\n\n┣ '
                              'Принято: 0\n┣ Отклонено: 0\n┣ '
                              'В очереди: 0\nНастройка задержки:'
                              ' моментально\n\nМожно выключить '
                              'автоматическое принятие  или настроить '
                              'их фильтрацию с помощью кнопок ниже', reply_markup=requests_button)


@dp.callback_query_handler(text='order')
async def filt(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f'В очереди {count} заявок 💤\n\n'
                              'Примите или отклоните все '
                              'скопившиеся заявки самостоятельно '
                              'одним нажатием', reply_markup=order_requests)


@dp.callback_query_handler(text='back_request')
async def back(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Вступительные заявки 📫\n\n┣ '
                              'Принято: 0\n┣ Отклонено: 0\n┣ '
                              'В очереди: 0\nНастройка задержки:'
                              ' моментально\n\nМожно выключить '
                              'автоматическое принятие  или настроить '
                              'их фильтрацию с помощью кнопок ниже', reply_markup=requests_button)