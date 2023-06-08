from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):
    full_name = State()
    phone = State()


class Greetings(StatesGroup):
    greetings = State()


class Verify(StatesGroup):
    verify = State()


