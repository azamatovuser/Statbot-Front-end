from aiogram import types
from loader import dp, bot
from keyboards.inline.rassilka_button import rassilka_button, auto_delete
from keyboards.inline.list_of_my_bots import list_of_my_bots
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards import inline
from data.config import ADMINS
import requests
from data.config import BASE_URL
from .my_bots import bot_id
import datetime
from keyboards import inline
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import tracemalloc


tracemalloc.start()


class Rassilka(StatesGroup):
    WaitingForRassilka = State()



rs = requests.get(url=f"{BASE_URL}bot/statistic/")
data = rs.json()


@dp.callback_query_handler(text='rassilka_3')
async def back(call:types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f'{bot_id[0]}\n\nАудитория бота\n✅ Активная: 4 чел.\n🚫 Заблокировали: 0 чел.\n\nПол аудитории\n🙍 М: 74%\n🙍 Ж: 26%\n\nЯзыки аудитории\n🇮🇸 RU: 39%\n🇮🇸 EN: 39%\n🇮🇸 TR: 17.5%\n🇮🇸 Другие: 39%\n\nПодключенные каналы\n🔗 Канал1\n🔗 Канал2\n\nПоследнее обновление статистики 11 декабря 2023 года в 13:23:21', reply_markup=detail_information_about_bot)


def replace_tags(message, user):
    today = datetime.date.today().strftime("%d.%m.%Y")
    message = message.replace("{username}", user.username)
    message = message.replace("{name}", user.first_name)
    message = message.replace("{today}", today)
    return message


# Создание инлайн-клавиатуры
def create_rassilka_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("Превью ✅", callback_data="toggle_preview"),
        types.InlineKeyboardButton("URL-кнопки 🔗", callback_data="url_buttons")
    )
    keyboard.add(types.InlineKeyboardButton("Обычная отправка 🔔", callback_data="regular_send"))
    keyboard.add(types.InlineKeyboardButton("Автоудаление 💣", callback_data="auto_delete"))
    keyboard.add(
        types.InlineKeyboardButton("Отложить 🧭", callback_data="schedule"),
        types.InlineKeyboardButton("Запустить 🔽", callback_data="start")
    )
    keyboard.add(types.InlineKeyboardButton("Вернуться", callback_data="4"))

    return keyboard


@dp.callback_query_handler(text='4')
async def rassilka(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text='Отправьте сообщение, которое будет разослано вашим пользователям.\n\n'
             '→ тэг {username} добавит юзернейм пользователя\n'
             '→ тэг {name} добавит имя пользователя\n'
             '→ тэг {today} добавит сегодняшнюю дату',
        reply_markup=rassilka_button
    )
    await Rassilka.WaitingForRassilka.set()


@dp.message_handler(state=Rassilka.WaitingForRassilka)
async def handle_message(message: types.Message, state: FSMContext):
    if message.text:
        user = message.from_user
        replaced_message = replace_tags(message.text, user)
        user_ids = [538905701]
        for user_id in user_ids:
            await bot.send_message(
                chat_id=user_id,
                text=replaced_message,
                reply_markup=create_rassilka_keyboard()
            )
        await state.finish()


@dp.callback_query_handler(text="regular_send")
async def handle_regular_send(query: types.CallbackQuery):
    current_text = query.message.reply_markup.inline_keyboard[1][0].text
    new_text = "Без уведомления 🔕" if current_text == "Обычная отправка 🔔" else "Обычная отправка 🔔"

    # Update the button text
    query.message.reply_markup.inline_keyboard[1][0].text = new_text

    # Edit the message with the updated button text
    await query.message.edit_reply_markup(reply_markup=query.message.reply_markup)


@dp.callback_query_handler(text="toggle_preview")
async def handle_toggle_preview(query: types.CallbackQuery):
    current_text = query.message.reply_markup.inline_keyboard[0][0].text
    new_text = "Превью 🚫" if current_text == "Превью ✅" else "Превью ✅"

    # Update the button text
    query.message.reply_markup.inline_keyboard[0][0].text = new_text

    # Edit the message with the updated button text
    await query.message.edit_reply_markup(reply_markup=query.message.reply_markup)


@dp.callback_query_handler(text='start')
async def start_rassilka(call: types.CallbackQuery):
    user_ids = [538905701]  # Список идентификаторов пользователей
    user = call.from_user
    message = replace_tags(call.message.text, user)

    for user_id in user_ids:
        await bot.send_message(
            chat_id=user_id,
            text=message
        )
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Успешно!")


@dp.message_handler(commands='stats')
async def rassilka(message:types.Message):
    stats_button = types.InlineKeyboardMarkup(row_width=1)
    one = types.InlineKeyboardButton('Рассылка', callback_data='4')
    stats_button.add(one)
    msg = f'Статистика Holus 💎\n\nПользователей: {data[0]}\nПодключенных ботов: {data[1]}\nПользователей в их ботах: 7472\nПодключенных к ботам каналов: 731'
    await bot.send_message(chat_id=ADMINS[0], text=msg, reply_markup=stats_button)


@dp.callback_query_handler(text='auto_delete')
async def auto_delete1(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text="Успешно!",
        reply_markup=auto_delete
    )


@dp.callback_query_handler(text='url_buttons')
async def url_buttons_button_click_handler(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Вы нажали на URL-кнопки 🔗")


@dp.callback_query_handler(text='schedule')
async def schedule_button_click_handler(call: types.CallbackQuery):
    today = datetime.date.today()
    middle_date = today
    num_days = 5

    keyboard = create_schedule_keyboard(middle_date, num_days)
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"Дата запуска рассылки {today.strftime('%d.%m')}\n\n→ Нет запланированных рассылок\n\n"
             f"Отправьте время начала рассылки в любом формате.",
        reply_markup=keyboard
    )


def create_schedule_keyboard(middle_date, num_days):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    middle_button_text = middle_date.strftime("%d.%m")
    buttons = [
        types.InlineKeyboardButton((middle_date - datetime.timedelta(days=1)).strftime("%d.%m"), callback_data="previous"),
        types.InlineKeyboardButton(middle_button_text, callback_data="middle"),
        types.InlineKeyboardButton((middle_date + datetime.timedelta(days=1)).strftime("%d.%m"), callback_data="next")
    ]
    keyboard.add(*buttons)
    return keyboard


@dp.callback_query_handler(lambda call: call.data in ['previous', 'middle', 'next'])
async def select_date_handler(call: types.CallbackQuery):
    selected_button = call.data

    if selected_button == 'middle':
        await bot.answer_callback_query(callback_query_id=call.id, text="Готово!")
    else:
        await bot.answer_callback_query(callback_query_id=call.id)

        # Update the middle date based on the selected button
        middle_date = datetime.date.today()
        if selected_button == 'previous':
            middle_date -= datetime.timedelta(days=1)
        elif selected_button == 'next':
            middle_date += datetime.timedelta(days=1)

        # Update the keyboard
        num_days = 5
        keyboard = create_schedule_keyboard(middle_date, num_days)

        # Edit the message with the updated keyboard
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=keyboard
        )