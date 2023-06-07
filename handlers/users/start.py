import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp, bot
from keyboards.default.my_bots import my_bots

bot_list = []


class BotTokenForm(StatesGroup):
    WaitingForToken = State()


async def validate_token(token):
    # Создаем экземпляр малого бота
    small_bot = Bot(token=token)

    try:
        # Получаем информацию о боте
        bot_info = await small_bot.get_me()
        bot_list.append(bot_info)


        # Возвращаем имя бота
        return True, bot_info.first_name
    except Exception as e:
        # Обработка ошибки, если не удалось получить информацию о боте
        print(f"Ошибка при получении информации о боте: {e}")
        return False, None


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    name = user.first_name if user.first_name else user.username
    await message.answer(f"Привет, {name}!\n\nHolus — конструктор в Telegram\n\nНовости: @holusnews\nТехподдержка: @holussupportbot")
    await message.answer(f"· Перейдите в @botfather;\n· Создайте нового бота;\n· Пришлите мне токен созданного бота;\n· Добавьте своего бота админом на канал;\n· Возвращайтесь — бот настроен!\n\nПример токена: 6003857882:AAHwbg9Mi1tmr_uFDn8Yd9vdOiOxHLLuuqY", reply_markup=types.ReplyKeyboardRemove())
    await BotTokenForm.WaitingForToken.set()


@dp.message_handler(state=BotTokenForm.WaitingForToken)
async def process_token(message: types.Message, state: FSMContext):
    user_token = message.text.strip()
    is_valid, bot_name = await validate_token(user_token)

    if is_valid:
        await message.answer(f"Бот Название успешно подключен!\n\n→ Отлично, осталось добавить бота в администраторы канала с которым будете работать - {bot_name}", reply_markup=my_bots)
        await state.finish()
    else:
        await message.answer("Неверный токен. Проверьте токен.")