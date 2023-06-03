from aiogram import types
from loader import dp
from keyboards.inline.rassilka_button import rassilka_button


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