from aiogram import types
from keyboards.default.menu import register_course, register_course_ru, menu_key, menu_key_ru, signal, signal_ru, obuna, obuna_ru
from loader import dp, bot
from states.messageinfo import RegisterState, ForexSignalState
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import client_keyboard
from aiogram.types import ReplyKeyboardRemove
from utils.db_api.postgresql import send_human_info

# Button 1 -> ‍🎓Treyding kursi 2023
# !!! UZ !!!


@dp.callback_query_handler(lambda a: a.data == "course", state=None)
async def course_inline(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "Siz bilan boglanishimiz uchun telefon raqamingizmi jo'nating", reply_markup=register_course)
    await RegisterState.phone.set()


@dp.message_handler(text=["◀️Bosh menyuga qaytish", "◀️Вернуться в главный меню"], state=RegisterState.phone)
async def back_main(message: types.Message, state: FSMContext):
    if message.text == "◀️Bosh menyuga qaytish":
        await state.finish()
        await message.answer("Tanlang", reply_markup=menu_key)
    elif message.text == "◀️Вернуться в главный меню":
        await state.finish()
        await message.answer("Выберите:", reply_markup=menu_key_ru)
    else:
        pass



@dp.message_handler(state=RegisterState.phone, content_types='contact')
async def client_phone(message: types.Message, state: FSMContext):
    phone = message['contact']['phone_number']
    await state.update_data(
        {'phone': phone}
    )
    client_data = await state.get_data()
    phone = client_data.get("phone")
    send_human_info(f"""INSERT INTO main_humaninfo ("phone") 
        values ('{phone}') returning *""")
    await state.finish()
    await message.answer("Yaqin orada siz bilan ulanamiz!", reply_markup=menu_key)



# !!! RU !!!

@dp.callback_query_handler(lambda a: a.data == "course_ru", state=None)
async def course_inline(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "Отправьте нам свой номер телефона, чтобы мы могли связаться с вами", reply_markup=register_course_ru)
    await RegisterState.phone.set()



@dp.message_handler(state=RegisterState.phone, content_types='contact')
async def client_phone(message: types.Message, state: FSMContext):
    phone = message['contact']['phone_number']
    await state.update_data(
        {'phone': phone}
    )
    client_data = await state.get_data()
    phone = client_data.get("phone")
    send_human_info(f"""INSERT INTO main_humaninfo ("phone") 
        values ('{phone}') returning *""")
    await state.finish()
    await message.answer("Мы свяжемся с вами в ближайшее время!", reply_markup=menu_key)






# Button 2 -> 📈Forex savdo signallari
#
# !!! UZ !!!


@dp.message_handler(text=["Shartlarni qabul qilish va Obuna bo'lish", "Принятие условий и подписки", "‍«Ortga", "‍«Назад"], state=None)
async def agree(message: types.Message):
    if message.text == "Shartlarni qabul qilish va Obuna bo'lish":
        main_menu = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(message.from_user.full_name)
                ],
                [
                    types.KeyboardButton("◀️Bosh menyuga qaytish")
                ]
            ],
            resize_keyboard=True
        )
        await message.answer("Ism Familiyangizni to'liq yozib qoldiring!:", reply_markup=main_menu)
        await ForexSignalState.full_name.set()
    elif message.text == "‍«Ortga":
        await message.answer("📄 Kompaniyaning xizmatlar katalogi:", reply_markup=menu_key)
    elif message.text == "Принятие условий и подписки":
        main_menu_ru = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(message.from_user.full_name)
                ],
                [
                    types.KeyboardButton("◀️Вернуться в главный меню")
                ]
            ],
            resize_keyboard=True
        )
        await message.answer("Напишите свое полное имя!:", reply_markup=main_menu_ru)
        await ForexSignalState.full_name.set()
    elif message.text == "‍«Назад":
        await message.answer("📄 Каталог услуг компании:", reply_markup=menu_key_ru)
    else:
        pass



@dp.message_handler(state=ForexSignalState.full_name)
async def client_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(
        {'full_name': full_name}
    )
    await message.answer("Endi telefon raqamingizni xatosiz yuboring", reply_markup=register_course)
    await ForexSignalState.next()



@dp.message_handler(state=ForexSignalState.phone, content_types='contact')
async def client_phone(message: types.Message, state: FSMContext):
    phone = message['contact']['phone_number']
    await state.update_data(
        {'phone': phone}
    )
    await message.answer("🕗 Obuna bo'lish muddatini tanlang. To'lovni tasdiqlaganingizdan so'ng, siz avtomatik ravishda kirish uchun havolani olasiz, tanlangan muddat tugagandan so'ng guruhdan chiqarilasiz. Siz obunani istalgan vaqt yangilashingiz mumkin.👇🏻 Kerakli muddatni tanlang.", reply_markup=obuna)
    await ForexSignalState.choose_price.set()


@dp.message_handler(state=ForexSignalState.choose_price)
async def price(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(
        {'price': price}
    )
    await message.answer("Murojatingiz qabul qilindi!!!")
    client_data = await state.get_data()
    full_name = client_data.get('full_name')
    phone = client_data.get("phone")
    price = client_data.get('price')
    await message.answer("Sizga tez orada aloqaga chiqamiz.", reply_markup=menu_key)
    send_human_info(f"""INSERT INTO main_forexsignal ("full_name", "phone", "price") 
    values ('{full_name}', '{phone}', '{price}') returning *""")
    await state.finish()