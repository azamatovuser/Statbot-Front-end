from aiogram import types
from loader import dp
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards.inline.list_of_my_bots import list_of_my_bots


@dp.callback_query_handler(text='8')
async def back(call:types.CallbackQuery):
    await call.message.answer('Ваши боты\n→ Бот1\n→ Бот2\n→ Бот3\n→ Бот4\n\nВыберите бота для настройки [1/1]', reply_markup=list_of_my_bots)
    await call.message.delete()