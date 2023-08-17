from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import menu_key, language_keyboard
from loader import dp
from utils.db_api.postgresql import send_human_info




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    try:
        send_human_info(
            f"""INSERT INTO main_getstart ("full_name", "username", "user_id") 
            values ('{full_name}', 'https://t.me/{username}', '{user_id}') returning *"""
        )
        await message.answer("Muloqot tilini tanlang: \nВыберите язык:"
                             , reply_markup=language_keyboard)
    except:
        await message.answer("Muloqot tilini tanlang: \nВыберите язык:"
                             , reply_markup=language_keyboard)

