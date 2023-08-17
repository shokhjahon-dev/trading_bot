from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    phone = State()


class ForexSignalState(StatesGroup):
    full_name = State()
    phone = State()
    choose_price = State()
