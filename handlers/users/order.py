from aiogram import types
from loader import dp, bot
from keyboards.inline.order_requests import order_requests
from keyboards.inline.requests_button import requests_button


@dp.callback_query_handler(text='order')
async def filt(callback_query:types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='В очереди 84 заявок 💤\n\n'
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