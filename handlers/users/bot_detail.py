from aiogram import types
from loader import dp, bot
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards.inline.list_of_my_bots import list_of_my_bots
from keyboards import inline
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(lambda c: c.data in ['1', '2', '3', '6', '7', '8'])
async def process_callback_query(callback_query: types.CallbackQuery):
    button_id = callback_query.data

    if button_id == '1':
        # Обработка нажатия кнопки "Вступительные заявки 📫"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text='Вступительные заявки 📫\n\n┣ '
                              'Принято: 0\n┣ Отклонено: 0\n┣ '
                              'В очереди: 0\nНастройка задержки:'
                              ' моментально\n\nМожно выключить '
                              'автоматическое принятие  или настроить '
                              'их фильтрацию с помощью кнопок ниже', reply_markup=inline.requests_button.requests_button)
    elif button_id == '2':
        # Обработка нажатия кнопки "Сообщения 💭"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Вы нажали кнопку 'Сообщения 💭'")
    elif button_id == '3':
        # Обработка нажатия кнопки "Розыгрыши 🎁"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Вы нажали кнопку 'Розыгрыши 🎁'")
    elif button_id == '6':
        # Обработка нажатия кнопки "Передать доступ 🔑"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Вы нажали кнопку 'Передать доступ 🔑'")
    elif button_id == '7':
        # Обработка нажатия кнопки "Избранное"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Вы нажали кнопку 'Избранное'")
    elif button_id == '8':
        # Обработка нажатия кнопки "Назад"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Вы нажали кнопку 'Назад'", reply_markup=inline.list_of_my_bots.list_of_my_bots)