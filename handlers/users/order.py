from aiogram import types
from loader import dp
from keyboards.inline.order_requests import order_requests


@dp.callback_query_handler(text='order')
async def filt(call:types.CallbackQuery):
    await call.message.answer('В очереди 84 заявок 💤\n\n'
                              'Примите или отклоните все '
                              'скопившиеся заявки самостоятельно '
                              'одним нажатием', reply_markup=order_requests)
    await call.message.delete()