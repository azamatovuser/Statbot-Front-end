from aiogram import types
from loader import dp
from keyboards.inline.requests_button import requests_button
from keyboards.inline.priyem import priyem
from keyboards.inline.detail_information_about_bot import detail_information_about_bot


@dp.callback_query_handler(text=['1'])
async def requests_def(call:types.CallbackQuery):
    await call.message.answer('Вступительные заявки 📫\n\n┣ '
                              'Принято: 0\n┣ Отклонено: 0\n┣ '
                              'В очереди: 0\nНастройка задержки:'
                              ' моментально\n\nМожно выключить '
                              'автоматическое принятие  или настроить '
                              'их фильтрацию с помощью кнопок ниже', reply_markup=requests_button)
    await call.message.delete()


@dp.callback_query_handler(text='avto_priem')
async def priem(call:types.CallbackQuery):
    await call.message.answer('Автоматический приём ✅️\n\nНастройте '
                              'автоматический прием заявок и время, '
                              'через которое бот будет принимать '
                              'пользователя в канал', reply_markup=priyem)
    await call.message.delete()


@dp.callback_query_handler(text='back')
async def back_def(call:types.CallbackQuery):
    await call.message.answer('Бот1\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21', reply_markup=detail_information_about_bot)
    await call.message.delete()


@dp.callback_query_handler(text='back_requests')
async def back_request(call:types.CallbackQuery):
    await call.message.answer('Вступительные заявки 📫\n\n┣ '
                              'Принято: 0\n┣ Отклонено: 0\n┣ '
                              'В очереди: 0\nНастройка задержки:'
                              ' моментально\n\nМожно выключить '
                              'автоматическое принятие  или настроить '
                              'их фильтрацию с помощью кнопок ниже', reply_markup=requests_button)
    await call.message.delete()