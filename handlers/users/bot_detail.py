from aiogram import types
from loader import dp, bot
from keyboards.inline.detail_information_about_bot import detail_information_about_bot
from keyboards.inline.list_of_my_bots import list_of_my_bots
from keyboards import inline


@dp.callback_query_handler(lambda c: c.data in ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
async def process_callback_query(callback_query: types.CallbackQuery):
    button_id = callback_query.data

    if button_id == '1':
        # Обработка нажатия кнопки "Вступительные заявки 📫"
        await bot.send_message(callback_query.from_user.id, 'Вступительные заявки 📫\n\n┣ '
                              'Принято: 0\n┣ Отклонено: 0\n┣ '
                              'В очереди: 0\nНастройка задержки:'
                              ' моментально\n\nМожно выключить '
                              'автоматическое принятие  или настроить '
                              'их фильтрацию с помощью кнопок ниже', reply_markup=inline.requests_button.requests_button)
        await callback_query.message.delete()
    elif button_id == '2':
        # Обработка нажатия кнопки "Сообщения 💭"
        await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку 'Сообщения 💭'")
        await callback_query.message.delete()
    elif button_id == '3':
        # Обработка нажатия кнопки "Розыгрыши 🎁"
        await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку 'Розыгрыши 🎁'")
        await callback_query.message.delete()
    elif button_id == '4':
        # Обработка нажатия кнопки "Рассылка 📣"
        await bot.send_message(callback_query.from_user.id, 'Отправьте сообщение, '
                              'которое будет разослано '
                              'вашим пользователям.\n\n→ '
                              'тэг {username} добавит юзернейм'
                              ' пользователя\n→ тэг {bot1}'
                              ' добавит ссылку на канал\n→ тэг '
                              '{today} добавит сегодняшнюю дату', reply_markup=inline.rassilka_button.rassilka_button)
        await callback_query.message.delete()
    elif button_id == '5':
        # Обработка нажатия кнопки "Капча 👾"
        await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку 'Капча 👾'")
        await callback_query.message.delete()
    elif button_id == '6':
        # Обработка нажатия кнопки "Передать доступ 🔑"
        await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку 'Передать доступ 🔑'")
        await callback_query.message.delete()
    elif button_id == '7':
        # Обработка нажатия кнопки "Избранное"
        await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку 'Избранное'")
        await callback_query.message.delete()
    elif button_id == '8':
        # Обработка нажатия кнопки "Назад"
        await bot.send_message(callback_query.from_user.id, "Вы нажали кнопку 'Назад'", reply_markup=inline.list_of_my_bots.list_of_my_bots)
        await callback_query.message.delete()
    elif button_id == '9':
        # Обработка нажатия кнопки "Удалить"
        await bot.send_message(callback_query.from_user.id, 'Вы ТОЧНО хотите удалить группу?', reply_markup=inline.delete_button.delete_button)
        await callback_query.message.delete()