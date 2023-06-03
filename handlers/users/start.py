from aiogram import types
from loader import dp
from keyboards.default.my_bots import my_bots


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    name = user.first_name if user.first_name else user.username
    await message.answer(f"Привет, {name}!\n\nHolus — конструктор в Telegram\n\nНовости: @holusnews\nТехподдержка: @holussupportbot")
    await message.answer(f"· Перейдите в @botfather;\n· Создайте нового бота;\n· Пришлите мне токен созданного бота;\n· Добавьте своего бота админом на канал;\n· Возвращайтесь — бот настроен!\n\nПример токена: 6003857882:AAHwbg9Mi1tmr_uFDn8Yd9vdOiOxHLLuuqY", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands='token')
async def token_def(message:types.Message):
    await message.answer('Бот Название успешно подключен!\n\n→ Отлично, осталось добавить бота в администраторы канала с которым будете работать', reply_markup=my_bots)