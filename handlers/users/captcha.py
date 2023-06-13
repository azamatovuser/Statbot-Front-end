from aiogram import types
from loader import dp, bot
from keyboards.inline.captcha_button import captcha_button
from .my_bots import bot_id
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards.inline.set_captcha_button import set_captcha_button
from keyboards.inline.captcha_button_off import captcha_button_off
import requests
from data.config import BASE_URL
import random



# rs = requests.get(url=f"{BASE_URL}bot/captcha/")
# data = rs.json()
special_food_emojis = []


@dp.callback_query_handler(text="captcha")
async def get_captcha_setting(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Капча ✅\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button)


@dp.callback_query_handler(text="back_captcha")
async def process_callback_query(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=f'{bot_id[0]}\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21', reply_markup=detail_information_about_bot)


@dp.callback_query_handler(text="set_captcha")
async def captcha_set(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Нажми на кнопку слева для выбора типа каптчи, '
                                        'а затем на кнопку справа для более индивидуальной'
                                        'настройки', reply_markup=set_captcha_button)


@dp.callback_query_handler(text="back_to_set_captcha")
async def back_to_set(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='Капча ✅\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button)


@dp.callback_query_handler(text="turn_off_captcha")
async def turn_off(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='Капча ⛔️\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button_off)


@dp.callback_query_handler(text="turn_on_captcha")
async def turn_on(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text='Капча ✅\n\nЯ прочитал(а) правила [простая]\n\nМожно '
                              'выключить капчу совсем, или изменить ее тип и сложность с'
                              'помощью кнопок ниже', reply_markup=captcha_button)


@dp.callback_query_handler(text="food_captcha")
async def food(call: types.CallbackQuery):
    global selected_emoji
    food_emojis = ["🌭", "🍔", "🍕", "🚓", "🚑", "🚒", "🍓", "🍑", "🍆"]

    # Выбор трех случайных эмодзи из списка
    random_food_emojis = random.sample(food_emojis, 3)

    # Проверка наличия эмодзи с отдельным callback_data
    has_special_emoji = False
    for emoji in random_food_emojis:
        if emoji in special_food_emojis:
            has_special_emoji = True
            break

    # Если нет эмодзи с отдельным callback_data, выбираем случайное и добавляем его
    if not has_special_emoji:
        special_emoji = random.choice(random_food_emojis)
        special_food_emojis.append(special_emoji)
        random_food_emojis.remove(special_emoji)

    # Создание inline-кнопок для выбранных эмодзи
    keyboard = types.InlineKeyboardMarkup()
    for emoji in random_food_emojis:
        callback_data = f"captcha_{emoji}"
        keyboard.add(types.InlineKeyboardButton(text=emoji, callback_data=callback_data))

    # Добавление кнопки с отдельным callback_data на случайную позицию
    special_callback_data = f"captcha_{special_emoji}_special"
    random_position = random.randint(0, len(random_food_emojis))
    keyboard.insert(types.InlineKeyboardButton(text=special_emoji, callback_data=special_callback_data))

    # Отправка сообщения с капчей и кнопками
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=f'Ваша заявка на вступление\n\nНажмите на кнопку {special_emoji} с одним из эмодзи ниже, чтобы пройти капчу и подписаться на канал',
        reply_markup=keyboard
    )


@dp.callback_query_handler(lambda c: c.data.startswith('captcha'))
async def handle_captcha(callback_query: types.CallbackQuery):
    callback_data = callback_query.data

    if callback_data.endswith('_special'):
        # Отправка сообщения с текстом и кнопкой "Домой"
        await bot.edit_message_text(
            chat_id=callback_query.from_user.id,
            message_id=callback_query.message.message_id,
            text='Капча пройдена\n\nБольшое спасибо, доступ к каналу будет открыт в ближайшее время',
            reply_markup=types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton(text='Вернуться', callback_data='captcha')
            )
        )

    else:
        # Обработка неправильного ответа
        await bot.edit_message_text(
            chat_id=callback_query.from_user.id,
            message_id=callback_query.message.message_id,
            text='Капча не пройдена, повторите попытку!',
            reply_markup=types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton(text='Сначала', callback_data='set_captcha')
            ))