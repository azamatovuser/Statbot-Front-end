from aiogram import types
from loader import dp
from keyboards.inline.rassilka_button import rassilka_button
from keyboards.inline.list_of_my_bots import list_of_my_bots
from keyboards.inline.detail_information_about_bot import detail_information_about_bot


@dp.callback_query_handler(text=['4'])
async def rassilki(call:types.CallbackQuery):
    await call.message.answer('Отправьте сообщение, '
                              'которое будет разослано '
                              'вашим пользователям.\n\n→ '
                              'тэг {username} добавит юзернейм'
                              ' пользователя\n→ тэг {bot1}'
                              ' добавит ссылку на канал\n→ тэг '
                              '{today} добавит сегодняшнюю дату', reply_markup=rassilka_button)
    await call.message.delete()


@dp.callback_query_handler(text='rassilka_3')
async def back(call:types.CallbackQuery):
    await call.message.answer('Бот1\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21', reply_markup=detail_information_about_bot)
    await call.message.delete()