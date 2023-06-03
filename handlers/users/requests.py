from aiogram import types
from loader import dp
from keyboards.inline.requests_button import requests_button
from keyboards.inline.priyem import priyem


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