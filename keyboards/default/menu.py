from aiogram import types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


language_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🇺🇿O'zbekcha"),
            KeyboardButton("🇷🇺Русский")
        ],
    ],
    resize_keyboard=True
)


menu_key = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton("‍🎓Treyding kursi 2023")
       ],
       [
           KeyboardButton("📈Forex savdo signallari")
       ],
       [
           KeyboardButton("ℹ️Bizning kompaniya haqida")
       ],
       [
           KeyboardButton("☎Aloqalar"),
           KeyboardButton("🇷🇺Tilni uzgartirish")
       ],
    ],
    resize_keyboard=True
)


menu_key_ru = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton("🎓Курсы по трейдингу 2023")
       ],
       [
           KeyboardButton("📈Торговые сигналы Forex")
       ],
       [
           KeyboardButton("ℹ️ О нашей компании")
       ],
       [
           KeyboardButton("☎️Контакты"),
           KeyboardButton("🇺🇿Сменить язык")
       ],
    ],
    resize_keyboard=True
)



client_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ],
    ],
    resize_keyboard=True
)


contact_info = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📞Telefon raqamni yuboring', request_contact=True)
        ],
    ],
    resize_keyboard=True
)


signal = ReplyKeyboardMarkup(
    keyboard=[
       [
            KeyboardButton("Shartlarni qabul qilish va Obuna bo'lish"),
       ],
       [
           KeyboardButton("‍«Ortga")
       ]
    ],
    resize_keyboard=True
)


signal_ru = ReplyKeyboardMarkup(
    keyboard=[
       [
            KeyboardButton("Принятие условий и подписки"),
       ],
       [

           KeyboardButton("‍«Назад")
       ]
    ],
    resize_keyboard=True
)



# main_menu = ReplyKeyboardMarkup(
#     keyboard=[
#        [
#            KeyboardButton("YOUR NAME"),
#            KeyboardButton("◀️Bosh menyuga qaytish")
#        ]
#     ],
#     resize_keyboard=True
# )


main_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton("◀️Вернуться в главный меню")
       ]
    ],
    resize_keyboard=True
)


register_course = ReplyKeyboardMarkup(
    keyboard=[
       [
            KeyboardButton('📞Telefon raqamni yuboring', request_contact=True)
       ],
       [
           KeyboardButton("◀️Bosh menyuga qaytish")
       ]
    ],
    resize_keyboard=True
)


register_course_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📞Отправить номер телефона:', request_contact=True),
        ],
       [
           KeyboardButton("◀️Вернуться в главный меню")
       ]
    ],
    resize_keyboard=True
)

obuna = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("1 oyga / $50.0"),
            KeyboardButton("3 oyga / $150.0")
        ],
        [
            KeyboardButton("6 oyga / $260.0"),
            KeyboardButton("12 oyga / $500.0")
        ],
        [
            KeyboardButton("◀️Bosh menyuga qaytish")
        ]
    ],
    resize_keyboard=True
)

obuna_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("1 месяц / $50.0"),
            KeyboardButton("3 месяц / $150.0")
        ],
        [
            KeyboardButton("6 месяц / $260.0"),
            KeyboardButton("12 месяц / $500.0")
        ],
        [
            KeyboardButton("◀️Вернуться в главный меню")
        ]
    ],
    resize_keyboard=True
)