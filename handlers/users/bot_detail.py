from aiogram import types
from loader import dp
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards.inline.list_of_my_bots import list_of_my_bots


@dp.callback_query_handler(text=['bot1'])
async def add_group(call:types.CallbackQuery):
    await call.message.answer('Бот1\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21', reply_markup=detail_information_about_bot)
    await call.message.delete()


@dp.callback_query_handler(text='8')
async def back(call:types.CallbackQuery):
    await call.message.answer('Ваши боты\n→ Бот1\n→ Бот2\n→ Бот3\n→ Бот4\n\nВыберите бота для настройки [1/1]', reply_markup=list_of_my_bots)
    await call.message.delete()